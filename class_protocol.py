class Value:

    def __init__ (self, tarif1, tarif2, period, room):
        self.__tarif1 = tarif1
        self.__tarif2 = tarif2
        self.__period = period
        self.__room = room

    def encode (data, bits):

        out = []

        if bits == 1:
            out.append(data)
            out = bytes(out)
            return out

        for i in range(bits-1, -1, -1):
            out.append((data>>(8*i)) & 255)

        out = bytes(out)
        
        return out

    def send (self):

        tarif1 = self.encode(int(self.tarif1), 3)
        tarif2 = self.encode(int(self.tarif2), 3)
        period = self.encode(int(self.period), 1)
        room = self.encode(int(self.room), 2)

        out = tarif1 + tarif2 + period + room

        return out