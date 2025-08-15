a=input("Enter any string value")
if (a.replace(' ','').isalpha):
    if len(a)<3:
        print("enter above 3 digit ")
        
    elif len(a)>20:
        print("enter below 20 digit ")

    elif len(a)>=3 and len(a)<=20:
        print(a)
        

    

# else:
#     print("Not a String")

# if str!=number:
#     print(a)

# else:
#     print


# email

E=input("enter any email: ")

if (E[0].isalpha() and E.endswith('@email.com'or "@yahoo.com" )):
    print('This is valid Email')

else:
    print("this is not valid Email")