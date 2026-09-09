import pandas as pd

class Seperater:

    def __init__(self):

        self.b_name = "Split by Delimiter"
        self.title = " DELIMITER "

        self.input_items = [
                            {
                                "id": 1,
                                "parent_id": None,
                                "depend_value": None,
                                "state": 1,
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
                                "name": "Add Columns",
                                "type": "check",
                                "content": "continue",
                                "return": False
                            },
                            {
                                "id": 3,
                                "parent_id": 2,
                                "depend_value": True,
                                "state": 2,
                                "name": "Add Columns",
                                "type": "multi-select",
                                "content": "columns",
                                "result": ""
                            }

        ]

        # Must include this
        self.df = None

        self.delimiter = None
        self.columns = None



    
    def start_app(self):
        self.delimiter = self.input_items[0]["return"]
        self.columns = self.input_items[2]["return"]

        new_df = self.process()

        return new_df
        

    def process(self):
        new_df = self.df[self.columns]
        result = pd.DataFrame(index=new_df.index)

        for i, col in enumerate(new_df.columns):

            result[col] = new_df[col]

            if i < len(new_df.columns) - 1:

                result[f"delim_{i}"] = self.delimiter

        return result