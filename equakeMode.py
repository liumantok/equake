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
                    
            parameter = io.requestInput()
                    
            #if not logic.analyzeInput(parameter): not for now
            #    print("Nope. ")

            io.defaultMessage(logic.requestData())    
        
