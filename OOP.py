class Building:
    objects = []
    def __init__(self, city, street, build_id, floors, square, color, cafes):
        self.__city = city
        self.__street = street
        self.__build_id = build_id
        self.__floors = floors
        self.__square = square
        self.__color = color
        self.__cafes = cafes
        self.objects.append(self)

    def get_build_id(self):
        return self.__build_id

    def set_cafe(self, cafe):
        self.__cafes.append(cafe)

    @property
    def cafes(self):
        for cafe in self.__cafes:
            print(cafe.get_name)
    
class Cafe:

    def __init__(self, name, build_id, floor):
        self.__name = name
        self.__build_id = build_id
        self.__floor = floor

        self.add_cafe()

    def add_cafe(self):
        for building in Building.objects:
            if self.__build_id == building.get_build_id():
                building.set_cafe(self)

    @property
    def get_name(self):
        return self.__name

building1 = Building(1, 1, 1, 1, 1, 1, [])
building2 = Building(1, 1, 2, 1, 1, 1, [])
cafe1 = Cafe('Paradise', 1, 5)
cafe2 = Cafe('Edem', 2, 3)
cafe3 = Cafe('Valhalla', 2, 5)
building1.cafes
building2.cafes