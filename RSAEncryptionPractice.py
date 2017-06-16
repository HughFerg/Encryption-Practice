'''
To be created in conjunction with https://www.youtube.com/watch?v=wXB-V_Keiu8
RSA explination
'''


def getAscVal():

    inputStr = raw_input("Enter your message: ")

    ascVal = ""

    for c in inputStr:
        ascVal += str(ord(c))

    print (ascVal)


def main():
    getAscVal()


if __name__ == "__main__":
    main()
