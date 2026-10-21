import importlib


def load_plugins(app_base:dict):
    apps = []
    for i, (mdl_name, cls_name) in enumerate(app_base.items(), start=1):
        module = importlib.import_module(f"apps.{mdl_name}")
        cls = getattr(module, cls_name)

        apps.append(cls())

    return apps