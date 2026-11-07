import threading
import queue

class DataWorker:
    def __init__(self, root):
        self.root = root
        self.worker = None
        self.task_queue = queue.Queue()
        self.progress_callback = None
        self.done_callback = None
        self.c_text = None

    def run(self, tasks, progress=None, done=None, p_text=None, c_text=None):

        self.progress_callback = progress
        self.done_callback = done
        self.c_text = c_text

        # Show progress UI immediately before starting thread work
        if progress:
            progress(_text=p_text, animate=True)
            
        # Force Tkinter to update the display so the bar appears instantly
        self.root.update_idletasks()

        # Run tasks
        self.run_tasks(tasks=tasks)

        # What happens when the task is running and done
        self.poll_progress()

    def poll_progress(self):

        if self.is_worker_running():
            self.root.after(100, self.poll_progress)
            print("progress running...")

        else:

            if self.progress_callback:
                self.progress_callback(_text=self.c_text, animate=False)
                print("progress stopped...")

            if self.done_callback:
                self.done_callback()


    def is_worker_running(self) -> bool:
        return self.worker is not None and self.worker.is_alive()

    def worker_loop(self):

        while not self.task_queue.empty():
            task = self.task_queue.get()
            try:
                task()
            except Exception as e:
                print(f"Task failed with error: {e}")
            finally:
                self.task_queue.task_done()


    def run_tasks(self, tasks):
        if not isinstance(tasks, list):
            tasks = [tasks]

        for task in tasks:
            self.task_queue.put(task)

        if not self.is_worker_running():

            self.worker = threading.Thread(
                target=self.worker_loop,
                daemon=True
            )

            self.worker.start()

