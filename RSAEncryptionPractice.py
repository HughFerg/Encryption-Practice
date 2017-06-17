'''
To be created in conjunction with https://www.youtube.com/watch?v=wXB-V_Keiu8
RSA explination
'''
import random


def getAscVal():

    inputStr = raw_input("Enter your message: ")

    ascVal = ""

    for c in inputStr:
        ascVal += str(ord(c))

    print (ascVal)

# checks to see if number is prime


def isPrime(n):
    count = 0
    for a in range(2, n - 1):
        if n % a == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

# calculates every prime number in range and puts it in list "primeList"


def calcPrimes():
    primeList = []
    for c in range(2, 5000):
        if isPrime(c):
            primeList.append(str(c))
    # calls func to selct 2 random prime numbers from primeList
    getRandomPrimes(primeList)


def getRandomPrimes(primeList):
    print primeList[random.randint(0, len(primeList) - 1)]
    print primeList[random.randint(0, len(primeList) - 1)]


def main():
    getAscVal()
    calcPrimes()


if __name__ == "__main__":
    main()
