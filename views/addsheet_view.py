import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class AddSheetView:

    def __init__(self):
        pass
    
    def load_sheet_items(self, frame):

        main_frame = ttk.Frame(frame)
        main_frame.pack(side=LEFT, fill=BOTH, expand=True)
        main_frame.widget_id = "view"


        # File name
        name_frame = ttk.Labelframe(main_frame, text=" File Name ", padding=15)
        name_frame.pack(fill=X, pady=(0, 20))
        self.filename_var = tk.StringVar(value="New File")

        ttk.Entry(
            name_frame,
            text="Enter a file name...",
            textvariable=self.filename_var,
        ).pack(side=LEFT, fill=X, expand=YES, padx=(0, 10))


        # Export Options
        options_frame = ttk.Labelframe(main_frame, text=" Add Options ", padding=15)
        options_frame.pack(fill=X, pady=(0, 15))

        self.include_header = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="Overwrite Original",
            variable=self.include_header,
            bootstyle="primary-round-toggle"
        ).pack(anchor=W, pady=3)


    def get_export_values(self):

        add_values = {}

        add_values['file_name'] = self.filename_var.get()
        add_values['include_header'] = self.include_header.get()

        return add_values