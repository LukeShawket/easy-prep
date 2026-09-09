

class Predicter:

    def __init__(self):

        self.b_name = "Predictive Analysis"
        self.title = "PREDICTIVE MODEL"

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

        self.next_input_items = []

        self.delimiter = None



    
    def on_start(self):
        self.delimiter = self.input_items[0]["return"]
        print(self.delimiter)

    def process(self):
        pass