from tkinter import filedialog
from ttkbootstrap.constants import *

import views.global_view as v_g
import views.home_view as v_h
import views.dashboard_view as v_d
from views.scroll_frame import ScrollableFrame


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
        self.tools = []

        self.v_global = v_g.GlobalView(app=app)
        self.v_home = v_h.HomeView(app=app)
        self.v_dashboard = v_d.DashboardView()
        
        self.main_frame = self.v_global.content_frame


    def start_app(self):

        self.v_home.build(self.main_frame)

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

        self.v_dashboard.create_dashboard_frame(content_frame=self.main_frame)
        self.v_dashboard.create_workspace_header(sheet_count=self.sheet_count, 
                                                 row_count= self.row_count, 
                                                 column_count=self.column_count, 
                                                 file_size=self.file_size
                                                 )
        self.v_dashboard.create_workspace_main(_type=self.file_type, data=self.raw_data, display_table=self.display_table,act_names=self.get_tool_names())
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

        data = self.raw_data[str(b.cget("text"))]

        self.v_dashboard.work_panel(parent=self.v_dashboard.workspace,data=data)

        for btn in self.v_dashboard.act_buttons:
            btn.configure(bootstyle=(OUTLINE, PRIMARY))



    def get_tool_names(self):
        tool_names = []
        for tool in self.tools:
            tool_names.append(tool.b_name)

        return tool_names  

    def update_process_panel(self, b):

        '''
        Example_work_ui_items = [
            ("Part Number", "entry"),
            ("Description", "entry"),
            ("Status", "combo", ["Open", "Closed"]),
            ("Needs Review", "check")
        ]
        '''
        b.configure(bootstyle=PRIMARY)

        if len(self.v_dashboard.act_buttons) > 1:
            for btn in self.v_dashboard.act_buttons:
                if btn != b:
                    btn.configure(bootstyle=(OUTLINE, PRIMARY))

        for tool in self.tools:
            if b.cget("text") == tool.b_name:
                self.v_dashboard.process_panel(title=f" {tool.title} ", 
                                                   fields=tool.input_items,
                                                   scrl = ScrollableFrame
                                                   )