

class CustomMaker:

    def __init__(self):

        self.b_name = "Make Custom Entry"
        self.title = "CUSTOM ENTRY"

        self.input_items = [
                            ("Slicer", "combo", [",", "|", "\t", ";",":", "^", "%", "@"]),
                            ("Column Count", "entry"),
                            ("Add Columns", "entry")
                        ]