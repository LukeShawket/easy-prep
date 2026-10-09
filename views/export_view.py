import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class ExportView:

    def __init__(self):
        pass
    
    def load_export_items(self, frame, path):

        export_frame = ttk.Frame(frame)
        export_frame.pack(side=LEFT, fill=BOTH, expand=True)
        export_frame.widget_id = "view"

        # Setup Canvas and Scrollbar Container
        canvas = tk.Canvas(export_frame, highlightthickness=0, bg=ttk.Style().colors.bg)
        scrollbar = ttk.Scrollbar(export_frame, orient="vertical", bootstyle=ROUND, command=canvas.yview)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create Scrollable Interior Frame
        scrollable_frame = ttk.Frame(canvas, padding=10)
        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Resizing triggers
        def _on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def _on_canvas_configure(event):
            canvas.itemconfig(window_id, width=event.width)

        scrollable_frame.bind("<Configure>", _on_frame_configure)
        canvas.bind("<Configure>", _on_canvas_configure)

        # File name
        name_frame = ttk.Labelframe(scrollable_frame, text=" File Name ", padding=15)
        name_frame.pack(fill=X, pady=(0, 20))
        self.filename_var = tk.StringVar(value="New File")

        ttk.Entry(
            name_frame,
            text="Enter a file name...",
            textvariable=self.filename_var,
        ).pack(side=LEFT, fill=X, expand=YES, padx=(0, 10))

        # File Format Selection (packed into scrollable_frame)
        format_frame = ttk.Labelframe(scrollable_frame, text=" File Format ", padding=15)
        format_frame.pack(fill=X, pady=(0, 15))

        self.export_format = tk.StringVar(value="xlsx")

        formats = [
            ("Excel Workbook (.xlsx)", "xlsx"),
            ("CSV (Comma Delimited) (.csv)", "csv"),
            ("Text(.txt)", "txt"),
            ("JSON (.json)", "json")
        ]


        for text, val in formats:
            ttk.Radiobutton(
                format_frame,
                text=text,
                value=val,
                variable=self.export_format,
                bootstyle="primary"
            ).pack(anchor=W, pady=3)



        # Export Options
        options_frame = ttk.Labelframe(scrollable_frame, text=" Export Options ", padding=15)
        options_frame.pack(fill=X, pady=(0, 15))

        self.include_header = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame,
            text="Include Column Headers",
            variable=self.include_header,
            bootstyle="primary-round-toggle"
        ).pack(anchor=W, pady=3)

        self.index_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="Include Row Index",
            variable=self.index_var,
            bootstyle="primary-round-toggle"
        ).pack(anchor=W, pady=3)



        # Destination Selection
        dest_frame = ttk.Labelframe(scrollable_frame, text=" Export Destination ", padding=15)
        dest_frame.pack(fill=X, pady=(0, 20))

        self.filepath_var = tk.StringVar(value=path)
        
        entry_container = ttk.Frame(dest_frame)
        entry_container.pack(fill=X)

        ttk.Entry(
            entry_container,
            textvariable=self.filepath_var,
        ).pack(side=LEFT, fill=X, expand=YES, padx=(0, 10))

        ttk.Button(
            entry_container,
            text="Browse...",
            bootstyle="secondary-outline",
            command=self.browse_destination
        ).pack(side=RIGHT)


    def get_export_values(self):

        export_values = {}

        export_values['file_name'] = self.filename_var.get()
        export_values['format'] = self.export_format.get()
        export_values['include_header'] = self.include_header.get()
        export_values['include_index'] = self.index_var.get()
        export_values['folder_path'] = self.filepath_var.get()

        return export_values


    def browse_destination(self):
        from tkinter import filedialog
    
        path = filedialog.askdirectory()

        if path:

            self.filepath_var.set(path)
