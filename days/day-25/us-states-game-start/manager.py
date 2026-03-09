import pandas
from state import State

DATA_PATH = "50_states.csv"

class Manager:
    def __init__(self):
        self.data = pandas.read_csv(DATA_PATH)

    def get_states_pos(self,name:str):
        state_row = self.data[self.data["state"] == name]
        pos:tuple[int,int] = (state_row.iloc[0,1],state_row.iloc[0,2])
        return pos

    def is_valid_name(self,name:str):
        target_data:pandas.DataFrame = self.data[self.data["state"] == name]
        if target_data.empty:
            return False
        else:
            return True

    def make_state(self,name:str,pos:tuple[int,int]):
        State(name,pos)
