import pandas as pd

class Validater:

    def __init__(self):

        self.b_name = "Data Validation"
        self.title = "Validation"
        self.default_path = "C:/Users/fxiaowuk/Downloads"
        
        self.input_items = [
                            {
                                "id": 1,
                                "state": 1,
                                "field_name": "Add Columns",
                                "type": "check",
                                "notify_true": "Select Columns",
                                "notify_false": "All Columns",
                                "content": "continue",
                                "return": None
                            },
                            {
                                "id": 2,
                                "state": 1,
                                "field_name": "Add Validation",
                                "type": "check",
                                "notify_true": "Select Validation",
                                "notify_false": "All Validation",
                                "content": "continue",
                                "return": None
                            },
                            {
                                "id": 3,
                                "parent_id": 2,
                                "depend_value": True,
                                "state": 2,
                                "frame_name": " Add Options ",
                                "type": "multi-select",
                                "content": ["Data Type", "Empty Fields", "Format", "Uniqueness", "Range"],
                                "return": None
                            },
                            {
                                "id": 4,
                                "parent_id": 1,
                                "depend_value": True,
                                "state": 2,
                                "frame_name": "Add Columns",
                                "type": "multi-select",
                                "content": "columns",
                                "layout": "horizontal",
                                "return": ""
                            }

        ]



    
    def start_app(self, df):
        self.validate_types = self.input_items[2]["return"]
        self.columns = self.input_items[3]["return"]

        new_df = self.process(df)

        return new_df
        

    def process(self, df):

        if not self.columns:
            self.columns = df.columns
        if not self.validate_types:
            self.validate_types = self.input_items[2]["content"]

        results = []

        for col in self.columns:
            if col not in df.columns:
                continue

            col_result = {
                "Column": col
            }

            series = df[col]

            # Data Type Validation
            if "Data Type" in self.validate_types:
                col_result["Data Type"] = str(series.dtype)

            # Empty Fields Validation
            if "Empty Fields" in self.validate_types:
                col_result["Empty Fields"] = int(series.isna().sum())

            # Format Validation
            if "Format" in self.validate_types:
                # Example: count non-string values for object columns
                if series.dtype == "object":
                    invalid_format = series[~series.fillna("").astype(str).str.strip().ne("")]
                    col_result["Format"] = f"{len(invalid_format)} potential issues"
                else:
                    col_result["Format"] = "N/A"

            # Uniqueness Validation
            if "Uniqueness" in self.validate_types:
                duplicate_count = int(series.duplicated().sum())
                col_result["Uniqueness"] = duplicate_count

            # Range Validation
            if "Range" in self.validate_types:
                if pd.api.types.is_numeric_dtype(series):
                    col_result["Range"] = f"{series.min()} - {series.max()}"
                else:
                    col_result["Range"] = "N/A"

            results.append(col_result)

        df = pd.DataFrame(results)

        return df