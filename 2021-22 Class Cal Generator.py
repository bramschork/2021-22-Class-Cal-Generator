import csv

a_day_classes = ['Calculus I*', 'Community Period', 'Finance: Portfolio Analysis', 'Lunch A', 'Woodworking II*', 'Free Period (D Block)']
b_day_classes = ['Finance: Portfolio Analysis', 'Community Period', 'Woodworking II*', 'Lunch / Free Period (D Block)', 'Calculus I*']
c_day_classes = ['Woodworking II*', 'Community Period', 'Free Period (D Block)', 'Calculus I*', 'Lunch B', 'Finance: Portfolio Analysis']
d_day_classes = ['Free Period (D Block)', 'Community Period', 'Calculus I*', 'Finance: Portfolio Analysis', 'Lunch B', 'Woodworking II*)']

file_path = 'C:/Users/Bram Schork/Dropbox/Bram/Projects/2021-22-Class-Cal-Generator/classes.csv'

global weds

weds = []

date_exceptions = [
    9012021,
    9022021,
    9032021,
    9062021,
    9072021,
    9082021,
    9162021,
    10112021, 
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
with open(file_path, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(format_bar)

def get_days_of_year():
    
    global all_dates, weds
    
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
    

    date = 9082021 #monthdayyear | A-day
    iter = 0 
    while iter < len(all_dates):
        wed_date = (all_dates[iter])
        weds.append(wed_date)
        iter += 7
    print(weds)

    date = 9092021 #monthdayyear | A-day | first day of school
    
    remove_weekends()     
   
def fill_a_days():   
    index_pos = 0
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4       
        
        if date in weds: #if this is true, meaning the date is a wednesday
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            a_day = [
                [a_day_classes[0], day, '9:00 AM', '10:15 AM'], 
                ['Break', day, '10:15 AM', '10:30 AM'],
                [a_day_classes[2], day, '10:35 AM', '11:50 AM'],
                [a_day_classes[3], day, '11:55 AM', '12:35 PM'],
                [a_day_classes[4], day, '12:40 PM', '1:55 PM'],
                [a_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(a_day)
        else:
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            a_day = [
                [a_day_classes[0], day, '8:30 AM', '9:45 AM'], 
                [a_day_classes[1], day, '9:50 AM', '10:30 AM'],
                [a_day_classes[2], day, '10:30 AM', '11:50 AM'],
                [a_day_classes[3], day, '11:55 AM', '12:35 PM'],
                [a_day_classes[4], day, '12:40 PM', '1:55 PM'],
                [a_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(a_day)

def fill_b_days():   
    index_pos = 1
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4    

        if date in weds: #if this is true, meaning the date is a wednesday
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            b_day = [
                [b_day_classes[0], day, '9:00 AM', '10:15 AM'], 
                ['Break', day, '10:15 AM', '10:30 AM'],
                [b_day_classes[2], day, '10:35 AM', '11:50 AM'],
                [b_day_classes[3], day, '11:55 AM', '1:55 PM'],
                [b_day_classes[4], day, '2:00 PM', '3:14 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(b_day)
                
        else:
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            b_day = [
            [b_day_classes[0], day, '8:30 AM', '9:45 AM'], 
            [b_day_classes[1], day, '9:50 AM', '10:30 AM'],
            [b_day_classes[2], day, '10:30 AM', '11:50 AM'],
            [b_day_classes[3], day, '11:55 AM', '1:55 PM'],
            [b_day_classes[4], day, '2:00 PM', '3:15 PM']
            ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(b_day)

def fill_c_days():   
    index_pos = 2
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4       
        
        if date in weds: #if this is true, meaning the date is a wednesday
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            c_day = [
                [c_day_classes[0], day, '9:00 AM', '10:15 AM'], 
                ['Break', day, '10:15 AM', '10:30 AM'],
                [c_day_classes[2], day, '10:35 AM', '11:50 AM'],
                [c_day_classes[3], day, '11:55 AM', '1:10 PM'],
                [c_day_classes[4], day, '1:15 PM', '1:55 PM'],
                [c_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(c_day)
        else:
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            c_day = [
                [c_day_classes[0], day, '8:30 AM', '9:45 AM'], 
                [c_day_classes[1], day, '9:50 AM', '10:30 AM'],
                [c_day_classes[2], day, '10:30 AM', '11:50 AM'],
                [c_day_classes[3], day, '11:55 AM', '1:10 PM'],
                [c_day_classes[4], day, '1:15 PM', '1:55 PM'],
                [c_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(c_day)

def fill_d_days():   
    index_pos = 3
    while index_pos < len(all_dates):
        date = all_dates[index_pos]
        index_pos += 4       
        
        if date in weds: #if this is true, meaning the date is a wednesday
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            d_day = [
                [d_day_classes[0], day, '9:00 AM', '10:15 AM'], 
                ['Break', day, '10:15 AM', '10:30 AM'],
                [d_day_classes[2], day, '10:35 AM', '11:50 AM'],
                [d_day_classes[3], day, '11:55 AM', '1:10 PM'],
                [d_day_classes[4], day, '1:15 PM', '1:55 PM'],
                [d_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(d_day)
        else:
            day = ('{0}/{1}/{2}'.format(str(date)[:-6], str(date)[-6:-4], str(date)[-4:])) #Month/Day/Year'

            d_day = [
                [d_day_classes[0], day, '8:30 AM', '9:45 AM'], 
                [d_day_classes[1], day, '9:50 AM', '10:30 AM'],
                [d_day_classes[2], day, '10:30 AM', '11:50 AM'],
                [d_day_classes[3], day, '11:55 AM', '1:10 PM'],
                [d_day_classes[4], day, '1:15 PM', '1:55 PM'],
                [d_day_classes[5], day, '2:00 PM', '3:15 PM']
                ]

            with open(file_path, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(d_day)
     
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