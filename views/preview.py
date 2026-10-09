import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


class Preview:

    def __init__(self):
        pass


    def preview_process(self, frame, df):

    
        # Table Container
        view_frame = ttk.Frame(frame)
        view_frame.pack(fill=BOTH,expand=True)
        view_frame.widget_id = "view"

        # Scrollbars
        y_scroll = ttk.Scrollbar(view_frame, orient="vertical", bootstyle="round")
        x_scroll = ttk.Scrollbar(view_frame, orient="horizontal", bootstyle="round")

        self.view_tree = ttk.Treeview(
            view_frame,
            columns=list(df.columns),
            show="headings",
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        y_scroll.config(command=self.view_tree.yview)
        x_scroll.config(command=self.view_tree.xview)

        # Column headers
        for col in df.columns:
            self.view_tree.heading(col, text=col, anchor=W)
            self.view_tree.column(col, width=120, anchor=W)
        # Rows
        for _, row in df.iterrows():
            self.view_tree.insert("", "end", values=list(row))

        # Layout
        y_scroll.pack(side=RIGHT, fill="y")
        x_scroll.pack(side=BOTTOM, fill="x")
        self.view_tree.pack(side=LEFT, fill=BOTH, expand=True)

