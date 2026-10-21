import threading


class DataWorker:

    def __init__(self, root):
        self.root = root

    def run(self, task, on_success=None, on_progress=None):

        def progress(percent, message=""):

            if on_progress:
                self.root.after(
                    0,
                    lambda: on_progress(percent, message)
                )

        def worker():

            result = task(progress)

            if on_success:
                self.root.after(
                    0,
                    lambda: on_success(result)
                )

        threading.Thread(
            target=worker,
            daemon=True
        ).start()