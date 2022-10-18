#Demonstrate your understanding of how class hierarchy and association are 
#used to organize information, and then construct the 
#class hierarchy and association according to specification.

from abc import ABC, abstractmethod


class ClubHead(ABC):
    def __init__(self, loft: float, weight: int):
        """ constructor that execute when an object is created """
        self._loft = loft
        self._weight = weight

    #getter methods for loft
    @property
    def loft(self):
        return self._loft

    #getter method for weight
    @property
    def weight(self):
        return self._weight

    #get height method
    @abstractmethod
    def getHeight(self):
        """ Returns height of the clubhead"""
        pass

    #str method
    def __str__(self):
        return "{},{}".format(self._loft, self._weight)


#Q1(b)
class WoodHead(ClubHead):
    def __init__(self,loft:float, weight:int, size:int):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._size = size
       
    #get height method for woodhead
    def getHeight(self):
        """find height for WoodHead"""
        height = self._size/400
        return f'{height:.1f} inch'

    def __str__(self):
        '''Method that returns a string of WoodHead'''
        return "Wood,{},{}".format(super().__str__(),self._size)


class IronHead(ClubHead):
    def __init__(self, loft:float, weight:int, material:str):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._material = material

    #get height method for Ironhead
    def getHeight(self):
        """find height for IronHead"""
        height = 1
        return f'{height} inch'

    def __str__(self):
        '''Method that returns a string of IronHead'''
        return "Iron,{},{}".format(super().__str__(),self._material)


class PutterHead(ClubHead):
    def __init__(self, loft:float, weight:int, style:str):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._style = style

    def getHeight(self):
        """find height for PutterHead"""
        if self._style == "Blade":
            height = 1
            return f'{height} inch'
        else:
            height = 0.5
            return 0.5 + 'inch'
    
    def __str__(self):
        '''Method that returns a string of PutterHead'''
        return "Putter,{},{}".format(super().__str__(), self._style)

#Q1(c)
def main():
    putter = PutterHead(3.5,365,'Blade')
    iron = IronHead(37.5,285, 'Forged')
    wood = WoodHead(9.5,206,450)
    print(putter)
    print(putter.getHeight())
    print(iron)
    print(iron.getHeight())
    print(wood)
    print(wood.getHeight())
main()