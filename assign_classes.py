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

"""assigning classes to empty slots"""

lit_cl = 5 # number of literature classes


for x in range(1,5):
        for y in range (1,6):
                for row in orarend:
                        if orarend[x][y] == "Lyukasóra":
                                orarend[x][y] = "Irodalomóra"


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
