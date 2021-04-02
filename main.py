from Generator import generateBit
from Coder import coderBit
from TransmisionCannal import transmision

def main():
    bits = []
    generateBit(bits, 25)
    print(bits)
    listofbits = coderBit(bits, 10)
    print("List of list: ")
    print(listofbits)

    transmision(listofbits, 0.5) # minimalnie 0.001 (1 promil)
    print(listofbits)

if __name__ == "__main__":
    main()
