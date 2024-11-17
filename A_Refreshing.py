# Create a class for drink: 
class Drink:
    _valid_bases = {"water", "sbrite", "pokecola", "Mr. Salt", "hill fog", "leaf wine"} # That stores a 'base' 
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}     # And the 'flavors' that haver been added 

    # Initializer for GETTERS:
    def __init__(self):
        self._base = None
        self._flavors = set()   # -> 'set()' helps avoid duplicates for flavors

    # GETTERS to grab the different aspects for the drink:
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        return list(self._flavors) # returns a 'list' for usr access
    
    def get_num_flavors(self):      # Keeps a tracker for number of flavors added 
        return len(self._flavors)
    
    # set the base:
    def set_base(self, base):
        if base in self._valid_bases: # Validates the base
            self._base = base
        else:
            raise ValueError(f"pick a proper base from {self._valid_bases}.")
        
    def add_flavor(self, flavor):       
        if flavor in self._valid_flavors:
            self._flavors.add(flavor)       # Checks for a valid flavor, then adds to list (helps with duplication)
        else: 
            raise ValueError(f"pick a proper flavor from {self._valid_flavors}.")

    # set the falvors:    
    def set_flavors(self, flavors):
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)

# Create an order class to contain our order items
class Order: 
    # Initialize the class
    def __init__(self):
        self._items = []    # Create a list as a starting point 

    # GETTERS for the items and total of items
    def get_items(self):
        return self._items
    
    def get_total(self):
        return len(self._items)
    
    def get_receipt(self):
        receipt = "Your order receipt:\n"
        for i, drink in enumerate(self._items):     # compares the list and counts the number of items ordered
            base = drink.get_base()
            flavors = ", ".join(drink.get_flavors())
            receipt += f"{i + 1}: base - {base}, Flavors - {flavors}\n"
        return receipt
    
    # Add drink items to list:
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError("You can only add drinks to this order.")
        
    # Remove drink items to list:
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid, cannot remove")
        