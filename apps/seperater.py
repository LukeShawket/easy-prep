import pandas as pd

class Seperater:

    def __init__(self):

        self.b_name = "Split by Delimiter"
        self.title = " DELIMITER "

        self.input_items = [
                            {
                                "id": 1,
                                "state": 1,
                                "name": "Select a Delimiter",
                                "type": "combo",
                                "content": [",", "|", "\t", ";",":", "^", "%", "@"],
                                "return": ""
                            },
                            {
                                "id": 2,
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
                                "type": "mst",
                                "content": "columns",
                                "result": ""
                            }

        ]

        self.next_input_items = []

        self.delimiter = None



    
    def on_start(self):
        self.delimiter = self.input_items[0]["return"]

    def process(self):
        pass