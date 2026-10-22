import threading

class DataWorker:
    def __init__(self, root):
        self.root = root
        self.worker = None

    def run(self, task, progress=None, done=None):
        # 1. Show progress UI immediately before starting thread work
        if progress:
            progress(animate=True)
            
        # Force Tkinter to update the display so the bar appears instantly
        self.root.update_idletasks()

        # 2. Start the background thread
        self.worker = threading.Thread(
            target=task,
            daemon=True
        )
        self.worker.start()

        # 3. Begin monitoring the thread state
        self.run_progress(progress=progress, done=done)

    def run_progress(self, progress=None, done=None):
        if self.worker and self.worker.is_alive():
            # Keep polling every 100ms
            self.root.after(
                100,
                lambda: self.run_progress(progress, done)
            )
            print("progress running...")
        else:
            # Task finished
            if progress:
                progress(animate=False)
                print("progress stopped...")

            if done:
                done()