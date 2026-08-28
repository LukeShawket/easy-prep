import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class ProcessView:

    def __init__(self):

        self.app_frame = None
        self.current_columns = None


    def process_panel(self, frame, title, fields, scrl, cls, funcs):

        if frame:
            for child in frame.winfo_children():
                child.destroy()

        if self.app_frame:
            self.app_frame.destroy()

        self.app_frame = ttk.Labelframe(frame, padding=10)
        self.app_frame.pack(side=LEFT,fill=BOTH,expand=True)
        self.app_frame.pack_propagate(False)
        self.app_frame.configure(text=title)

        self.current_columns = cls

        # Toolbar
        toolbar = ttk.Frame(self.app_frame)
        toolbar.pack(fill=X, pady=(0, 10))

        ttk.Button(toolbar,text="View Data",width=10,bootstyle=SECONDARY).pack(side=LEFT, padx=5)
        ttk.Button(toolbar,text="Preview",width=10,bootstyle=SECONDARY).pack(side=LEFT)
        ttk.Button(toolbar,text="Clear",width=10,bootstyle=SECONDARY).pack(side=LEFT, padx=5)
        ttk.Button(toolbar,text="Submit",width=10,bootstyle=SECONDARY,command=funcs["submit"]).pack(side=LEFT)

        # Scrollable Area
        scrl_area = scrl(self.app_frame)
        scrl_area.pack(fill=BOTH, expand=True)
        form_frame = scrl_area.scrollable_frame

        # Optional "card" container
        form_card = ttk.Labelframe(form_frame,text="Input Details",bootstyle="info",padding=15)
        form_card.pack(fill=X, padx=10, pady=10)

        field_var = {}
    
        # Dynamic Fields
        for field in fields:

            field_name = field["name"]
            field_type = field["type"]
            field_content = field["content"]

            row = ttk.Frame(form_card)
            row.pack(fill=X, pady=6)

            ttk.Label(row,text=field_name,width=20).pack(side=LEFT, padx=(0, 10))

            if field_type == "entry":
                widget, var = self.load_entry_field(row=row)

            elif field_type == "combo":
                widget, var = self.load_combo_field(row=row,value=field["content"])

            elif field_type == "check":
                widget, var = self.load_check_field(row=row)

            elif field_type == "mst":
                if field_content == "columns":
                    widget, var = self.load_mst(row=row, items=self.current_columns)

            elif field_type == "sst":
                if field_content == "columns":
                    widget, var = self.load_sst(row=row, items=self.current_columns)

            else:
                    continue

            widget.pack(side=LEFT,fill=X,expand=True)
            field_var[field_name] = var
            

        return widget, field_var

                


    def load_entry_field(self, row):
        var = tk.StringVar()
        widget = ttk.Entry(row,textvariable=var)

        return widget, var

    def load_combo_field(self, row, value):
        var = tk.StringVar()
        widget = ttk.Combobox(row,textvariable=var,values=value,state="readonly")

        return widget, var

    def load_check_field(self, row):
        var = tk.BooleanVar()
        widget = ttk.Checkbutton(row,variable=var,bootstyle="round-toggle")

        return widget, var

    def load_mst(self, row, items=None):
        var = {}
        widget = ttk.Frame(row)
        canvas = tk.Canvas(widget, height=35, highlightthickness=0, bg=ttk.Style().colors.bg)
        canvas.pack(fill="x", expand=True)

        scrollbar = ttk.Scrollbar(widget,orient="horizontal", bootstyle=ROUND,command=canvas.xview)
        scrollbar.pack(fill="x")

        canvas.configure(xscrollcommand=scrollbar.set)
        checkbox_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

        checkbox_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for item in items:
            var[item] = tk.BooleanVar()
            ttk.Checkbutton(checkbox_frame,text=item,
            variable=var[item],
            bootstyle="toolbutton").pack(side="left", padx=4)

        widget.selection_vars = var

        return widget, var


    def load_sst(self, row, items=None):
        var = {}
        widget = ttk.Frame(row)
        canvas = tk.Canvas(widget, height=35, highlightthickness=0, bg=ttk.Style().colors.bg)
        canvas.pack(fill="x", expand=True)

        scrollbar = ttk.Scrollbar(widget,orient="horizontal", bootstyle=ROUND,command=canvas.xview)
        scrollbar.pack(fill="x")

        canvas.configure(xscrollcommand=scrollbar.set)
        checkbox_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

        checkbox_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for item in items:
            var[item] = tk.BooleanVar()
            ttk.Checkbutton(checkbox_frame,text=item,
            variable=var[item],
            bootstyle="toolbutton").pack(side="left", padx=4)

        return widget, var

