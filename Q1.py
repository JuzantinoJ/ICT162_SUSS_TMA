#Demonstrate your understanding of how class hierarchy and association are 
#used to organize information, and then construct the 
#class hierarchy and association according to specification.

class ClubHead:
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
    def getHeight(self):
        """ Returns height of the clubhead"""
        pass

    #str method
    def __str__(self):
        return "{},{}".format(self._loft, self._weight)

# testHead = ClubHead(9.0,200)
# print(testHead.getHeight())


class WoodHead(ClubHead):
    def __init__(self,loft:float, weight:int, size:int):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._size = size
       
    #get height method for woodhead
    def getHeight(self):
        """find height for WoodHead"""
        height = self._size/400
        return height

    def __str__(self):
        '''Method that returns a string of WoodHead'''
        return "Wood,{},{},{}".format(self._loft, self._weight,self._size)


class IronHead(ClubHead):
    def __init__(self, loft:float, weight:int, material:str):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._material = material

    #get height method for Ironhead
    def getHeight(self):
        """find height for IronHead"""
        height = 1
        return height

    def __str__(self):
        '''Method that returns a string of IronHead'''
        return "Iron,{},{},{}".format(self._loft,self._weight,self._material)

class PutterHead(ClubHead):
    def __init__(self, loft:float, weight:int, style:str):
        """ constructor that execute when an object is created """
        super().__init__(loft,weight)
        self._style = style

    def getHeight(self):
        """find height for PutterHead"""
        if self._style == "Blade":
            return 1
        else:
            return 0.5
    
    def __str__(self):
        '''Method that returns a string of PutterHead'''
        return "Putter,{},{},{}".format(self._loft, self._weight, self._style)

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