from item import Item

# Inheritance
class Phone(Item):

    def __init__(self, name, price, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones: {broken_phones} is not greater than or equal to zero"
        
        # Assign to self object
        self.broken_phones = broken_phones


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    

