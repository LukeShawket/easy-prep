

class PriceMaker:

    def __init__(self):

        self.b_name = "Make Price Entry"
        self.title = "PRICE ENTRY"

        self.input_items = [
                            ("Status", "combo", ["OEM", "Vendor", "Both"]),
                            ("Description", "entry"),
                            ("Needs Review", "check")
                        ]