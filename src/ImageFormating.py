from PIL import Image
import base64

def ImgToBitArr(filename):
    with open(filename, "rb") as img: #read byte
        hexs = base64.b16encode(img.read()) #hex w byte b`(wartosc)`
        hexs = hexs.decode("utf-8") #czysta wartosc hex  (wartosc)
        IntH = int(hexs, 16) #teraz mamy wartość decimal
        BinH = bin(IntH) #wartosc binarna
        BinH = BinH.replace('0b', '') #wywalenie z 0b z poczatku ciagu
        BinList = list(BinH) #lista
        BinList = list(map(int, BinList))
        return BinList

def BitArrToImg(FileToWrite,bArr):
    bArr = list(map(str, bArr))
    BitString = "".join(bArr)
    img = hex(int(BitString, 2)) #odrazu do hexa
    img = img.replace('0x','') #usniecie 0x z 0x(wartosc)
    img = img.upper() #aby base64.b16decode dzialal musza byc duze
    img = img.encode("utf-8") #trzeba zrobic z tego byte object
    img = base64.b16decode(img) #zakodowanie zdjecia
    File = open(FileToWrite, "wb")
    File.write(img)
    File.close()

def TestImages(filename):
    BitArrToImg("Result.jpg",ImgToBitArr(filename))