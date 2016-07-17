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

"""asking user for number of classes"""

lit_class = int(input("Magyarórák száma a héten:"))
mat_class = int(input("Matematikaórák száma a héten:"))
phys_class = int(input("Fizikaórák száma a héten:"))

print("A héten a magyarórák száma %s, a matematikaórák száma %s, \
a fizikaórák száma pedig %s. Ez összesen %s óra." \
% (lit_class, mat_class, phys_class, (lit_class+mat_class+phys_class)))

"""assigning classes to empty slots"""

def assign_class(number_of_class, name_of_class): # function for assigning a given number of classes to empty slots
        for timeslot in range(1,5):
                for day in range(1,6):
                        for row in orarend:
                                while number_of_class > 0 and orarend[timeslot][day] == "Lyukasóra":
                                        orarend[timeslot][day] = name_of_class
                                        number_of_class -= 1

assign_class(lit_class, "Irodalomóra")
assign_class(phys_class, "Fizikaóra")
assign_class(mat_class, "Matematikaóra")


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
