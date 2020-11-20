bold= '\33[1m'
red='\33[41m'
green= '\33[42m'
end= '\33[0m'
print(bold+'WELCOME TO THE VALIDATION PORTAL'+end)
print()
def first(a):
    return(a[:1])
def leftnum(a):
    return(a[3:])
def left(a):
    return(a[1:3])
a=input("Please enter your 6 digit validation key: ")
logic=True
while logic==True:
    ans=first(a)
    ans1=leftnum(a)
    ans2=left(a)
    b=(len(a)==6) and (ans>="A" and ans<"[") and (ans1>='0' and ans1<':') and (ans2>="a" and ans2<"{")
    if b==True:
        c=input(bold+"Please enter your 6 digit validation key again: "+end)
        if b and (a==c):
            print(green+'SUCCESS'+end)
            logic=False
        else:
            
            print(red+"PLEASE TRY AGAIN"+end)
            a=input(bold+"Please enter your 6 digit validation key: "+end)
            
    elif b==False:
        print(red+"PLEASE INPUT DATA IN CORRECT FORMAT"+end)
        print()
        a=input(bold+"Please enter your 6 digit validation key: "+end)

        
        
        
