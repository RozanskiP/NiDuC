
def decodeBit(listofbits, n):
    lastElem = 0
    for list in listofbits:
        for numbers in list:
            lastElem += 1
    
    listOfErrorPackage = [] # 0 - dobrze, 1 - źle
    countonebit = 0

    temp = 0
    for list in listofbits:
        countonebit = 0
        counter = 0
        temp += 1
        for numbers in list:
            if numbers == 1:
                countonebit += 1
            counter += 1
            
            # print("counter: " + str(counter))
            if counter == n:
                # print("List: " + str(list[n]))
                # print("countonebit % 2: " + str(countonebit % 2))
                if list[n] == countonebit % 2:
                    listOfErrorPackage.append(0)
                    print("!")
                else:
                    listOfErrorPackage.append(1)
                    print("@")
                break
            if counter == lastElem and len(listofbits)-lastElem == temp*n:
                print("!!!!!")
    print("KONIEC")
    print(listOfErrorPackage)
