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
    # Miller-Rabin Primality Test
    twoToThex = float(1)
    multiplier = float()

    multiplier = (n - 1) / (2**twoToThex)

    while (multiplier.is_integer()):
        print twoToThex
        print multiplier
        twoToThex = twoToThex + 1
        multiplier = (n - 1) / (2**twoToThex)

    twoToThex = twoToThex - 1
    multiplier = (n - 1) / (2**twoToThex)

    print ("%s = 2^%s * %s" % (n - 1, twoToThex, multiplier))

    # Choosing random number between 1,n-1

    a = random.randint(1, n - 1)

    b = (2 ** multiplier) % n

    print b

    if b == 1 or b == -1:
        return True

    while (b != 1):
        b = ((b ** 2) % n)
        a += 1
    if b == 1:
        print ("%s is not prime!" % n)
    elif b == -1:
        print("%s is probably prime!" % n)


def calcPrimes():
    num1 = random.getrandbits(2084)
    if num1 % 2 == 0:
        num1 += 1
    num2 = random.getrandbits(2084)
    if num2 % 2 == 0:
        num2 += 1
    n = num1 * num2

    phiOfn = (num1 - 1) * (num2 - 1)

    e = 17
    print num1
    print num2
    print ("n =  %s" % n)
    print ("Phi of n = %s" % phiOfn)
    print ("e = %s" % e)


def main():
    getAscVal()
    calcPrimes()
    isPrime(561)


if __name__ == "__main__":
    main()
