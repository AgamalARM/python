##################################################
###   Author      : Ahmed Gamal               ####
###   Description : Binary Checker            ####
###                                           ####
###   Date        : 3 Dec 2020                ####
###   Version     : v1                        ####
##################################################

file = open("bootcode.bin", "rb")
mylist = list()
byte = file.read(1)

while byte != b"":
    byte = file.read(1)
    mylist.append(byte)
    
size = str(len(mylist)) 
print(mylist)
print("The Size of Binary file is : "+size)
file.close()

file = open("bootcode.bin", "ab") 
file.write(b"invalid !")        
file.close()       
        