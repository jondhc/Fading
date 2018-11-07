import math

def correction_factor():
    fc = int(input("Input the carrier frequency (Mhz): "))
    hr = int(input("Input the height of received antenna (m): "))
    city_size = int(input("Is the city small(1), medium(2) or big(3)? Write the number: "))
    if city_size == 1 or city_size == 2:
        result = (((1.1*math.log10(fc))-0.7) * hr) - ((1.56*log10(fc) - 0.8))
    elif city_size == 3:
        if fc <= 300:
            result = (8.29*(math.pow((math.log10(1.54*hr)), 2))) - 1.1
        elif fc >= 300:
            result = (3.2*(math.pow((math.log10(11.75*hr)), 2))) - 4.97
    print("A(HR): ")
    print(result)
    return result

def path_loss(ahr):
    area_kind = int(input("Is the area urban(1), suburban(2) or open(3)? Write the number:"))
    fc = int(input("Input the carrier frequency (Mhz): "))
    hr = int(input("Input the height of received antenna (m): "))
    ht = int(input("Input the height of transmitting antenna: "))
    d = int(input("Input the propagation distance: "))
    result = 0
    if area_kind == 1:
        result = 69.55 + (26.16*math.log10(fc)) - (13.82*math.log10(ht)) - ahr + ((44.9-(6.55*math.log10(ht)))*math.log10(d))
        return result
    if area_kind == 2:
        ldb_urban = 69.55 + (26.16*math.log10(fc)) - (13.82*math.log10(ht)) - ahr + ((44.9-(6.55*math.log10(ht)))*math.log10(d))
        result = ldb_urban - (2 * math.sqrt(math.log10(fc/28))) - 5.4
        return result
    if area_kind == 3:
        ldb_urban = 69.55 + (26.16 * math.log10(fc)) - (13.82 * math.log10(ht)) - ahr + (
                    (44.9 - (6.55 * math.log10(ht))) * math.log10(d))
        result = ldb_urban - (4.78 * math.sqrt(math.log10(fc))) - (418.733 * math.log10(fc)) - 40.98
        return result
    else:
        return result


print(path_loss(correction_factor()))
print("dB of path loss")





