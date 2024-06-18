# Try to recreate the class explained below:

# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

class Door:
    def __init__(self, is_opened: bool = True ) -> None:
        self.is_opened = is_opened
    

    def open_door(self):
        self.is_opened = True
        print('Door if opened')
        
    def close_door(self):
        self.is_opened = False
        print('Door is closed')

class BlockedDoor(Door):
    def open_door(self):
        raise Exception("a blocked door can't be open")
    
    def close_door(self):
        raise Exception("a blocked door can't be close")
    
door1 = Door()
door1.close_door()
print(door1.is_opened)

door2 = BlockedDoor()
door2.close_door()

def sum_of_numbers(lst):
    sum_num = 0
    for item in lst:
        try:
            sum_num += int(item)
        except (ValueError, TypeError):
            # If item is not a number, ignore it and continue
            pass
    return sum_num

# Example usage
my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
result = sum_of_numbers(my_list)
print(result)  # Output: 59



    
# We can create a class called BlockedDoor that inherits from the base class Door.

# We just override the parent class's functions of open_door() and close_door() 
# with our own BlockedDoor version of those functions,
#  which simply raises an Error that a blocked door cannot be opened or closed.