while True:
    marks = float(input("Enter your Marks(0-100):"))
    if marks<100:
        break
    print("Wrong Number")  
if marks > 90:
    remarks = "Good"
elif marks>80:
    remarks = "you can do better"
elif marks>70:
    remarks ="you need to improve"
else:
    remarks = "You are faild"
print(remarks)
# Next Program
