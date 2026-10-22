from services.parser import Parser

class WorkSpace:

    def __init__(self):

        # Initial
        self.raw_data = None
        self.file_type = None
        self.memo_usage = None
        self.sheet_count = None

        # Updatable
        self.current_sheet = None
        self.current_sheet_name = None
        self.current_row_count = None
        self.current_columns_count = None
        self.current_columns = None

    def load_work_space_data(self, data, parser: Parser):

        self.raw_data = data
        self.file_type = parser.flag
        self.memo_usage = parser.get_memory_usage()
        self.sheet_count = parser.get_sheet_count()

        self.current_sheet, self.current_sheet_name = parser.get_first_table()
        self.current_row_count = len(self.current_sheet)
        self.current_columns = self.current_sheet.columns.tolist()
        self.current_columns_count = len(self.current_sheet.columns)

    def update_current_data(self, name):

        self.current_sheet_name = name
        self.current_sheet = self.raw_data[name]
        self.current_sheet_name = name
        self.current_row_count = len(self.current_sheet)
        self.current_columns_count = len(self.current_sheet.columns)
        self.current_columns = self.current_sheet.columns.tolist()