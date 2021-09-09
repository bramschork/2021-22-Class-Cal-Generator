import csv

date_exceptions = [
    9012021,
    9022021,
    9032021,
    9062021,
    9072021,
    9082021,
    9162021, 
    10222021, 
    11152021, 
    11242021,
    11252021,
    11262021,
    12172021,  
    12202021, 
    12212021, 
    12222021, 
    12232021, 
    12242021, 
    12272021, 
    12282021, 
    12292021, 
    12302021, 
    12312021, 
    1172022,
    2182022,
    2212022,
    3242022,
    3252022,
    3282022,
    3292022,
    3302022,
    3312022,
    4012022,
    4152022,
    4182022,
    5302022
    ]

format_bar = [['Subject', 'Start Date', 'Start Time', 'End Time']]
with open('C:/Users/Bram Schork/Desktop/Schedule/classes.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(format_bar)

date = 9092021 #monthdayyear | A-day

def fill_a_days():   
    index_pos = 0
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4    
    
        day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

        a_day = [
            ['Calculus I*', day, '8:30 AM', '9:45 AM'], 
            ['Advisory', day, '9:50 AM', '10:30 AM'],
            ['Finance: Portfolio Analysis', day, '10:30 AM', '11:50 AM'],
            ['Lunch A', day, '11:55 AM', '12:35 PM'],
            ['Woodworking II*', day, '12:40 PM', '1:55 PM'],
            ['Free Period (D Block)', day, '2:00 PM', '3:15 PM']
            ]

        with open('C:/Users/Bram Schork/Desktop/Schedule/classes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(a_day)

def fill_b_days():   
    index_pos = 1
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4    
    
        day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

        b_day = [
            ['Finance: Portfolio Analysis', day, '8:30 AM', '9:45 AM'], 
            ['Community Period', day, '9:50 AM', '10:30 AM'],
            ['Woodworking II*', day, '10:30 AM', '11:50 AM'],
            ['Lunch / Free Period (D Block)', day, '11:55 AM', '1:55 PM'],
            ['Calculus I*', day, '2:00 PM', '3:15 PM']
            ]

        with open('C:/Users/Bram Schork/Desktop/Schedule/classes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(b_day)

def fill_c_days():   
    index_pos = 2
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4    
    
        day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

        c_day = [
            ['Woodworking II*', day, '8:30 AM', '9:45 AM'], 
            ['Advisory', day, '9:50 AM', '10:30 AM'],
            ['Free Period (D Block)', day, '10:30 AM', '11:50 AM'],
            ['Calculus I*', day, '11:55 AM', '1:10 PM'],
            ['Lunch B', day, '1:15 PM', '1:55 PM'],
            ['Finance: Portfolio Analysis', day, '2:00 PM', '3:15 PM']
            ]

        with open('C:/Users/Bram Schork/Desktop/Schedule/classes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(c_day) 

def fill_d_days():   
    index_pos = 3
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4    
    
        day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

        d_day = [
            ['Free Period (D Block)', day, '8:30 AM', '9:45 AM'], 
            ['Advisory', day, '9:50 AM', '10:30 AM'],
            ['Calculus I*', day, '10:30 AM', '11:50 AM'],
            ['Finance: Portfolio Analysis', day, '11:55 AM', '1:10 PM'],
            ['Lunch B', day, '1:15 PM', '1:55 PM'],
            ['Woodworking II*)', day, '2:00 PM', '3:15 PM']
            ]

        with open('C:/Users/Bram Schork/Desktop/Schedule/classes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(d_day)

def get_days_of_year():
    
    global all_dates
    
    all_dates = []

    September = 30
    October = 31
    November = 30
    December = 31
    January = 31
    February = 28
    March = 31
    April = 30
    May = 31
    June = 30

    iterable = 0
    working_date = 9012021

    for num in range(1, September + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= September*10000

    for num in range(1, October + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= October*10000

    for num in range(1, November + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= November*10000

    for num in range(1, December + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= December*10000
    working_date -= 12000000 #NEW YEAR
    working_date += 1

    for num in range(1, January + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= January*10000

    for num in range(1, February + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= February*10000

    for num in range(1, March + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= March*10000

    for num in range(1, April + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= April*10000

    for num in range(1, May + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= May*10000

    for num in range(1, June + 1):
        while iterable < num:
            all_dates.append(working_date)
            working_date += 10000 #advance it by one day
            iterable += 1
    iterable = 0 
    working_date += 1000000
    working_date -= June*10000   
    
    remove_weekends()     
        
def remove_weekends():
    
    global all_dates
    
    #September 1, 2021 is a Wednesday
    
    Weekend = 3
    Sunday = 4

    while Weekend < len(all_dates):
        all_dates.pop(Weekend) #Sat
        all_dates.pop(Weekend) #Sun
        Weekend += 5
        
    remove_school_day_exceptions()
       
def remove_school_day_exceptions():
    
    global all_dates
    index_position = 0
    
    for exception in date_exceptions:
        for item in all_dates:
            if item == exception:
                all_dates.pop(index_position)
            index_position += 1
        index_position = 0
                    
get_days_of_year()

fill_a_days()
fill_b_days()
fill_c_days()
fill_d_days()