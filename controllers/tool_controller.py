import os
import importlib

class ToolController:

    def __init__(self):

        self.tools = []


    def create_tools(self, tool_base:dict):
        for i, (mdl_name, cls_name) in enumerate(tool_base.items(), start=1):
            module = importlib.import_module(f"tools.{mdl_name}")
            cls = getattr(module, cls_name)

            self.tools.append(cls())

        return self.tools