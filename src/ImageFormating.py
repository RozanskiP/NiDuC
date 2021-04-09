from PIL import Image
import numpy as np

def loadImage(filename):
    image = Image.open(filename)
    image.show()
    return image

# wyświetlenie orginalnego zdjęcia
def displayOriginalImage(image):
    print("Display: ")
    array = numpy.array(image)
    Flattenarray = array.flatten('C')
    binarray = []
    imagenew = Image.fromarray(Flattenarray)
    
    print("Array: ")
    for list in Flattenarray:
        binarray.append(format(list, "b"))
    print(Flattenarray.size)
    # for list2 in binarray:
    #     print(binarray)
    print(Flattenarray[0])
    print(binarray[0])
    i = 0
    for list2 in binarray[0]:
        print(list2)
        i += 1
    print("SIZE: ", i)

    intt = 100
    print(format(intt, "b"))

    pass

def displayImageBeforeTransmision():
    pass

def formatArray():
    pass

def formatFramesWithCode():
    pass

def main():
    # image = loadImage("../pies.jpg") # ../pies.jpg
    # displayOriginalImage(image)

    img = Image.open('../pies.jpg')
    ary = np.array(img)

    # Split the three channels
    r,g,b = np.split(ary,3,axis=2)
    r=r.reshape(-1)
    g=r.reshape(-1)
    b=r.reshape(-1)

    # Standard RGB to grayscale 
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
    zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    im.save('pies2.jpg')

    pass

if __name__ == "__main__":
    main()