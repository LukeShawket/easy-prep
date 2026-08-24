

class PartMaker:

    def __init__(self):

        self.b_name = "Make Part Entry"
        self.title = "PART ENTRY"

        self.input_items = [
                            ("Status", "combo", ["OEM", "Vendor", "Both"]),
                            ("Description", "entry"),
                            ("Needs Review", "check")
                        ]