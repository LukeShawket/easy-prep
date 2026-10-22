# Libraries
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
import ast

# Controllers
import controllers.view_controller as c_view

# Services
from services.parser import Parser
from services.plugin_loader import load_plugins
from services.data_worker import DataWorker

# Models
import models.workspace as w_space





class App():
    def __init__(self, reset_callback):

        # Initialize
        self.app = ttk.Window(title="Easy Prep",themename="darkly",size=(1200, 800))
        self.reset_callback = reset_callback
        # Insert more tools here and drop your .py file in tools folder
        self.work_space = w_space.WorkSpace()
        self.ctrl_view = c_view.ContrllerView(app=self.app, w_space=self.work_space)
        self.worker = DataWorker(self.app)
        self.app_base = self.get_app_dict()
        self.apps = load_plugins(app_base=self.app_base)

        # Core starts here.
        self.run_app()

        self.app.mainloop()

    def run_app(self):
        self.ctrl_view.start_app(parse_callback=self.parse_file)
        self.ctrl_view.apps = self.apps

     
    def parse_file(self, path):

        self.worker.run(
            task=lambda: self.parse_task(path),
            progress=self.ctrl_view.show_progress,
            done=self._file_loaded
        )


    def parse_task(self, path):

        parser = Parser()
        data = parser.parse_file(path)

        self.result = (data, parser)


    def _file_loaded(self):

        data, parser = self.result

        self.work_space.load_work_space_data(
            data=data,
            parser=parser
        )

        self.ctrl_view.load_dashboard()


    def get_app_dict(self):
        result = {}
        for tools_file in Path("apps").glob("*.py"):
            with open(tools_file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            clss = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]


            if clss:
                 result[tools_file.stem] = clss[0]

        return result



        
    def destroy(self, event=None):
            self.app.destroy()
            self.reset_callback()