def firstSetBit(n):
    count = 1
    while(n):
        if(n&1 == 1):
            break
        count += 1
        n >>= 1
    return count

#OnesAndZeros
def numOfBits(n):
    ones = 0
    zeros = 0
    while(n):
        if(n&1 == 1):
            ones+=1
        else:
            zeros+=1
        n >>= 1
    print("\n\nOnes = ", ones, "\nZeros ", zeros)


num = int(input("Enter a number of your choice: "))
numOfBits(num)

#nthBitSetorNot
def setOrNot(number , n):
    if number & 1 << (n-1):
        print("\nSET")
    else:
        print("\nNOT SET")

number = int(input("Enter a number: "))
n = int(input("Enter a bit number: "))
setOrNot(number, n)