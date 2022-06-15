import pandas as pd
try:
    import importlib.resources as ir
except ImportError:
    import importlib_resources as ir
from . import assets

class PlaystationGame:
    name = ""
    id = ""

    def PlaystationGame(self, name, id):
        self.name = name
        self.id = id
    

    def __str__(self):
        return self.name + " " + self.id


    def get_name(self):
        return self.name


    def get_id(self):
        return self.id



"""
Gets a Playstation Game with the given ID
"""
def find_by_id(game_id, platform = "") -> PlaystationGame:
    id_type = game_id[0:4]
    id_number = game_id[4:]
    file_loc = ir.open_text(assets, "PS3_GAMES.tsv")
    print(file_loc)
    df = pd.read_table(file_loc)
    print(df)

