# # num = int(input("Enter first number: "))
# # if(num>0):
# #     print("Positive number")
# # elif(num==0):
# #     print("Zero")
# # else:
# #     print("Negative number")
# # names = ["Ali","Ahmad","Arsalan","Ahtasam","Abubakar"]
# # for name in names:
# #     print(f"Hello, {name}")
# # #The following code will print  sum of first 10 numbers using while loop
# # i = 1
# # sum = 0
# # while(i<=10):
# #     sum = sum + i
# #     i = i + 1

# # print(f"The sum of first 10 numbers is: {sum}")
# def CalculateArea(len=1 ,Width=1):
#     return len*Width

# area = CalculateArea(4,5)

# print(area)
Name="Behram"
Age=15
Class="AI Depart"
context =  f"{Name},{Age},{Class}"
           
with open("Example.txt","w") as file:
    file.write(context)
    
with open("Example.txt","r") as file:
    Sub = file.read()

print(Sub)