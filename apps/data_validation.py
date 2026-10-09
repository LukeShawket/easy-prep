

class Validater:

    def __init__(self):

        self.b_name = "Data Validation"
        self.title = "Validation"
        self.default_path = "C:/Users/fxiaowuk/Downloads"
        
        self.input_items = [
                            {
                                "id": 1,
                                "parent_id": None,
                                "depend_value": None,
                                "state": 1,
                                "is_child": False,
                                "name": "Add Columns",
                                "type": "check",
                                "notify_true": "Select Columns",
                                "notify_false": "All Columns",
                                "content": "continue",
                                "return": ""
                            },
                            {
                                "id": 2,
                                "parent_id": None,
                                "depend_value": None,
                                "state": 1,
                                "is_child": False,
                                "name": "Add Validation",
                                "type": "check",
                                "notify_true": "Select Validation",
                                "notify_false": "All Validation",
                                "content": "continue",
                                "return": False
                            },
                            {
                                "id": 3,
                                "parent_id": 2,
                                "depend_value": True,
                                "state": 2,
                                "is_child": True,
                                "frame_name": " Add Options ",
                                "type": "multi-select",
                                "content": ["Data Type", "Empty Fields", "Format", "Uniqueness", "Range", "Custom"],
                                "return": ""
                            },
                            {
                                "id": 4,
                                "parent_id": 1,
                                "depend_value": True,
                                "state": 2,
                                "is_child": True,
                                "frame_name": "Add Columns",
                                "type": "multi-select",
                                "content": "columns",
                                "layout": "horizontal",
                                "return": ""
                            }

        ]



    
    def start_app(self, df):
        self.delimiter = self.input_items[0]["return"]
        self.columns = self.input_items[2]["return"]

        new_df = self.process(df)

        return new_df
        

    def process(self, df):

        return df