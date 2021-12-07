class Value:

    def __init__ (self, data):
        self.__tarif1, self.__tarif2, self.__period, self.__room = data

    def get_all (self):
        return self.__tarif1, self.__tarif2, self.__period, self.__room

    def encode (self):

        tarif1 = Value.formate(int(self.__tarif1), 3)
        tarif2 = Value.formate(int(self.__tarif2), 3)
        period = Value.formate(int(self.__period), 1)
        room = Value.formate(int(self.__room), 2)

        out = tarif1 + tarif2 + period + room

        return out

    def decode (data):

        tarif1 = Value.deformate(data[0:3], 3)
        tarif2 = Value.deformate(data[3:6], 3)
        period = Value.deformate(data[6], 1)
        room = Value.deformate(data[7::], 2)

        return tarif1, tarif2, period, room

    def formate (data, bits):

        out = []

        if bits == 1:
            out.append(data)
            out = bytes(out)
            return out

        for i in range(bits-1, -1, -1):
            out.append((data>>(8*i)) & 255)

        out = bytes(out)
        
        return out

    def deformate (data, bits):

        if bits == 1:
            return data

        out = 0
        c = 0

        for i in range(bits-1, -1, -1):

            out = out | (data[c]<<(i*8))
            c += 1

        return out



data = '851 31 8 1943'
value1 = Value(list(map(int, data.split())))
print(value1.get_all())
print(Value.decode(value1.encode()))