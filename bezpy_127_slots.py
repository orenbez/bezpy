# slots tell Python not to use a Dict, and only allocate space for a fixed set of attributes
# * faster attribute access.
# * space savings in memory.
# we use __dict__ for its flexibility after creating the object where you can add new attributes after intialization
# However, __slots__ will fix the attributes when you create the class. It will not possible to add new attributes later
# Note that __slots__ will prevent multiple inheritance if both parent classes use __slots__


# ======================================================================================================================

# Without Slots  (uses __dict__)
class MyClass1:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# With Slots
class MyClass2:
    __slots__ = ['name', 'id']
    def __init__(self, name, identifier):
        self.name = name
        self.id = id

x = MyClass1('Fred', 7) 
y = MyClass2('John', 8)   # does not have __dict__ property,  attributes are fixed
 
x.__dict__   # {'name': 'Fred', 'id': 7}
y.__slots__  #  ['name', 'id']



# ======================================================================================================================
# Using __slots__ with dataclasses, introduced in python 3.10 ...
# ======================================================================================================================

import timeit  
from dataclasses import dataclass
from functools import partial

@dataclass(slots=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    
    def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand
  
@dataclass(slots=True)
class InventoryItemSlot:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
      
      
inventory_item = InventoryItem(name="John", unit_price=100, quantity_on_hand=5)
inventory_item_slot = InventoryItemSlot(name="John", unit_price=100, quantity_on_hand=5)

#I have used  timeit to calculate the execution time. It return value is seconds as a float.
execution_time = min(timeit.repeat(partial(inventory_item.total_cost), number=5000000))
execution_time_with_slots = min(timeit.repeat(partial(inventory_item_slot.total_cost), number=500000))

print(f"Execution time with out slots: {execution_time}")
print(f"Execution time with out slots: {execution_time_with_slots}")
print(f"% Performance improvement: {(execution_time - execution_time_with_slots) / execution_time:.2%}")
