

class Validater:

    def __init__(self):

        self.b_name = "Data Validation"
        self.title = "Validation"

        self.input_items = [
                            {
                                "name": "Select A Column",
                                "type": "sst", # single select tab
                                "content": "columns",
                                "return": ""
                            },
                            {
                                "name": "Select Columns",
                                "type": "mst", # single select tab
                                "content": "columns",
                                "return": ""
                            }
        ]