# dopisac dodawanie na koncu bity parzystosci 

def coderBit(bits, n):
    listofbits = []
    counter = 0
    temp = 0
    for i in bits:
        counter += 1
        if counter % n == 0:
            listofbits.append(bits[counter-10:counter])
            temp = counter
    if temp == len(bits):
        return listofbits
    listofbits.append(bits[temp:len(bits)])
    return listofbits
            