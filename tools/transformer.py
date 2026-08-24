

class Transformer:

    def __init__(self):

        self.b_name = "Transform Data"
        self.title = "TRANSFORMER"

        self.input_items = [
                            ("Status", "combo", ["OEM", "Vendor", "Both"]),
                            ("Description", "entry"),
                            ("Needs Review", "check")
                        ]