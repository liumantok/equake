from cli.equake_io import EquakeIO
from logic.equake_logic import EquakeLogic

class EquakeMode:
    
    def startup(self, io):
        io.welcome_message()
        io.present_options()
    
    def mode(self):
        io = EquakeIO()
        logic = EquakeLogic()
        self.startup(io)
        while True:
            timeframe = io.inquire_timeframe()
            group = io.inquire_group()

            io.display_earthquakes(logic.request_data(timeframe, group))