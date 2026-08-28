import os
import importlib

class ToolController:

    def __init__(self):

        pass


    def create_apps(self, app_base:dict):
        apps = []
        for i, (mdl_name, cls_name) in enumerate(app_base.items(), start=1):
            module = importlib.import_module(f"apps.{mdl_name}")
            cls = getattr(module, cls_name)

            apps.append(cls())

        return apps