# leap year 
year=int(input("Enter a year :"))
if (year%400==0) or (year%4==0 and year%100!=0 ):
    print(year,"Yes it is a leap year")
else:
    print(year,"No it is not a leap year")


    
