# Base class
class Smartphone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Polymorphic method
    def launch(self):
        print(f"{self.brand} {self.model} ({self.year}) is launching...")

# Subclass for Samsung
class Samsung(Smartphone):
    def launch(self):
        print(f"{self.brand} {self.model} boots up with One UI.")

# Subclass for Apple
class Apple(Smartphone):
    def launch(self):
        print(f"{self.brand} {self.model} starts with iOS.")

# Subclass for Google
class Google(Smartphone):
    def launch(self):
        print(f"{self.brand} {self.model} powers on with Android.")

# Demonstrating polymorphism
phones = [
    Samsung("Samsung", "Galaxy S25 Ultra", 2025),
    Apple("Apple", "iPhone 16 Pro Max", 2025),
    Google("Google", "Pixel 10", 2025)
]

for phone in phones:
    phone.launch()   # Same method name, different behavior, thus polymorphism
