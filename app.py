import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import _global.ui as g_ui
import views.home as v_home
import views.work_space as v_dashboard

import tools.uploader as loader




class App():
    def __init__(self, reset_callback):

        # Initialize
        self.app = ttk.Window(
            title="Easy Prep",
            themename="darkly",
            size=(1200, 800)
        )
        self.reset_callback = reset_callback

        #classes
        self.ui_global = g_ui.Global_ui(app=self.app)
        self.home_view = v_home.Home_ui(app=self.app,content_frame=self.ui_global.content_frame)
        self.file_uploader = loader.Uploader()
        self.dashboard_view = v_dashboard.WorkSpaceView()


        # values
        self.data = None
        self.first_table = None
        self.file_path = ""
        self.file_type = ""

        # main
        self.run_app()

        self.app.mainloop()

    def run_app(self):
        self.home_view.home_view(func_upload=self.upload_file)



    def upload_file(self):

        self.data = self.file_uploader.upload()
        self.first_table = self.file_uploader.get_first_table()

        self.ui_global.clear_content()

        self.dashboard_view.display_dashboard(dashboard_frame=self.ui_global.content_frame,
                                              sheet_count=self.file_uploader.get_sheet_count(),
                                              row_count=len(self.first_table),
                                              column_count=len(self.first_table.columns),
                                              file_size=self.file_uploader.get_memory_usage(),
                                              _type=self.file_uploader.flag,
                                              data=self.data,
                                              first_table=self.first_table
                            )

        self.home_view.create_statusbar(status_text=f"{self.file_uploader.flag} uploaded. File Type: {type(self.data)}")


    def destroy(self, event=None):
            self.app.destroy()
            self.reset_callback()