from equakeIO import equakeIO
from equakeLogic import equakeLogic

class equakeMode():
    
    def __init__(self):
        pass
    
    def startup(self):
        logic = equakeLogic()
        io = equakeIO()
        io.welcomeMessage()
        io.presentOptions()
    
    def mode(self):
        self.startup()
        while True:
            logic = equakeLogic()
            io = equakeIO()
                    
            timeframe = io.inquireTimeframe()
            group = io.inquireGroup()

            io.defaultMessage(logic.requestData(timeframe, group))
        
