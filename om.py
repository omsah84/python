# # # # # # Using python language to create function and to call

# # # # # # def om(a):
# # # # # #     print("hell")
# # # # # #     print("hhwlo ao")
# # # # # #     print(a)
# # # # # # om(35);


# # # # # # num1 = int(input("Enter the first number:"))
# # # # # # num2 =int(input("Enter the second number:"))

# # # # # # sum= num1 + num2
# # # # # # print("The sum of two number is {} and {} is {}".format(num1,num2,sum));

# # # # # # for i in range(0,5):
# # # # # #     if(num1==5):
# # # # # #         print("first number is equal to 5..")
# # # # # #     else:
# # # # # #         print("not equal to 5")
# # # # # # while(num1>num2):
# # # # # #     print("hell");
# # # # # #     break;
   
# # # # # while(True):
# # # # #     num1 = int(input("Enter the first number:"));
# # # # #     num2=int(input("Enter the second numebr:"));
# # # # #     num3 = int(input("Enter the third number:"));

# # # # #     if((num1>num2)and(num1>num3)):
# # # # #         print("First number is greater than seond number or third numebr.");
# # # # #         print("\n")

# # # # #     elif(num2>num3):
# # # # #         print("second number is greater than first number and third number...")

# # # # #     else:
# # # # #         print("third number is greater than first number and second number...")



# # # # number = int(input("Enter the step of fiboniseries"))
# # # # a = 0 #int(input("Enter the first numebre...")
# # # # b = 1 #int(input("Enter the second number..."))
# # # # i =0;
# # # # print(a)
# # # # print(b)

# # # # while(i<number):
# # # #     c= a+b;
# # # #     a =b;
# # # #     b=c;
# # # #     print(c);

# # # #     i=i+1;

# # # nunber = int(input("Enter the number="));
# # # a = 0;
# # # b = 1;
# # # print(a);
# # # print(b);

# # # for i in range(0,nunber):
# # #     c =a+b;
# # #     a=b;
# # #     b=c;
# # #     print(c)

# # a = int(input("Enter the number="))

# # for i in range(2,a):
# #     if(i%2==0):
# #         pass;
# #     else:
# #         print(i)

# lis = []

# num = int(input("Enter the numebr="))

# for i in range(num):
#     number = int(input())
#     lis.append(number)

# print("the list is =",lis);

# print("the sum is=",sum(lis));

# print(list(set(lis)));

list = []

for i in range(7):
    a = int(input())
    list.append(a)

print(list); fd

list = list.sort();
print(list)
