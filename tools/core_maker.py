

class CoreMaker:

    def __init__(self):

        self.b_name = "Core Maker"
        self.title = "CORE ENTRY"

        self.input_items = [
                    ("Type", "combo", ["OEM", "Vendor", "Both"]),
                    ("OEM Part #", "entry"),
                    ("Vendor Part #", "entry"),
                    ("OEM Suffix", "entry"),
                    ("Vendor Suffix", "entry"),
                    ("Part Description", "entry"),
                    ("Core Cost", "entry"),
                    ("Sku", "entry"),
                    ("AP Number", "entry"),
                    ("Update", "check")
                ]