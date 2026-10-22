import pandas as pd

class Seperater:

    def __init__(self):

        self.b_name = "Quick Summarize"
        self.title = " SUMMARIZE "
        self.default_path = "C:/Users/fxiaowuk/Downloads"
                
        self.input_items = [
                            {
                                "id": 1,
                                "parent_id": None,
                                "depend_value": None,
                                "state": 1,
                                "is_child": False,
                                "name": "Select a Delimiter",
                                "type": "combo",
                                "content": [",", "|", "\t", ";",":", "^", "%", "@"],
                                "return": ""
                            },
                            {
                                "id": 2,
                                "parent_id": None,
                                "depend_value": None,
                                "state": 1,
                                "is_child": False,
                                "name": "Add Columns",
                                "type": "check",
                                "notify_true": "Selected Columns",
                                "notify_false": "All Columns",
                                "content": "continue",
                                "return": False
                            },
                            {
                                "id": 3,
                                "parent_id": 2,
                                "depend_value": True,
                                "state": 2,
                                "is_child": True,
                                "name": "Add Columns",
                                "type": "multi-select",
                                "content": "columns",
                                "return": ""
                            }

        ]

        self.delimiter = None
        self.columns = None



    
    def start_app(self, df):
        self.delimiter = self.input_items[0]["return"]
        self.columns = self.input_items[2]["return"]

        new_df = self.process(df)

        return new_df
        

    def process(self, df):

        return df