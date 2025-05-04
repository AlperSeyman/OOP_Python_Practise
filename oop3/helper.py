# When to use class method and when to use static method ? 

class Item:

    @staticmethod
    def check_integer(num):
        '''
        This should do something that has a relationship with
        the class, but not something that must be unique per instance
        '''

    @classmethod
    def instantiate_from_csv(cls):
        '''
        This should do something that has a relationship with
        the class, but usually, those are used to manipulate 
        different structures of data to instantiate objects, 
        like we have done with CSV.
        '''