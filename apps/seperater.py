

class Seperater:

    def __init__(self):

        self.b_name = "Split by Delimiter"
        self.title = "SEPERATE VALUE"

        self.input_items = [
                            {
                                "name": "Slicer",
                                "type": "combo",
                                "content": [",", "|", "\t", ";",":", "^", "%", "@"],
                                "return": ""
                            },
                            {
                                "name": "Add Columns",
                                "type": "check",
                                "content": "continue",
                                "return": ""
                            }
        ]