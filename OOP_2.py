class Building:

    def __init__(self, city, street, build_id, floors, square, color, cafes):
        self.__city = city
        self.__street = street
        self.__build_id = build_id
        self.__floors = floors
        self.__square = square
        self.__color = color
        self.__cafes = cafes

    @property
    def cafes(self):
        for cafe in self.__cafes:
            print(cafe.get_name)

    def cafes_set(self, cafe):
        self.__cafes.append(cafe)
        return
    
class Cafe:

    def __init__(self, name, build_id, floor):
        self.__name = name
        self.__build_id = build_id
        self.__floor = floor

    @property
    def get_name(self):
        return self.__name


cafe1 = Cafe('Paradise', 1, 1)
cafe2 = Cafe('Edem', 1, 2)
cafe3 = Cafe('Valhalla', 1, 4)
cafe4 = Cafe('Helheim', 1, 5)
building1 = Building(1, 1, 1, 1, 1, 1, [cafe1, cafe2, cafe3])
building1.cafes
building1.cafes_set(cafe4)
building1.cafes