

class Transformer:

    def __init__(self):

        self.b_name = "Transform Data"
        self.title = "TRANSFORMER"

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