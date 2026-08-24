import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import controllers.view_controller as c_view
import controllers.tool_controller as c_tool

import models.parser as ps




class App():
    def __init__(self, reset_callback):

        # Initialize
        self.app = ttk.Window(title="Easy Prep",themename="darkly",size=(1200, 800))
        self.reset_callback = reset_callback
        self.ctrl_view = c_view.ContrllerView(app=self.app)
        self.ctrl_tool = c_tool.ToolController()
        self.parser = ps.Parser()
        self.data = None
        self.tools = []

        # Insert more tools here and drop your .py file in tools folder
        self.tool_base = {
            "transformer": "Transformer",
            "slicer": "Slicer",
            "predict": "Predicter",
            "core_maker": "CoreMaker",
            "make_custom": "CustomMaker",
            "part_maker": "PartMaker",
            "price_maker": "PriceMaker",
        }

        # Core starts here.
        self.run_app()

        self.app.mainloop()

    def run_app(self):
        self.ctrl_view.start_app()
        self.tools = self.ctrl_tool.create_tools(tool_base=self.tool_base)
        self.ctrl_view.tools = self.tools
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

        
    def destroy(self, event=None):
            self.app.destroy()
            self.reset_callback()