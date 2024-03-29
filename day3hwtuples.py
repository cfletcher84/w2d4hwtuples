# Tuple Mastery in Python

user_itin = ()

# tuples_list = [('Alice','New York','London'),('Bob','Tokyo','San Fransisco')]

def itin_output(list):
    count = 0
    for i in list:
        name = i[0]
        start = i[1]
        end = i[2]
        count += 1
        print(f'\nItinerary {count}: {name} - From {start} to {end}.')
        
# itin_output([('Alice','New York','London'),('Bob','Tokyo','San Fransisco')])

#  Python Data Structure Challenges in Real-World Scenarios
        
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_new ():
    while True:
        try:
            title = input('\nWhat is the title of the book? : ')
            author = input('\nWho is the author? : ')
            my_tuple = title, author
            if title in library[0]:
                print("This book already exists in the list")
            else:
                library.append(my_tuple)
                print(library)
            return(library)
        except ValueError:
            print("You entered an invalid year.")

# add_new()

# Python Loops and Tuples in Analytical Applications
duplicates_list = []

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-04", 145.0),
    ("MSFT", "2021-01-04", 225.0),
]

def find_dupes():
    user_input = input('\nWhat stock would you like to average? : ')
    for i in stock_data:
        print(i[2])
        if i[0] == user_input:
            duplicates_list.append(i)
        elif i[0] != user_input:
            print('Stock ticker does not exist in data.')
    return duplicates_list

def find_average():
    total_price = 0
    average_price = 0
    for i in duplicates_list:
        print(i)
        total_price += i[2]
        average_price = total_price/len(duplicates_list)
    print(f'Your average price for {i[0]} is {average_price}')
    return average_price

# find_dupes()
# find_average()


# Event Attendance Tracker



attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    ('Chris', 'Tattoo Show')
]

def which_event():
    event_one_count = 0
    event_two_count = 0
    event_three_count = 0
    event_one = []
    event_two = []
    event_three =[]

    for i in attendees:
        if i[1] == 'Python Conference':
            event_one_count += 1
            event_one.append(i[0])
        elif i[1] == "AI Summit":
            event_two_count += 1
            event_two.append(i[0])
        else:
            event_three_count += 1
            event_three.append(i[0])
    return event_one, event_two, event_three, event_one_count, event_two_count, event_three_count


event_stats = which_event()
print(event_stats)

print(f'\nThe Python Conference has the following {event_stats[3]} people attending: \n{event_stats[0]}\
      \nThe AI Summit has the following {event_stats[4]} people attending: \n{event_stats[1]}\
      \nThe Tattoo Show had the following {event_stats[5]} attending: \
      \n{event_stats[2]}')

