

class Predicter:

    def __init__(self):

        self.b_name = "Predictive Analysis"
        self.title = "PREDICTIVE MODEL"

        self.input_items = [
                            ("Status", "combo", ["OEM", "Vendor", "Both"]),
                            ("Description", "entry"),
                            ("Needs Review", "check")
                        ]