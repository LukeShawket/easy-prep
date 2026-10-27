

class Predicter:

    def __init__(self):

        self.b_name = "Query Tool"
        self.title = "QUERY TOOL"
        self.default_path = "C:/Users/fxiaowuk/Downloads"
                
        self.input_items = [
                            {
                                "id": 1,
                                "state": 1,
                                "outer_frame_name": "Query Tool",
                                "type": "entry_box",
                                "default_text": "SELECT TOP 100 *\nFROM ~",
                                "return": None
                            }

        ]

        self.delimiter = None
        self.columns = None



    
    def start_app(self, df):
        self.delimiter = self.input_items[0]["return"]
        self.columns = self.input_items[2]["return"]

        new_df = self.process(df)

        return new_df
        

    def process(self, df):

        return df