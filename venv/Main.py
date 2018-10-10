import math

def correction_factor():
    fc = int(input("Input the carrier frequency (Mhz): "))
    hr = int(input("Input the height of received antenna (Km): "))
    city_size = int(input("Is the city small(1), medium(2) or big(3)? Write the number: "))
    if city_size == 1 or city_size == 2:
        result = (((1.1*math.log10(fc))-0.7) * hr) - ((1.56*log10(fc) - 0.8))
    elif city_size == 3:
        if fc <= 300:
            result = (8.29*(math.pow((math.log10(1.54*hr)), 2))) - 1.1
        elif fc >= 300:
            result = (3.2*(math.pow((math.log10(11.75*hr)), 2))) - 4.97
    return result

print(correction_factor())




