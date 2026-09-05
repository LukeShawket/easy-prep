from tkinter import filedialog
from ttkbootstrap.constants import *

import views.global_view as v_g
import views.home_view as v_h
import views.dashboard_view as v_d
from views.scroll_frame import ScrollableFrame
import views.process_view as v_p


class ContrllerView:

    def __init__(self, app):
        self.main_frame = None
        self.file_path = None
        self.folder_path = None

        self.sheet_count = None
        self.row_count = None
        self.column_count = None
        self.file_size = None
        self.display_table = None
        self.file_type = None
        self.raw_data = None
        self.current_sheet = None
        self.current_columns = None
        self.current_app_name = None
        self.apps = []
        self.funcs = {}
        self.widget = None
        self.vars = None

        self.v_global = v_g.GlobalView(app=app)
        self.v_home = v_h.HomeView(app=app)
        self.v_dashboard = v_d.DashboardView()
        self.v_process = v_p.ProcessView()
        
        self.main_frame = self.v_global.content_frame


    def start_app(self):

        self.v_home.build(self.main_frame)

        self.funcs["submit"] = self.submit_app

    def get_path(self, func_after):
        self.v_home.btn_open_file.config(command=lambda: self.ask_file(func=func_after))
        self.v_home.btn_open_folder.config(command=self.ask_folder)

    def ask_file(self, func):
        self.file_path = filedialog.askopenfilename()
        func(self.file_path)

    def ask_folder(self, func):
        self.folder_path = filedialog.askdirectory()

    def assign_file_info(self, cnt_sheet, cnt_row, cnt_clmn, table, _type, data, size):
        self.sheet_count = cnt_sheet
        self.row_count = cnt_row
        self.column_count = cnt_clmn
        self.display_table = table
        self.file_type = _type
        self.raw_data = data
        self.file_size = size

        self.load_dashboard()

    def load_dashboard(self):
        self.v_global.clear_content()

        for key, value in self.raw_data.items():
            if not self.current_sheet:
                self.current_sheet = value
                break
        self.v_dashboard.create_dashboard_frame(content_frame=self.main_frame)
        self.v_dashboard.create_workspace_header(sheet_count=self.sheet_count, 
                                                 row_count= self.row_count, 
                                                 column_count=self.column_count, 
                                                 file_size=self.file_size
                                                 )
        self.v_dashboard.create_workspace_main(_type=self.file_type, data=self.raw_data, display_table=self.display_table,act_names=self.get_app_names())
        # Assign sheet buttons
        for btn in self.v_dashboard.sheet_buttons:
            btn.configure(command=lambda b=btn: self.update_dashboard(b=b))

        # Assign action buttons
        for btn in self.v_dashboard.act_buttons:
                    btn.configure(command=lambda b=btn: self.update_process_panel(b=b))

        self.v_home.create_statusbar(status_text="Ready")


    def update_dashboard(self, b):
        b.configure(bootstyle=PRIMARY)

        if len(self.v_dashboard.sheet_buttons) > 1:
            for btn in self.v_dashboard.sheet_buttons:
                if btn != b:
                    btn.configure(bootstyle=(OUTLINE, PRIMARY))

        self.current_sheet = self.raw_data[str(b.cget("text"))]

        for title, item in self.v_dashboard.updatables.items():
            if title == "Rows":
                item.configure(text=len(self.current_sheet))
            elif title == "Columns":
                item.configure(text=len(self.current_sheet.columns))

        self.v_dashboard.work_panel(parent=self.v_dashboard.workspace,data=self.current_sheet)

        for btn in self.v_dashboard.act_buttons:
            btn.configure(bootstyle=(OUTLINE, PRIMARY))



    def get_app_names(self):
        app_names = []
        for app in self.apps:
            app_names.append(app.b_name)

        return app_names

    def update_process_panel(self, b):

        self.current_app_name = b.cget("text")

        # Fix here
        if self.current_columns:
            self.current_columns = self.current_sheet.columns.tolist()

        for key, value in self.raw_data.items():
            if not self.current_columns:
                self.current_columns = list(value.columns)
                break

        b.configure(bootstyle=PRIMARY)

        if len(self.v_dashboard.act_buttons) > 1:
            for btn in self.v_dashboard.act_buttons:
                if btn != b:
                    btn.configure(bootstyle=(OUTLINE, PRIMARY))

        for app in self.apps:
            if self.current_app_name == app.b_name:
                self.widget, self.vars = self.v_process.process_panel(title=f" {app.title} ",
                                            frame=self.v_dashboard.work_frame,
                                            fields=app.input_items,
                                            scrl = ScrollableFrame,
                                            cls=self.current_columns,
                                            funcs=self.funcs
                                        )


    def submit_app(self):    
        for app in self.apps:
            if app.b_name == self.current_app_name:
                for key, value in self.vars.items():
                    for item in app.input_items:
                        if item["name"] == key:
                            item["return"] = value.get()