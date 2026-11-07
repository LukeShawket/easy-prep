import os
from pathlib import Path
import pandas as pd


class Parser:

    def __init__(self):
        self.data = {} 
        self.file_name = ""
        self.flag = ""
        self.file_path = None

    def parse_file(self, file_path):
        self.file_path = file_path
        if not self.file_path:
            return {}

        self.file_name = Path(self.file_path).stem
        ext = Path(self.file_path).suffix.lower()

        # 1. JSON Files
        if ext == ".json":
            try:
                # First attempt: standard pandas JSON parser
                df = pd.read_json(self.file_path)
            except Exception:
                try:
                    # Fallback attempt: line-delimited JSON (JSONL)
                    df = pd.read_json(self.file_path, lines=True)
                except Exception as e:
                    print(f"JSON Import Error: {e}")
                    df = pd.DataFrame()

            self.data = {self.file_name: df}
            self.flag = "json"

        # 2. Parquet Files
        elif ext in [".parquet", ".pq"]:
            try:
                df = pd.read_parquet(self.file_path)
                self.data = {self.file_name: df}
                self.flag = "parquet"
            except Exception as e:
                print(f"Parquet Import Error: {e}")
                self.data = {}
                self.flag = ""

        # 3. CSV Files
        elif ext == ".csv":
            df = pd.read_csv(self.file_path)
            self.data = {self.file_name: df}
            self.flag = "csv"

        # 4. Excel Files (.xlsx, .xls)
        elif ext in [".xlsx", ".xls"]:
            self.data = pd.read_excel(self.file_path, sheet_name=None)
            self.flag = "sheets" if len(self.data) > 1 else "sheet"

        # 5. Text Files (.txt)
        elif ext == ".txt":
            try:
                df = pd.read_csv(file_path, sep=None, engine="python")
            except Exception:
                try:
                    with open(
                        file_path, "r", encoding="utf-8", errors="ignore"
                    ) as f:
                        df = pd.DataFrame({"text": f.read().splitlines()})
                except Exception as inner_error:
                    df = pd.DataFrame()
                    print(f"TXT Import Error: {inner_error}")

            self.data = {self.file_name: df}
            self.flag = "text"

        else:
            print(f"Unsupported file type: {ext}")
            self.data = {}
            self.flag = ""

        return self.data

    def get_first_table(self):
        if not self.data:
            return None, ""
        first_sheet_name = next(iter(self.data))
        first_table = self.data[first_sheet_name]
        return first_table, first_sheet_name

    def get_sheet_count(self):
        return len(self.data)

    def get_memory_usage(self):
        file_size = os.path.getsize(self.file_path)
        return round((file_size / 1024) / 1024, 2)