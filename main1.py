# assignment1: design your own class
class smartphone:
    def __init__(self,brand,model,year): #constructor initialized
        self.brand = brand #attributes
        self.model = model
        self.year = year
#method
    def launch(self):
        print(f"{self.brand} {self.year} {self.model} is currently the best phone in the market.")

#create object
samsung = smartphone("Samsung","Galaxy S25 Ultra","2025")
#calling the method
samsung.launch()