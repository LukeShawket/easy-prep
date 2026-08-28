

class Slicer:

    def __init__(self):

        self.b_name = "Slice Data"
        self.title = "DATA SLICER"

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