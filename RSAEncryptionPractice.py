'''
To be created in conjunction with https://www.youtube.com/watch?v=wXB-V_Keiu8
RSA explination
'''
import random
import time


def getAscVal():

    inputStr = raw_input("Enter your message: ")

    ascVal = ""

    for c in inputStr:
        ascVal += str(ord(c))

    print (ascVal)

# checks to see if number is prime


def isPrime(n, k):

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in lowPrimes:
        return True
    for prime in lowPrimes:
        if (n % prime == 0):
            return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Miller-Rabin Primality Test

    r = 0
    s = n - 1

    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def calcPrimes():
    num1 = random.getrandbits(2084)
    if num1 % 2 == 0:
        num1 += 1
    num2 = random.getrandbits(2084)
    if num2 % 2 == 0:
        num2 += 1

    while not isPrime(num1, 400):
        num1 += 1
    while not isPrime(num2, 400):
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
    startTime = time.time()
    calcPrimes()
    print (time.time() - startTime)


if __name__ == "__main__":
    main()
