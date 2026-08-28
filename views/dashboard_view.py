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

        ttk.Label(
            self.dashboard_frame,
            text="File Overview",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor=W, pady=(0, 15))

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

            card = ttk.Labelframe(
                cards,
                text=f" {title} ",
                padding=20
            )

            card.pack(
                side=LEFT,
                fill=X,
                expand=True,
                padx=5
            )

            ttk.Label(
                card,
                text=title,
                font=("Segoe UI", 10),
            ).pack()

            kpi_lables = ttk.Label(card,text=value,font=("Segoe UI", 18, "bold"))
            kpi_lables.pack(pady=(5, 0))
            if title == "Rows" or title == "Columns":
                self.updatables[title] = kpi_lables



    def create_workspace_main(self, _type, data, display_table, act_names):
        
        self.workspace = ttk.Frame(self.dashboard_frame)
        self.workspace.pack(
            fill=BOTH,
            expand=True,
            pady=(20, 0)
        )

        print(_type)
        self.create_sheets_panel(parent=self.workspace, type_flag=_type, data=data)
        self.work_panel(parent=self.workspace, data=display_table, )
        self.create_actions_panel(parent=self.workspace, action_names=act_names)

        return self.workspace


    def create_sheets_panel(self, parent, type_flag=None, data=None):
    
        frame = ttk.Labelframe(parent, text=" SHEETS ",width=200)
        frame.pack(side=LEFT,padx=10,fill=Y)
        frame.pack_propagate(False)

        canvas = tk.Canvas(frame, highlightthickness=0, bd=0, relief="flat", bg=ttk.Style().colors.bg)
        scrollbar = ttk.Scrollbar(frame,orient=VERTICAL,command=canvas.yview,bootstyle="round")
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



        if type_flag == "sheets" or type_flag == "sheet":

            self.sheet_buttons.clear()

            for key, value in data.items():
                btn = ttk.Button(button_frame,text=key,bootstyle=(OUTLINE, PRIMARY),padding=(10, 12))
                btn.pack(fill=X,padx=10,pady=4)
                self.sheet_buttons.append(btn)

        else:
            self.sheet_buttons.clear()
            btn = ttk.Button(button_frame,text="Sheet",bootstyle=(OUTLINE, PRIMARY),padding=(10, 12))
            btn.pack(fill=X,padx=10,pady=4)
            self.sheet_buttons.append(btn)

        self.sheet_buttons[0].configure(bootstyle=PRIMARY)


    # ==================================
    # DATA PREVIEW PANEL
    # ==================================

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

        # Scrollbars
        y_scroll = ttk.Scrollbar(view_frame, orient="vertical", bootstyle="round")
        x_scroll = ttk.Scrollbar(view_frame, orient="horizontal", bootstyle="round")

        self.view_tree = ttk.Treeview(
            view_frame,
            columns=list(data.columns),
            show="headings",
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        y_scroll.config(command=self.view_tree.yview)
        x_scroll.config(command=self.view_tree.xview)

        # Column headers
        for col in data.columns:
            self.view_tree.heading(col, text=col, anchor=W)
            self.view_tree.column(col, width=120, anchor=W)
        # Rows
        for _, row in data.iterrows():
            self.view_tree.insert("", "end", values=list(row))

        # Layout
        y_scroll.pack(side=RIGHT, fill="y")
        x_scroll.pack(side=BOTTOM, fill="x")
        self.view_tree.pack(side=LEFT, fill=BOTH, expand=True)


    # ACTIONS PANEL

    def create_actions_panel(self, parent, action_names):

        frame = ttk.Labelframe(parent, text=" ACTIONS ", width=200)
        frame.pack(side=RIGHT,padx=10,fill=Y)
        frame.pack_propagate(False)

        canvas = tk.Canvas(frame, highlightthickness=0, bd=0, relief="flat", bg=ttk.Style().colors.bg)
        scrollbar = ttk.Scrollbar(frame,orient=VERTICAL,command=canvas.yview,bootstyle="round")
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

        # Action Buttons
        for act_name in action_names:
            btn = ttk.Button(
                button_frame,
                text=act_name,
                bootstyle=(OUTLINE, PRIMARY),
                padding=(10, 12)
            )

            self.act_buttons.append(btn)

            btn.pack(fill=X,padx=10,pady=4)

