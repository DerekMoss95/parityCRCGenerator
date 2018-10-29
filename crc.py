from array import array
import sys

#16 bit parity test cases
listp1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listp2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
listp3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
listp4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
listp5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]

#256 bit parity test cases
lists1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lists2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
 
#2byte function to return a 8 bit crc code
def initializePresentBits2bytes(list1):
#initialize all present bits to 0
    pb1 = 0
    pb2 = 0
    pb3 = 0
    pb4 = 0
    pb5 = 0
    pb6 = 0
    pb7 = 0
    pb8 = 0

#for loop to move bits around according to given logic
    for x in range(0,16):
        nb1 = list1[x]
        nb2 = pb1
        nb3 = (pb2 ^ pb8)
        nb4 = (pb3 ^ pb8)
        nb5 = (pb4 ^ pb8)
        nb6 = pb5
        nb7 = pb6
        nb8 = pb7
        pb1 = nb1
        pb2 = nb2
        pb3 = nb3
        pb4 = nb4
        pb5 = nb5
        pb6 = nb6
        pb7 = nb7
        pb8 = nb8
#return 8 bit result
    listresults = [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8]
    return listresults

#32byte function to return a 8 bit crc code
def initializePresentBits32bytes(list1):
#initialize all present bits to 0
    pb1 = 0
    pb2 = 0
    pb3 = 0
    pb4 = 0
    pb5 = 0
    pb6 = 0
    pb7 = 0
    pb8 = 0

    for x in range(0,256):
#for loop to move bits around according to given logic
        nb1 = list1[x]
        nb2 = pb1
        nb3 = (pb2 ^ pb8)
        nb4 = (pb3 ^ pb8)
        nb5 = (pb4 ^ pb8)
        nb6 = pb5
        nb7 = pb6
        nb8 = pb7
        pb1 = nb1
        pb2 = nb2
        pb3 = nb3
        pb4 = nb4
        pb5 = nb5
        pb6 = nb6
        pb7 = nb7
        pb8 = nb8
#return 8 bit result

    listresults = [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8]
    return listresults

#call functions for every test case and print out resulting crc codes
results1 = initializePresentBits2bytes(listp1)
results2 = initializePresentBits2bytes(listp2)
results3 = initializePresentBits2bytes(listp3)
results4 = initializePresentBits2bytes(listp4)
results5 = initializePresentBits2bytes(listp5)
results6 = initializePresentBits32bytes(lists1)
results7 = initializePresentBits32bytes(lists2)

if results1 != results2:
    print "The crc checksums were different"
else:
    print "The crc checsums were the same"

print(results1)
print(results2)
print(results3)
print(results4)
print(results5)
print(results6)
print(results7)

