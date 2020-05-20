num=0
tot=0.0
while True:
    val=input("Enter a number:")
    if val=='done':
        break
    try:
        fval=float(val)
    except:
        print("Invalid input")

    num=num+1
    tot=tot+fval

print(tot,num)
