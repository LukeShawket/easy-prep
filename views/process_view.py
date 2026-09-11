import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class ProcessView:

    def __init__(self):

        self.current_columns = None
        self.input_schema = None
        self.gui_index = 1
        self.form_card = None
        self.field_var = {}
        self.last_added_field_id = None
        self.toolbar = None


    def process_panel(self, frame, title, fields, scrl, cls, funcs):

        self.gui_index = 0

        if frame:
            for child in frame.winfo_children():
                child.destroy()

        frame.configure(text=title)

        self.current_columns = cls
        self.input_schema = fields

        # Toolbar
        self.toolbar = ttk.Frame(frame)
        self.toolbar.pack(fill=X, pady=(0, 10))

        ttk.Button(self.toolbar,text="View Data",width=10,bootstyle=SECONDARY,command=funcs["view"]).pack(side=LEFT, padx=5)
        ttk.Button(self.toolbar,text="Preview",width=10,bootstyle=SECONDARY,command=funcs["preview"]).pack(side=LEFT)
        ttk.Button(self.toolbar,text="Clear",width=10,bootstyle=SECONDARY,command=funcs["clear"]).pack(side=LEFT, padx=5)
        ttk.Button(self.toolbar,text="Add Sheet",width=10,bootstyle=SECONDARY).pack(side=LEFT)
        ttk.Button(self.toolbar,text="Export",width=10,bootstyle=SECONDARY).pack(side=LEFT).pack(side=LEFT, padx=5)

        # Scrollable Area
        scrl_area = scrl(frame)
        scrl_area.pack(fill=BOTH, expand=True)
        form_frame = scrl_area.scrollable_frame

        # Optional "card" container
        self.form_card = ttk.Labelframe(form_frame,text="Input Details",bootstyle="info",padding=15)
        self.form_card.pack(fill=X, padx=10, pady=10)


        self.gui_index += 1
        var = self.render_fields()

        return var




    def render_fields(self, wipe=None):

        if wipe:
            for widget in self.form_card.winfo_children():
                if hasattr(widget, "field_id"):
                    if widget.field_id == self.last_added_field_id:
                        widget.destroy()

        # Dynamic Fields
        for field in self.input_schema:

            if int(field.get("state", 1)) == self.gui_index and not wipe:

                field_name = field["name"]
                field_type = field["type"]
                field_content = field["content"]

                row = ttk.Frame(self.form_card)
                row.field_id = field.get("id")
                row.pack(fill=X, pady=6)

                ttk.Label(row,text=field_name,width=20).pack(side=LEFT, padx=(0, 10))

                if field_type == "entry":
                    widget, var = self.load_entry_field(row=row)

                elif field_type == "combo":
                    widget, var = self.load_combo_field(row=row,value=field["content"])

                elif field_type == "check":
                    widget, var = self.load_check_field(row=row)
                    widget.configure(command=lambda v= var, f=field: self.check_btn_update(var=v, fld=f))

                elif field_type == "multi-select":
                    if field_content == "columns":
                        widget, var = self.load_mst(row=row, items=self.current_columns)

                elif field_type == "singgle_select":
                    if field_content == "columns":
                        widget, var = self.load_mst(row=row, items=self.current_columns)

                else:
                        continue

                widget.pack(side=LEFT,fill=X,expand=True)
                self.field_var[field_name] = var

        return self.field_var



    def check_btn_update(self, var, fld):
        next_state = fld.get("state") + 1
        for field in self.input_schema:
            if field.get("state") == next_state:
                if var.get() != field.get("depend_value"):
                    self.gui_index -= 1
                    self.render_fields(wipe=True)

                else:
                    self.gui_index += 1
                    self.last_added_field_id = field.get("id")
                    self.render_fields()
                    
                break

                


    def load_entry_field(self, row):
        var = tk.StringVar()
        widget = ttk.Entry(row,textvariable=var)
        widget.field_id = id

        return widget, var

    def load_combo_field(self, row, value):
        var = tk.StringVar()
        widget = ttk.Combobox(row,textvariable=var,values=value,state="readonly")
        widget.field_id = id

        return widget, var

    def load_check_field(self, row):
        var = tk.BooleanVar()
        widget = ttk.Checkbutton(row,variable=var,bootstyle="round-toggle")
        widget.field_id = id

        return widget, var

    def load_mst(self, row, items=None):
        var = {}
        widget = ttk.Frame(row)
        widget.field_id = id
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

