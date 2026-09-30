import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import controllers.view_controller as c_view
import controllers.app_controller as c_app

import models.parser as ps
from pathlib import Path
import ast




class App():
    def __init__(self, reset_callback):

        # Initialize
        self.app = ttk.Window(title="Easy Prep",themename="darkly",size=(1200, 800))
        self.reset_callback = reset_callback
        self.ctrl_view = c_view.ContrllerView(app=self.app)
        self.ctrl_app = c_app.AppController()
        self.parser = ps.Parser()
        self.data = None
        self.apps = []

        # Insert more tools here and drop your .py file in tools folder
        self.app_base = self.get_app_dict()

        # Core starts here.
        self.run_app()

        self.app.mainloop()

    def run_app(self):
        self.ctrl_view.start_app()
        self.apps = self.ctrl_app.create_apps(app_base=self.app_base)
        self.ctrl_view.apps = self.apps
        self.ctrl_view.get_path(func_after=self.parse_file)

    def parse_file(self, path):
        self.data = self.parser.parse_file(file_path=path)
        self.ctrl_view.assign_file_info(cnt_sheet=self.parser.get_sheet_count(),
                                        cnt_row=len(self.parser.get_first_table()),
                                        cnt_clmn=len(self.parser.get_first_table().columns),
                                        table=self.parser.get_first_table(),
                                        _type=self.parser.flag,
                                        data=self.data,
                                        size=self.parser.get_memory_usage(file_path=self.ctrl_view.file_path)
                                        )


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