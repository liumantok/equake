import questionary

class EquakeIO:

    def welcome_message(self):
        print("Welcome to equake!")

    def present_options(self):
        print("Choose your paraneters. ")
    
    def inquire_timeframe(self):
        timeframe = questionary.select(
            "Choose a timeframe. ",
            choices=[
                "Past hour",
                "Past day",
                "Past 7 days",
                "Past 30 days"
            ]).ask()
        return timeframe

    def inquire_group(self):
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
    
    def display_earthquakes(self, eqs):
        for eq in eqs:
            print(eq)