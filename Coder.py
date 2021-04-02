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
        return addParityCode(listofbits)
    listofbits.append(bits[temp:len(bits)])
    return addParityCode(listofbits)

def addParityCode(listofbits): #kod parzystosci
    # print("POCZATEK dodawania kodu parzystosci")
    # print(listofbits)
    countonebit = 0
    for list in listofbits:
        countonebit = 0
        for numbers in list:
            if numbers == 1:
                countonebit += 1
        if countonebit % 2 == 0:
            list.append(0)
        else:
            list.append(1)
    # print("KONIEC dodawania kodu parzystosci")
    # print(listofbits)
    return listofbits  
            