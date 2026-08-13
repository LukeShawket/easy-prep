from tkinter import filedialog
from pathlib import Path
import pandas as pd
import os


class Uploader:

    def __init__(self):
        self.data = None
        self.file_path = ""
        self.file_name = ""
        self.flag = ""

    def upload(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_name = Path(self.file_path).stem

            if self.file_path.endswith(".csv"):
                self.data = pd.read_csv(self.file_path)
                self.flag = "csv"

            elif self.file_path.endswith(".xlsx") or self.file_path.endswith(".xls"):
                self.data = pd.read_excel(self.file_path, sheet_name=None)
                if len(self.data) > 1:
                    self.flag = "sheets"
                else:
                    self.flag = "sheet"

            elif self.file_path.lower().endswith(".txt"):
                try:
                    self.data = pd.read_csv(
                        self.file_path,
                        sep=None,
                        engine="python"
                    )

                    self.flag = "text"

                except Exception as e:

                    try:
                        with open(
                            self.file_path,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ) as f:

                            self.data = pd.DataFrame(
                                {"text": f.read().splitlines()}
                            )

                        self.flag = "text"

                    except Exception as inner_error:

                        self.data = None
                        self.flag = ""

                        print(f"TXT Import Error: {e}")
                        print(f"Fallback Error: {inner_error}")

            else:
                print(f"Unsupported file type!!!")
                
        return self.data


    def get_first_table(self):

        if self.flag == "sheets" or self.flag == "sheet":
            first_table = next(iter(self.data.values()))

        elif self.flag == "csv" or self.flag == "text":
            first_table = self.data

        return first_table



    def get_sheet_count(self):

            if self.flag == "sheets" or self.flag == "sheet":
                count = len(self.data)

            elif self.flag == "csv" or self.flag == "text":
                count = 1
    
            return count


    def get_memory_usage(self):

        file_size = os.path.getsize(self.file_path)

        file_size = round((file_size/1024)/1024, 2)

        return file_size