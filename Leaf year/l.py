def leap(year):
    if(year%400==0 or year%4==0 and year%100!=0):
        
            return("leap year")
    else:
          return("is not leap year")

year=int(input("enter any year:"))
z=leap(year)
print(z)
        
    