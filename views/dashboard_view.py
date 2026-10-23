import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class DashboardView:

    def __init__(self):
        self.dashboard_frame = None
        self.sheet_buttons = []
        self.act_buttons = []
        self.updatables = {}
        self.selected_btn = None
        self.work_frame = None
        self.table_view = None


    def create_dashboard_frame(self, content_frame):
        self.dashboard_frame = ttk.Labelframe(
            content_frame,
            text=" WORK SPACE ",
            padding=20,
            bootstyle=PRIMARY
        )

        self.dashboard_frame.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        
    def create_workspace_header(self, sheet_count, row_count, column_count, file_size):

        # FILE INFO HEADER

        ttk.Label(self.dashboard_frame, text="File Overview",font=("Segoe UI", 18, "bold")).pack(anchor=W, pady=(0, 15))

        # STATS CARDS

        cards = ttk.Frame(self.dashboard_frame)
        cards.pack(fill=X)

        stats = [
            ("Sheets", sheet_count),
            ("Rows", row_count),
            ("Columns", column_count),
            ("File Size", f"{file_size} MB")
        ]

        for title, value in stats:

            card = ttk.Labelframe(cards,text=f" {title} ",padding=20)

            card.pack(side=LEFT,fill=X,expand=True,padx=5)

            kpi_lables = ttk.Label(card,text=value,font=("Segoe UI", 18, "bold"))
            kpi_lables.pack(pady=(5, 0))
            if title == "Rows" or title == "Columns":
                self.updatables[title] = kpi_lables



    def create_workspace_main(self, _type, data, display_table, act_names, scrll):
        
        self.workspace = ttk.Frame(self.dashboard_frame)
        self.workspace.pack(fill=BOTH,expand=True,pady=(20, 0))

        self.create_sheets_panel(parent=self.workspace, type_flag=_type, data=data)
        self.work_panel(parent=self.workspace, data=display_table, )
        self.create_actions_panel(parent=self.workspace, action_names=act_names)

        return self.workspace


    def create_sheets_panel(self, parent, type_flag=None, data=None):

        frame = ttk.Labelframe(parent, text=" SHEETS ", width=200)
        frame.pack(side=LEFT, padx=10, fill=Y)
        frame.pack_propagate(False)

        self.sheets_canvas = tk.Canvas(frame, highlightthickness=0, bd=0, relief="flat", bg=ttk.Style().colors.bg)
        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.sheets_canvas.yview, bootstyle="round")
        self.sheets_canvas.configure(yscrollcommand=scrollbar.set)
        self.button_frame = ttk.Frame(self.sheets_canvas, borderwidth=0)
        window_id = self.sheets_canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

        self.button_frame.bind(
            "<Configure>",
            lambda e: self.sheets_canvas.configure(scrollregion=self.sheets_canvas.bbox("all"))
        )

        self.sheets_canvas.bind(
            "<Configure>",
            lambda e: self.sheets_canvas.itemconfigure(window_id, width=e.width)
        )

        # Pack layout elements
        scrollbar.pack(side=RIGHT, fill=Y)
        self.sheets_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Mouse Wheel Scroll Logic
        def _on_mousewheel(event):
            if event.delta:
                self.sheets_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                self.sheets_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.sheets_canvas.yview_scroll(1, "units")

        def _bind_to_mousewheel(event):
            self.sheets_canvas.bind_all("<MouseWheel>", _on_mousewheel) # Windows
            self.sheets_canvas.bind_all("<Button-4>", _on_mousewheel) # Linux Up
            self.sheets_canvas.bind_all("<Button-5>", _on_mousewheel) # Linux Down

        def _unbind_from_mousewheel(event):
            self.sheets_canvas.unbind_all("<MouseWheel>")
            self.sheets_canvas.unbind_all("<Button-4>")
            self.sheets_canvas.unbind_all("<Button-5>")

        # Base background bindings
        self.sheets_canvas.bind("<Enter>", _bind_to_mousewheel)
        self.sheets_canvas.bind("<Leave>", _unbind_from_mousewheel)
        self.button_frame.bind("<Enter>", _bind_to_mousewheel)
        self.button_frame.bind("<Leave>", _unbind_from_mousewheel)

        self.sheet_buttons.clear()

        for key, value in data.items():
            btn = ttk.Button(self.button_frame, text=key, bootstyle=(OUTLINE, PRIMARY), padding=(10, 12))
            btn.pack(fill=X, padx=10, pady=4)
            
            # Bind the enter/leave scroll events directly to the button
            btn.bind("<Enter>", _bind_to_mousewheel)
            btn.bind("<Leave>", _unbind_from_mousewheel)
            
            self.sheet_buttons.append(btn)


        if self.sheet_buttons:
            self.sheet_buttons[0].configure(bootstyle=PRIMARY)



    def scroll_sheets_view(self, value):
        self.sheets_canvas.update_idletasks()
        self.sheets_canvas.yview_moveto(value)


    def add_new_sheet(self, text):

        new_btn = ttk.Button(self.button_frame,text=text,bootstyle=(OUTLINE, PRIMARY),padding=(10, 12))
        new_btn.pack(fill=X,padx=10,pady=4)
        self.sheet_buttons.append(new_btn)



    # DATA PREVIEW PANEL

    def work_panel(self, parent, data):

        if self.work_frame:
            self.work_frame.destroy()

        self.work_frame = ttk.Labelframe(parent, text=" DATA PREVIEW ", padding=10)
        self.work_frame.pack(side=LEFT,fill=BOTH,expand=True)
        self.work_frame.pack_propagate(False)

        # Toolbar
        toolbar = ttk.Frame(self.work_frame)
        toolbar.pack(fill=X,pady=(0, 10))

        ttk.Entry(toolbar).pack(side=LEFT,fill=X,expand=True,padx=(0, 5))
        ttk.Button(toolbar,text="Refresh",bootstyle=PRIMARY).pack(side=LEFT)

        # Table Container
        view_frame = ttk.Frame(self.work_frame)
        view_frame.pack(fill=BOTH,expand=True)

        self.table_view.preview_process(view_frame, data)


    # ACTIONS PANEL

    def create_actions_panel(self, parent, action_names):

        frame = ttk.Labelframe(parent, text=" ACTIONS ", width=200)
        frame.pack(side=RIGHT, padx=10, fill=Y)
        frame.pack_propagate(False)

        canvas = tk.Canvas(frame, highlightthickness=0, bd=0, relief="flat", bg=ttk.Style().colors.bg)
        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview, bootstyle="round")
        canvas.configure(yscrollcommand=scrollbar.set)
        button_frame = ttk.Frame(canvas, borderwidth=0)
        window_id = canvas.create_window((0, 0), window=button_frame, anchor="nw")

        button_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfigure(window_id, width=e.width)
        )

        # Pack layout elements
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Mouse Wheel Scroll Logic
        def _on_mousewheel(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        def _bind_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows
            canvas.bind_all("<Button-4>", _on_mousewheel)    # Linux scroll up
            canvas.bind_all("<Button-5>", _on_mousewheel)    # Linux scroll down

        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
            canvas.unbind_all("<Button-4>")
            canvas.unbind_all("<Button-5>")

        # Bind base container surfaces
        canvas.bind("<Enter>", _bind_to_mousewheel)
        canvas.bind("<Leave>", _unbind_from_mousewheel)
        button_frame.bind("<Enter>", _bind_to_mousewheel)
        button_frame.bind("<Leave>", _unbind_from_mousewheel)

        # Action Buttons
        for act_name in action_names:
            btn = ttk.Button(
                button_frame,
                text=act_name,
                bootstyle=(OUTLINE, PRIMARY),
                padding=(10, 12)
            )

            self.act_buttons.append(btn)
            btn.pack(fill=X, padx=10, pady=4)

            # pass scroll control back to canvas when hovering over this specific button
            btn.bind("<Enter>", _bind_to_mousewheel)
            btn.bind("<Leave>", _unbind_from_mousewheel)

