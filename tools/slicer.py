

class Slicer:

    def __init__(self):

        self.b_name = "Slice Data"
        self.title = "DATA SLICER"

        self.input_items = [
                            ("Status", "combo", ["OEM", "Vendor", "Both"]),
                            ("Description", "entry"),
                            ("Needs Review", "check")
                        ]