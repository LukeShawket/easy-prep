import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class ProcessView:

    def __init__(self):

        self.current_columns = None
        self.input_schema = None
        self.next_state = 1
        self.max_state = 0
        self.form_card = None
        self.field_var = {}
        self.check_btn_var = {}
        self.toolbar = None

    def process_panel(self, frame, title, fields, scrl, cls, funcs):


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
        ttk.Button(self.toolbar,text="Add Sheet",width=10,bootstyle=SECONDARY,command=funcs["addsheet"]).pack(side=LEFT)
        ttk.Button(self.toolbar,text="Export",width=10,bootstyle=SECONDARY,command=funcs["export"]).pack(side=LEFT, padx=5)

        # Scrollable Area
        form_frame = scrl(frame)
        form_frame.pack(fill=BOTH, expand=True)

        # Optional "card" container
        self.form_card = ttk.Labelframe(form_frame.content,text="Input Details",bootstyle="info",padding=15)
        self.form_card.pack(fill=BOTH, padx=10, pady=10)

        frame.update_idletasks()



        var = self.render_fields()

        return var




    def render_fields(self, wipe=None, parent=None, _child=None):

        # Dynamic Fields
        for field in self.input_schema:

            if field["state"] > self.max_state:
                self.max_state = field["state"]

            if wipe:
                for widget in self.form_card.winfo_children():
                    if hasattr(widget, "field_id"):
                        if widget.field_id == _child["id"] or field["parent_id"] == _child["id"]:
                            widget.destroy()
                        

            elif int(field.get("state", 1)) == self.next_state and not wipe:

                field_name = None
                frame_name = None

                if "name" in field:
                    field_name = field["name"]
                elif "frame_name" in field:
                    frame_name = field["frame_name"]

                    
                field_id = field["id"]
                field_type = field["type"]
                field_content = field["content"]
                is_child = field["is_child"]
                widget = None

                if not is_child:

                    row = ttk.Frame(self.form_card)
                    row.pack(fill=X, pady=6)

                    if field_name:
                        ttk.Label(row,text=field_name,width=20).pack(side=LEFT, padx=(0, 10))

                    if field_type == "entry":
                        widget, var = self.load_entry_field(row=row)

                    elif field_type == "combo":
                        widget, var = self.load_combo_field(row=row,value=field["content"])

                    elif field_type == "check":
                        widget, var = self.load_check_field(row=row)
                        for child in widget.winfo_children():
                            if isinstance(child, ttk.Checkbutton):
                                child.configure(command=lambda w=widget, v=var, f=field: self.check_btn_update(wid=w, var=v, fld=f))
                            else:
                                child.configure(text=field["notify_false"])

                    elif field_type == "multi-select":
                        widget, var = self.load_multi_selection_field(row=row, _field=field, _frame_name=frame_name or field_name)

                    else:
                            continue
                    

                else:
                    if parent:
                        if field.get("parent_id") == parent.get("id"):

                            row = ttk.Frame(self.form_card)
                            row.field_id = _child["id"]
                            row.pack(fill=X, pady=6)

                            if field_name:
                                ttk.Label(row,text=field_name,width=20).pack(side=LEFT, padx=(0, 10))
                            
                            if field_type == "entry":
                                widget, var = self.load_entry_field(row=row)
        
                            elif field_type == "combo":
                                widget, var = self.load_combo_field(row=row,value=field["content"])
        
                            elif field_type == "check":
                                widget, var = self.load_check_field(row=row)
                                for child in widget.winfo_children():
                                    if isinstance(child, ttk.Checkbutton):
                                        child.configure(command=lambda w=widget, v=var, f=field: self.check_btn_update(wid=w, var=v, fld=f))
                                    else:
                                        child.configure(text=field["notify_false"])
        
                            elif field_type == "multi-select":
                                widget, var = self.load_multi_selection_field(row=row, _field=field, _frame_name=frame_name or field_name)
                                
                            else:
                                    continue


                    else:
                        print("No parent")

                if widget:
                    widget.pack(side=LEFT,fill=X,expand=True)
                    self.field_var[field_id] = var

        return self.field_var



    def check_btn_update(self, wid, var, fld):
        cld = None
        for f in self.input_schema:
            if f["parent_id"] == fld["id"]:
                cld = f
        if self.next_state < self.max_state:
            self.next_state = fld.get("state") + 1
        for field in self.input_schema:
            if field.get("state") == self.next_state:
                if var.get() != field.get("depend_value"):
                    self.next_state -= 1
                    for child in wid.winfo_children():
                        if isinstance(child, ttk.Label):
                            child.configure(text=fld["notify_false"])
                    self.render_fields(wipe=True, _child=cld)

                else:
                    for child in wid.winfo_children():
                        if isinstance(child, ttk.Label):
                            child.configure(text=fld["notify_true"])

                    self.render_fields(parent=fld, _child=cld)
                    
                break

                


    def load_entry_field(self, row):
        var = tk.StringVar()
        widget = ttk.Entry(row,textvariable=var)

        return widget, var

    def load_combo_field(self, row, value):
        var = tk.StringVar()
        widget = ttk.Combobox(row,textvariable=var,values=value,state="readonly")

        return widget, var

    def load_check_field(self, row):

        widget = ttk.Frame(row)

        var = tk.BooleanVar()
        ttk.Checkbutton(widget, variable=var, bootstyle="round-toggle").pack(side=LEFT,fill=X,expand=True)
        ttk.Label(widget).pack(side=LEFT,fill=X,expand=True)

        return widget, var


    def load_multi_selection_field(self, row, _field, _frame_name):
        layout = _field.get("layout")
        check_vars = {}

        selection = (
            self.current_columns
            if _field["content"] == "columns"
            else _field["content"]
        )

        # Outer container
        widget = ttk.Labelframe(
            row,
            text=f" {_frame_name} ",
            padding=10
        )

        if layout == "horizontal":
            # Canvas is the visible viewport
            canvas = tk.Canvas(
                widget,
                height=40,
                highlightthickness=0,
                bg=ttk.Style().colors.bg
            )
            canvas.pack(fill=X, expand=True)

            # Keep a reference to the embedded window
            content_frame = ttk.Frame(canvas)

            window_id = canvas.create_window(
                (0, 0),
                window=content_frame,
                anchor="nw"
            )

            # Horizontal scrollbar
            scrollbar = ttk.Scrollbar(
                widget,
                orient="horizontal",
                command=canvas.xview,
                bootstyle="round"
            )
            scrollbar.pack(fill=X)

            canvas.configure(xscrollcommand=scrollbar.set)

            # Update scrollable area when content changes
            def update_scroll_region(event=None):
                canvas.configure(
                    scrollregion=canvas.bbox(window_id)
                )

            content_frame.bind("<Configure>", update_scroll_region)

            # Create checkboxes inside the embedded frame
            for item in selection:
                var = tk.BooleanVar(value=False)
                check_vars[item] = var

                ttk.Checkbutton(
                    content_frame,
                    text=item,
                    variable=var,
                    bootstyle="primary"
                ).pack(side=LEFT, padx=5)

            # Calculate the initial content width
            content_frame.update_idletasks()
            update_scroll_region()

            # Optional Shift + mouse wheel scrolling
            canvas.bind(
                "<Shift-MouseWheel>",
                lambda e: (
                    canvas.xview_scroll(
                        -1 if e.delta > 0 else 1,
                        "units"
                    ),
                    "break"
                )[1]
            )

            return widget, check_vars

        # Vertical layout
        for item in selection:
            var = tk.BooleanVar(value=False)
            check_vars[item] = var

            ttk.Checkbutton(
                widget,
                text=item,
                variable=var,
                bootstyle="primary"
            ).pack(anchor=W, pady=3)

        return widget, check_vars



    

