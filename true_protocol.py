def send (data):

    tarif1, tarif2, period, room = data.split(sep=' ')
    tarif1 = encode(int(tarif1), 3)
    tarif2 = encode(int(tarif2), 3)
    period = encode(int(period), 1)
    room = encode(int(room), 2)

    out = tarif1 + tarif2 + period + room

    return out

def get (data):

    tarif1 = decode(data[0:3], 3)
    tarif2 = decode(data[3:6], 3)
    period = decode(data[6], 1)
    room = decode(data[7::], 2)

    return tarif1, tarif2, period, room

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

def decode (data, bits):

    if bits == 1:
        return data

    out = 0
    c = 0

    for i in range(bits-1, -1, -1):

        out = out | (data[c]<<(i*8))
        c += 1

    return out

data = '851 31 8 1943'

print(get(send(data)))