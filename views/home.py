import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Home_ui:
    def __init__(self, app, content_frame):
        self.app = app

        self.content_frame = content_frame

    def home_view(self, func_upload):
        self.create_hero(self.content_frame)
        self.create_drop_zone(self.content_frame, func_upload)
        self.create_bottom_section(self.content_frame)


    def create_hero(self, parent):
        hero = ttk.Frame(parent)
        hero.pack(fill=X, pady=(20, 30))

        ttk.Label(
            hero,
            text="Your company name",
            font=("Segoe UI", 20, "bold")
        ).pack()

        ttk.Label(
            hero,
            text="Import CSV, Excel, or text files to begin.",
            font=("Segoe UI", 11),
            bootstyle=SECONDARY
        ).pack(pady=(5, 25))

        return hero

    # =========================
    # DROP ZONE
    # =========================

    def create_drop_zone(self, parent, upload_func):
        drop_frame = ttk.Labelframe(
            parent,
            text=" FILE IMPORT ",
            padding=40,
            bootstyle=PRIMARY
        )

        drop_frame.pack(fill=X)

        ttk.Label(
            drop_frame,
            text="📄",
            font=("Segoe UI Emoji", 40)
        ).pack()

        ttk.Label(
            drop_frame,
            text="Drop files here",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(10, 5))

        ttk.Label(
            drop_frame,
            text="CSV • XLSX • TXT",
            bootstyle=SECONDARY
        ).pack()

        buttons = ttk.Frame(drop_frame)
        buttons.pack(pady=25)

        ttk.Button(
            buttons,
            text="Open File",
            bootstyle=PRIMARY,
            width=18,
            command=upload_func
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            buttons,
            text="Open Folder",
            bootstyle=(OUTLINE, PRIMARY),
            width=18,
            command=upload_func
        ).pack(side=LEFT, padx=5)

        return drop_frame


    # BOTTOM CONTAINER

    def create_bottom_section(self, parent):
        bottom = ttk.Frame(parent)
        bottom.pack(fill=BOTH, expand=True, pady=30)

        self.create_recent_files(bottom)
        self.create_quick_actions(bottom)

        return bottom


    # RECENT FILES

    def create_recent_files(self, parent):
        recent = ttk.Labelframe(
            parent,
            text=" Recent Files ",
            padding=15
        )

        recent.pack(
            side=LEFT,
            fill=BOTH,
            expand=True,
            padx=(0, 10)
        )

        files = [
            ("inventory.xlsx", "Today"),
            ("parts_master.csv", "Yesterday"),
            ("pricing_update.xlsx", "2 days ago")
        ]

        for file, date in files:
            row = ttk.Frame(recent)
            row.pack(fill=X, pady=5)

            ttk.Label(
                row,
                text=f"📄 {file}"
            ).pack(side=LEFT)

            ttk.Label(
                row,
                text=date,
                bootstyle=SECONDARY
            ).pack(side=RIGHT)

        return recent


    # QUICK ACTIONS

    def create_quick_actions(self, parent):
        actions = ttk.Labelframe(
            parent,
            text=" Quick Actions ",
            padding=15
        )

        actions.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )

        card_container = ttk.Frame(actions)
        card_container.pack(fill=BOTH, expand=True)

        cards = [
            ("🧹 Clean Data", "Remove blanks and spaces"),
            ("🔀 Split Columns", "Delimiter-based splitting"),
            ("🔤 Format Text", "Upper, lower, title case")
        ]

        for title, desc in cards:
            card = ttk.Frame(
                card_container,
                padding=12
            )

            card.pack(fill=X, pady=6)

            ttk.Label(
                card,
                text=title,
                font=("Segoe UI", 11, "bold")
            ).pack(anchor=W)

            ttk.Label(
                card,
                text=desc,
                bootstyle=SECONDARY
            ).pack(anchor=W)

        return actions

    # STATUS BAR

    def create_statusbar(self, status_text):
        status = ttk.Frame(self.app, padding=10)
        status.pack(fill=X)

        ttk.Label(
            status,
            text=status_text
        ).pack(side=LEFT)

        return status