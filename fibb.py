number = int(input("how many terms you want"))
f1 = 0
f2 =1
count = 0
if number==0:
    print("0 is a number")
elif number==1:
    print('1 is a number')
else:
    while count<number:
        nth = f1+f2
        f1 =f2
        f2 = nth
        count += 1
