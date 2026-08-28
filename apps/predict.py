

class Predicter:

    def __init__(self):

        self.b_name = "Predictive Analysis"
        self.title = "PREDICTIVE MODEL"

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