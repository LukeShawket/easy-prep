import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Global_ui:
    def __init__(self, app):
        self.app = app

        self.create_header()

        self.content_frame = ttk.Frame(self.app)
        self.content_frame.pack(fill=BOTH, expand=True, padx=40, pady=10)


    def create_header(self):
        header = ttk.Frame(self.app, padding=(30, 20))
        header.pack(fill=X)

        ttk.Label(
            header,
            text="Easy Prep",
            font=("Segoe UI", 28, "bold")
        ).pack(side=LEFT)

        ttk.Button(
            header,
            text="Settings",
            bootstyle=(OUTLINE, SECONDARY)
        ).pack(side=RIGHT)

        return header

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    