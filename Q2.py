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
        return height

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
        return 1

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
            return 1
        else:
            return 0.5 
    
    def __str__(self):
        '''Method that returns a string of PutterHead'''
        return "Putter,{},{}".format(super().__str__(), self._style)



# #Q2(a)

class Shaft():
    def __init__(self, length:float,weight:int,material:str,flex:str):
        self._length = length
        self._weight = weight
        self._material = material
        self._flex = flex
        
    @property
    def length(self):
        return self._length
    
    @property
    def weight(self):
        return self._weight

    @property
    def material(self):
        return self._material

    @property
    def flex(self):
        if self._flex == "Senior":
            return "SR"
        elif self._flex == "Regular":
            return "R"
        elif self._flex == "Stiff":
            return "S"
        elif self._flex == "Extra-Stiff":
            return "XS"
        else:
            return self._flex

    def __str__(self):
        return "{}, {}, {}, {} ".format(self._length, self._weight, self._material, self._flex)
    

class Grip():
    def __init__(self, diameter: float, weight: int, material: str):
        self._diameter = diameter
        self._weight = weight
        self._material = material

    @property
    def weight(self):
        return self._weight
    
    @property
    def diameter(self):
        return self._diameter

    def __str__(self):
        return "{},{},{}".format(self._diameter, self._weight,self._material)

# #Q2(b)   
class EquipmentRuleException(Exception):
    """ EquipmentRuleException, a subclass of the Exception class"""

# #Q2(c)
class Club():
    def __init__(self, label: str, head: ClubHead, shaft: Shaft, grip: Grip):
        self._label = label.upper()
        self._head = head
        self._shaft = shaft
        self._grip = grip

# Weight of head must be more than the combined weight of the shaft and grip.
# Otherwise, raise EquipmentRuleException with appropriate message.
# Assembled club length must be within 18 to 48 inches. Otherwise, raise
# EquipmentRuleException with appropriate message
    @property
    def loft(self):
        '''Loft of the club refers to the loft of the clubhead'''
        return float(self._head.loft)

    @property
    def label(self):
        '''labelling or numbering in uppercase, to help golfers identify the club'''
        return self._label

    @property
    def weight(self):
        '''Weight of the club is the total weight of clubhead, shaft and grip'''
        totalWeight = self._head.weight + self._shaft.weight + self._grip.weight
        return totalWeight

    @property
    def flex(self):
        '''Flex of the club refers to the shafts flex.'''
        return self._shaft.flex

    def length(self):
        '''Length of the club is the length of the shaft and the height of the clubhead'''
        return self._shaft.length + self._head.getHeight()

    
    def changeGrip(self, newGrip: Grip):
        '''The changeGrip method replaces the instance variable _grip with the given parameter Grip object, 
        provided that the weight of head must be more than the combined weight of the shaft and this new grip. 
        Otherwise,raise EquipmentRuleException with appropriate message.'''
        if self._head.weight > self._shaft.weight+ self._grip.weight: 
            self._grip = newGrip
        else:
            raise EquipmentRuleException("Head weight heavier than Shaft weight and Grip weight")
    
    def getDetails(self):
        return "Club: {} Loft: {} Length: {} Flex: {} Weight: {}".format(self._label, self.loft ,self.length(), self.flex , self.weight )

    def __str__(self):
        return f"{self._label},{self._head}, {self._shaft},{self._grip}"

#2(d)
def main():
#2d(i)
    driver = Club("Driver", WoodHead(10.5,203,450),Shaft(45,68,"Graphite","S"),Grip(0.6,62,"Rubber"))
    eightIron = Club("8-iron", IronHead(34.5,268,"Cast"),Shaft(35.5,109,"Steel","R"),Grip(0.6,62,"Rubber"))
    sunset = Club("Sunset", PutterHead(3,380,"Mullet"),Shaft(33,120,"Steel","S"),Grip(0.6,62,"Rubber"))
    fiveWood = Club("5-wood", WoodHead(17.5,150,280),Shaft(42.5,89,"Steel","S"),Grip(0.6,62,"Rubber"))
    # print(driver)
    # print(eightIron)
    # print(sunset)
    # print(fiveWood)

    totalClubWeight = driver.weight + eightIron.weight + sunset.weight + fiveWood.weight
    print(f'{totalClubWeight} grams')

#2(dii)
    driver.changeGrip(Grip(0.58,75,"Leather"))
    eightIron.changeGrip(Grip(0.58,75,"Leather"))
    sunset.changeGrip(Grip(0.58,75,"Leather"))
    fiveWood.changeGrip(Grip(0.58,75,"Leather"))

    print(driver)
    print(eightIron)
    print(sunset)
    print(fiveWood)

main()