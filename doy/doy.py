# Code qui calcule le nombre de jour jusqua un date donner
# Code that calculates the number of days until a given date.
def is_year_leap(year):
# Vérifier si l'année est bissextile ou pas
# Verify if a given year is leap year or not
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

def days_in_month(year, month):
    m31 = (1,3,5,7,8,10,12)
    if month in m31:
        return 31
    elif month == 2:
        if  is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return 30

def day_of_year(year, month, day):
    i=1
    s=0
    while i < month:
        s+=days_in_month(year,i)
        i+=1
    return s+day
# tester pour la date 10/03/2025
print(day_of_year(2025, 3, 10))
