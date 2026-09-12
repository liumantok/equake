import questionary

class equakeIO:

    def __init__(self):
        pass

    def welcomeMessage(self):
        print("Welcome to equake!")

    def presentOptions(self):
        print("input parameters ")
    
    def inquireTimeframe(self):
        timeframe = questionary.select(
            "Choose a timeframe. ",
            choices=[
                "Past hour",
                "Past day",
                "Past 7 days",
                "Past 30 days"
            ]).ask()
        return timeframe

    def inquireGroup(self):
        group = questionary.select(
            "Choose which group of earthquakes to show. Alternatively, you may also choose to see all. ",
            choices=[
                "Significant",
                "M4.5+",
                "M2.5+",
                "M1.0+",
                "All"
            ]).ask()
        return group
    
    def defaultMessage(self, msg):
        print(msg)