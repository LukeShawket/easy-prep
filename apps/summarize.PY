import pandas as pd

class Seperater:

    def __init__(self):

        self.b_name = "Quick Summarize"
        self.title = " SUMMARIZE "

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



    
    def start_app(self, df):

        new_df = self.process(df)

        return new_df
        

    def process(self, df):
        if self.columns:
            new_df = df[self.columns]
        else:
            new_df = df

        result = pd.DataFrame(index=new_df.index)

        #  Do something with data frame result

        return result