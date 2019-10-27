from abc import *

class PId(ABC):
    @property
    @abstractmethod
    def ID(self):
        pass
    
class Priced(ABC):
    @property
    @abstractmethod
    def price(self):
        pass
    
class Goods(PId, Priced):
    def __init__(self, Id, price):
        self._id = Id
        self._price = price
        
    @property
    def ID(self):
        return self._id
        
    @property
    def price(self):
        return self._price
        
def show(inf):
    print(f'id = {inf.ID}, price = {inf.price}')
    
bread = Goods(1, 5)
show(bread)
