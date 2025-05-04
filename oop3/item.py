import csv

class Item:

    # Class attributes
    pay_rate = 0.8
    all_items = []

    def __init__(self, name:str, price:float, quantity=0):
        
        # Run validations to the received arguments
        assert price >= 0, f"Price: {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity: {quantity} is not greater than or equal to zero!"


        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all_items.append(self)
    
    @property
    # Property Decorator = Read-Only Attribute - Getter
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value
    

    @property
    def price(self):
        return self.__price
    

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value 

    def calculate_total_price(self):
        total_price = self.__price + self.quantity 
        return total_price
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items=list(reader)

        for item in items:
            cls(
                name= item['name'],
                price= float(item['price']),
                quantity= int(item['quantity'])
            )
            # Item can be used instead of 'cls'

    @staticmethod
    def check_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    

    # Abstraction 
    def __connect(self, smtp_server):
        pass
    
    # Abstraction
    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        """
    
    # Abstraction
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
