from array import array
import sys

#8 bit parity test cases
listp1 = [0,0,1,0,1,1,0,1]
listp2 = [0,0,0,1,1,0,0,1]
listp3 = [0,0,0,1,1,1,0,1]
listp4 = [0,0,0,1,1,1,1,1]

#function to create parity bit as well as append it to the end of the list
def makeParity(list1):
    list2 = [(list1[0] ^ list1[1]), (list1[2] ^ list1[3]), (list1[4] ^ list1[5]), (list1[6] ^ list1[7])]
    list3 = [(list2[0] ^ list2[1]), (list2[2] ^ list2[3])]
    list4 = [(list3[0] ^ list3[1])]
    list5 = list1 + list4
    print(list5)
    return list5

#Define a new list defined by calling the makeParity function
listparity1 = makeParity(listp1)
listparity2 = makeParity(listp4)

#Adds all the values of each list and stores it
counter1 = sum(listparity1)
counter2 = sum(listparity2)

#Checks if the sum modulus 2 returns anything other than 0
if ((counter1 % 2) > 0):
    print("The modulus returned more than 0")
    parity = False
else:
    print("Modulus returned 0")
    parity = True

#Checks if the parity bit was the same between the lists being compared
if (listparity1[8] != listparity2[8]):
    print("Parity was NOT the same.")
    paritybit = False
else: 
    print("Parity was the same!")
    paritybit = True

#Checks if overall, the transmission are the same, will however fail if there are 2 errors. All other number of errors should return false
if parity & paritybit == True:
    print("Overall, the byte was fine!")
else:
    print("Failed the parity check")
