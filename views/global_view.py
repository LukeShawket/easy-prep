import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class GlobalView:
    def __init__(self, app):
        self.app = app

        self.create_header()

        self.content_frame = ttk.Frame(self.app)
        self.content_frame.pack(fill=BOTH, expand=True, padx=40, pady=10)


    def create_header(self):
        self.header = ttk.Frame(self.app, padding=(30, 20))
        self.header.pack(fill=X)

        ttk.Label(self.header,text="Easy Prep",font=("Segoe UI", 28, "bold")).pack(side=LEFT)

        ttk.Button(self.header,text="Settings",bootstyle=(OUTLINE, SECONDARY), width=10).pack(side=RIGHT)
        

        return self.header

    def add_global_buttons(self):
        ttk.Button(self.header,text="Print",bootstyle=(OUTLINE, SECONDARY), width=10).pack(side=RIGHT, padx=5)
        ttk.Button(self.header,text="Export",bootstyle=(OUTLINE, SECONDARY), width=10).pack(side=RIGHT)
        ttk.Button(self.header,text="Home",bootstyle=(OUTLINE, SECONDARY), width=10).pack(side=RIGHT, padx=5)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    