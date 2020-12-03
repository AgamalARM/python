##################################################
###   Author      : Ahmed Gama                ####
###   Description : Initialization Direction  ####
###                 of PORTA AVR              ####
###   Date        : 3 Dec 2020                ####
###   Version     : v1                        ####
##################################################
myfile = open("InitAVR.c" , "w")
i = int(0)
port = list()
while i < 8 :
    while True :
        x = input("Please Enter Bit "+str(i)+" mode : ")
        x = x.lower()
        if x == "input":
            port.append(0)
            break
        
        elif x == "output":
            port.append(1)
            break
        else  :
            print("Wrong Bit Mode ,Please Try again")
        
    i = i + 1
print(port)
s = """void Init_PORTA_DIR (void)
{
    DDRA = 0b"""+str(port[7])+str(port[6])+str(port[5])+str(port[4])+str(port[3])+str(port[2])+str(port[1])+str(port[0])
u = """
}"""
z = s + u
myfile.write(z)
print(z)
myfile.close()
