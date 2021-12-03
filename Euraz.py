def send (data):
    tarif1, tarif2, period, room = data.split(sep=' ')

    if validate(tarif1, tarif2, period, room):

        tarif1 = bin(int(tarif1)).replace('0b', '')
        tarif2 = bin(int(tarif2)).replace('0b', '')
        period = bin(int(period)).replace('0b', '')
        room = bin(int(room)).replace('0b', '')
        print(int(tarif1, 2), int(tarif2, 2), int(period, 2), int(room, 2))

        tarif1 = '0'*(24-len(tarif1)) + tarif1
        tarif2 = '0'*(24-len(tarif2)) + tarif2
        period = '0'*(8-len(period)) + period
        room = '0'*(16-len(room)) + room

        packet = int(room[::-1] + period[::-1] + tarif2[::-1] + tarif1[::-1], 2)
        print(bin(packet))

        return packet
    
    else:

        raise ValueError

def get(data):
    
    tarif_mask = 0b111111111111111111111111
    period_mask = 0b11111111
    room_mask = 0b1111111111111111
    
    tarif1 = formate(data, tarif_mask, 24)

    data = data >> 24

    tarif2 = formate(data, tarif_mask, 24)

    data = data >> 24

    period = formate(data, period_mask, 8)

    data = data >> 8

    room = formate(data, room_mask, 16)

    return tarif1, tarif2, period, room

def validate (tarif1, tarif2, period, room):

    if (int(tarif1)<2**20 and int(tarif1)>=0 and int(tarif2)<2**20 and int(tarif2)>=0 
        and int(period)<=12 and int(period)>=1 and int(room)>=1 and int(room)<2**12):

        return True
    
    return False

def formate (data, mask, shift):

    value = data & mask
    value = (1 << shift) | value
    value = value >> 1
    value = bin(value).replace('0b1', '')[::-1]
    value = int(value, 2)

    return value

data = '851 3 1 1943'
print(get(send(data)))