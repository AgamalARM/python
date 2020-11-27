########################   Mobile Number Check  ###########
number  = str (input("Enter your mobile Number : "))
count   = 0 
flag    = 0 
for i in number :
    if i>='0' and i<='9' :
        count = count + 1
    else :
        print("The Number must be contain numic value")
        flag = 1
        break
if flag == 0 :
    if count == 11 :
        print("the Number Accepted")
    else :
        print("The Number Must be 11 digit")
else:
    pass
