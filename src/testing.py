import hashlib

def main():

    list =  [1,3,1,13,9,2,3,2,3,3,2,2,1,1,9]

    listnew = [1,2,3]

    # m1 = hashlib.sha256(b'list').hexdigest()
    # m2 = hashlib.sha256(b"P").hexdigest()

    strlist = [str(i) for i in list]
    res = str(int("".join(strlist)))

    listhash = hashlib.sha256(res.encode('utf-8')).hexdigest()

    binaryhash = bin(int(listhash, 16))[2:].zfill(8)
    print(binaryhash)
    hexsstr = str(binaryhash)
    # listhex = list(hexsstr)
    for i in hexsstr:
        listnew.append(int(i))
    print(listnew)


    # print(list)



    # strm1 = bytes(m1, 'utf-8')
    # print(strm1)

    # hexsbin = format(m1, "b")
    # print(hexsbin)
    # for i in m1:
    #     listnew.append(int(i))
    # print(listnew)

    # print("1: ")
    # print(m1)
    # print("2: ")
    # print(m2)

    # zmienna = bin(int(m1, 16))[2:]

    # print(zmienna)


if __name__ == "__main__":
    main()