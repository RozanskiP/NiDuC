from PIL import Image
import base64
def ImgToBitArr(filename):
    with open(filename, "rb") as img: #read byte
        hexs = base64.b16encode(img.read()) #hex w byte b`(wartosc)`
        hexs = hexs.decode("utf-8") #czysta wartosc hex  (wartosc)
        IntH = int(hexs, 16) #teraz mamy wartość decimal
        BinH = bin(IntH) #wartosc binarna
        BinH = BinH.replace('0b', '') #wywalenie z 0b z poczatku ciagu
        BinList = list(BinH) #Stworzenie listy z ciagu bitów jest to lista stringów
        BinList = list(map(int, BinList)) #zmiana na liste intów
        return BinList

def BitArrToImg(FileToWrite,bArr):
    print(len(bArr))
    for j in range(5):
        for i in range(10):
            bArr[15000+i+100*j] = 0
            bArr[20000+i+100*j] = 0
            bArr[40000+i+100*j] = 0
            bArr[50000+i+100*j] = 0
    bArr = list(map(str, bArr)) #zmiana na liste stringów
    BitString = "".join(bArr) #zmiana listy na jeden ciag znaków
    img = hex(int(BitString, 2)) #ciag binarny do hexa
    img = img.replace('0x','') #usniecie 0x z 0x(wartosc)
    img = img.upper() #aby base64.b16decode dzialal musza byc duze
    img = img.encode("utf-8") #trzeba zrobic z tego byte object
    img = base64.b16decode(img) #zakodowanie zdjecia
    File = open(FileToWrite, "wb")
    File.write(img)
    File.close()

def TestImages(filename):
    BitArrToImg("Result.jpg",ImgToBitArr(filename))

def ShowResultImage():
    image = Image.open("Result.jpg")
    image.show()