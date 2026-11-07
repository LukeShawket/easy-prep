from duckdb import DuckDBPyConnection
from pandas import DataFrame

class QueryTool:

    def __init__(self):

        self.b_name = "Query Tool"
        self.title = "QUERY TOOL"
        self.default_path = "C:/Users/fxiaowuk/Downloads"
        self.db: DuckDBPyConnection = None
                
        self.input_items = [
                            {
                                "id": 1,
                                "state": 1,
                                "outer_frame_name": "Query Tool",
                                "type": "entry_box",
                                "default_text": "SELECT *\nFROM {table}\nLIMIT 10",
                                "return": None
                            }

        ]



    
    def start_app(self, df=None, db=None):
        self.db = db

        new_df = self.process()

        return new_df
        

    def process(self):

        sql = self.input_items[0]["return"]

        result = None

        try:
            result = self.db.execute(sql).df()
            return result

        except Exception as e:
            print(e)
            return DataFrame({
                "Error": [str(e)]
            })