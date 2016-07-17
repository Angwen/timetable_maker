"""making the blank schedule table"""

orarend = [] # the whole schedule table itself

first_row = []  # creating lists for rows
first_slot = []
second_slot = []
third_slot = []
fourth_slot = []

orarend.append(first_row) # assigning row lists to the schedule table
orarend.append(first_slot)
orarend.append(second_slot)
orarend.append(third_slot)
orarend.append(fourth_slot)

first_row.append("Időpont") # defining column names
first_row.append("Hétfő")
first_row.append("Kedd")
first_row.append("Szerda")
first_row.append("Csütörtök")
first_row.append("Péntek")

for row in orarend: # creating index for time slot assignment
        if row != first_row:
                row.append(["Lyukasóra"])

first_slot[0] = "8:00 - 8:45"
second_slot[0] = "9:00 - 9:45"
third_slot[0] = "10:00 - 10:45"
fourth_slot[0] = "11:00 - 11:45"
	
for row in orarend: # assign filler to blank spaces
        if row != first_row:
                for i in range(0,5):
                        row.append("Lyukasóra")

"""asking user for number and names of classes"""

class_numbers = [] # list for all class numbers to calculate sum

class_name1 = input("Tantárgy neve:")
nr_class1 = int(input(class_name1 + "órák száma a héten:"))
class_numbers.append(nr_class1)
class_name2 = input("Tantárgy neve:")
nr_class2 = int(input(class_name2 + "órák száma a héten:"))
class_numbers.append(nr_class2)
class_name3 = input("Tantárgy neve:")
nr_class3 = int(input(class_name3 + "órák száma a héten:"))
class_numbers.append(nr_class3)

def classes_total(classes): # function for calculating sum of lessons
    total = 0
    for i in classes:
        total += i
    return total
    
sum_of_lessons = classes_total(class_numbers) # variable for sum of lessons

print("A héten a %sórák száma %s, a %sórák száma %s, \
a %sórák száma pedig %s. Ez összesen %s óra." \
% (class_name1, nr_class1, class_name2, nr_class2, \
class_name3, nr_class3, sum_of_lessons))


"""assigning classes to empty slots"""

def assign_class(number_of_class, name_of_class): # function for assigning a given number of classes to empty slots
        for timeslot in range(1,5):
                for day in range(1,6):
                        for row in orarend:
                                while number_of_class > 0 and orarend[timeslot][day] == "Lyukasóra":
                                        orarend[timeslot][day] = name_of_class
                                        number_of_class -= 1

assign_class(nr_class1, class_name1)
assign_class(nr_class2, class_name2)
assign_class(nr_class3, class_name3)


"""printing the blank schedule table"""

for row in orarend:
        for i in row:
                print(i, end=" ")
                               

"""printing the schedule table into a csv file"""

output = open("orarend.csv", "w") # the name of the output file variable
for row in orarend:
        for i in row:
                output.write(str(i)+" ")
output.close()
