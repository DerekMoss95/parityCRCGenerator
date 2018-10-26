from array import array
import sys, os

#8 bit parity test cases
listp1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listp2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
listp3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
listp4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
listp5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]

lists1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lists2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
 
def initializePresentBits(list1):
    pb1 = 0
    pb2 = 0
    pb3 = 0
    pb4 = 0
    pb5 = 0
    pb6 = 0
    pb7 = 0
    pb8 = 0

    for x in range(0,16):
        #print(x)
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
        #print(pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8)
    listresults = [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8]
    return listresults

def initializePresentBits32bytes(list1):
    pb1 = 0
    pb2 = 0
    pb3 = 0
    pb4 = 0
    pb5 = 0
    pb6 = 0
    pb7 = 0
    pb8 = 0

    for x in range(0,256):
        #print(x)
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
        #print(pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8)
    listresults = [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8]
    return listresults

results1 = initializePresentBits(listp1)
results2 = initializePresentBits(listp2)
results3 = initializePresentBits(listp3)
results4 = initializePresentBits(listp4)
results5 = initializePresentBits(listp5)
results6 = initializePresentBits32bytes(lists1)
results7 = initializePresentBits32bytes(lists2)

print(results1)
print(results2)
print(results3)
print(results4)
print(results5)
print(results6)
print(results7)

# Next Bit 1 = next bit of Data In

# Next Bit 2 = Present Bit 1
# Next Bit 3 = Present Bit 2 XOR
# present Bit 8
# Next Bit 4 = Present Bit 3 XOR
# present Bit 8
# Next Bit 5 = Present Bit 4 XOR
# present Bit 8
# Next Bit 6 = Present Bit 5
# Next Bit 7 = Present Bit 6
# Next Bit 8 = Present Bit 7
# Move next states into present states
# Present Bit 1 = Next Bit 1
# Present Bit 2 = Next Bit 2
# Present Bit 3 = Next Bit 3
# Present Bit 4 = Next Bit 4
# Present Bit 5 = Next Bit 5
# Present Bit 6 = Next Bit 6
# Present Bit 7 = Next Bit 7
# Present Bit 8 = Next Bit 8
