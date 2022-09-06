# a - z huncyoms@gmail.com
# 0 - 9
# . _ time 1
# @ time 1
# . 2,3 position
 
import re #regxe
while(1):
    email_conditon ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_email = input("Enter your email:")

    if re.search(email_conditon,user_email):
        print("right")

    else:
        print("wrong email.")