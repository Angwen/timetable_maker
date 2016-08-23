# coding=utf-8


import tkinter
import tkinter.messagebox as mbox

ORARENDKESZITO = 'Órarendkészítő'
EDDIGI_ORAK_OSSZESEN = "Eddigi órák száma összesen:"
LABEL_BLANK_SLOT = "Lyukasóra"


class Subject:
    subject_name = None
    subject_number = None

    def __init__(self, subject_name, subject_number):
        self.subject_name = subject_name
        self.subject_number = subject_number

    def __str__(self):
        return "Subject{subject_name=%s;subject_number=%s}" % (self.subject_name, self.subject_number)


class Subjects:
    sum_of_lessons = None
    subject1 = None
    subject2 = None
    subject3 = None

    def __init__(self, subject_numbers=None, subject1=None, subject2=None, subject3=None):
        if subject_numbers is None:
            self.subject_numbers = []
        else:
            self.subject_numbers = subject_numbers

        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def __str__(self):
        return "Subject{subject1=%s;subject2=%s;subject3=%s}" % (self.subject1, self.subject2, self.subject3)

    def calculate_sum_of_lessons(self):
        return calculate_total_lessons_count(self.subject_numbers)


schedule = []
subjects = Subjects()


def init_window():
    window = tkinter.Tk()
    window.wm_withdraw()
    mbox.showinfo('%s' % ORARENDKESZITO, "Ez egy órarendkészítő alkalmazás, \
ami az általad megadott három tantárgy nevéből és számából generál egy órarendet.")


def create_blank_scheduler_table():
    global schedule
    header = ["Időpont", "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek"]
    schedule = [header, [], [], [], []]
    create_blank_slots()
    assign_row_labels()


def assign_row_labels():
    assign_row_label(1, "8:00 - 8:45")
    assign_row_label(2, "9:00 - 9:45")
    assign_row_label(3, "10:00 - 10:45")
    assign_row_label(4, "11:00 - 11:45")


def assign_row_label(column_index, label):
    global schedule
    schedule[column_index][0] = label


def create_blank_slots():
    global schedule
    for row in schedule:
        if schedule.index(row) != 0:
            for column_index in range(0, len(schedule)+1):
                row.append(LABEL_BLANK_SLOT)


def check_and_create_subject():
    """
    function for getting input and checking input type
    :return: a Subject
    """
    textual_input_present = False
    name_of_subject = ''
    while not textual_input_present:
        name_of_subject = input(("Tantárgy neve:"))
        if len(name_of_subject.strip()) == 0:
            print("Kérlek, ne hagyd üresen a mezőt!")
        elif name_of_subject.isnumeric():
            print("Kérlek, adj meg szöveges tantárgynevet!")
        else:
            textual_input_present = True

    numerical_input_present = False
    while not numerical_input_present:
        number_of_subject = input(name_of_subject + "órák száma a héten:")
        if not number_of_subject.isnumeric():
            print("Kérlek, egy számot adj meg!")
        elif int(number_of_subject) > 20 or int(number_of_subject) == 0:
            print("Kérlek, egy 1 és 20 közötti számot adj meg!")
        else:
            subjects.subject_numbers.append(int(number_of_subject))
            return Subject(name_of_subject, int(number_of_subject))


def calculate_total_lessons_count(lesson_counts):
    total_lessons_count = 0
    for lesson_count in lesson_counts:
        total_lessons_count += lesson_count
    return total_lessons_count


def read_and_create_model():
    global subjects
    correct_input = False
    while not correct_input:

        subject_numbers = []

        subject1 = check_and_create_subject()
        subject_numbers.append(subject1.subject_number)
        sum_of_lessons = calculate_total_lessons_count(subject_numbers)
        print(EDDIGI_ORAK_OSSZESEN, sum_of_lessons)
        print("Összesen 20 db. óra lehet a héten.")

        subject2 = check_and_create_subject()
        subject_numbers.append(subject2.subject_number)
        sum_of_lessons = calculate_total_lessons_count(subject_numbers)
        print(EDDIGI_ORAK_OSSZESEN, sum_of_lessons)
        print("Összesen 20 db. óra lehet a héten.")

        subject3 = check_and_create_subject()
        subject_numbers.append(subject3.subject_number)
        sum_of_lessons = calculate_total_lessons_count(subject_numbers)

        if sum_of_lessons > 20:
            mbox.showinfo(ORARENDKESZITO,
                          'A megadott óraszám túl magas! Kérlek, összesen legfeljebb 20 db. órát adj meg.')
        else:
            correct_input = True
            subjects = Subjects(subject_numbers, subject1, subject2, subject3)


def random_distribute_subjects(name_of_subject, number_of_subject):
    import random
    while number_of_subject > 0:
        timeslot = random.randint(1, 4)
        day = random.randint(1, 5)
        if schedule[timeslot][day] == LABEL_BLANK_SLOT:
            schedule[timeslot][day] = name_of_subject
            number_of_subject -= 1


def distribute_all_subjects():
    random_distribute_subjects(subjects.subject1.subject_name, subjects.subject1.subject_number)
    random_distribute_subjects(subjects.subject2.subject_name, subjects.subject2.subject_number)
    random_distribute_subjects(subjects.subject3.subject_name, subjects.subject3.subject_number)


def calculate_schedule_by_day():
    schedule_by_columns = []
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []

    def rearrange(day, column):
        for row in schedule:
            if schedule.index(row) != 0:
                day.append(row[column])

    rearrange(monday, 1)
    rearrange(tuesday, 2)
    rearrange(wednesday, 3)
    rearrange(thursday, 4)
    rearrange(friday, 5)
    schedule_by_columns.append(monday)
    schedule_by_columns.append(tuesday)
    schedule_by_columns.append(wednesday)
    schedule_by_columns.append(thursday)
    schedule_by_columns.append(friday)
    return schedule_by_columns


def define_empty_slots(schedule_by_day):
    global x
    for line in schedule_by_day:
        n = line.count(LABEL_BLANK_SLOT)
        while n > 0:
            if line.index(LABEL_BLANK_SLOT) == 0:
                line[0] = "Temp"
                n -= 1
            else:
                x = line.index(LABEL_BLANK_SLOT)
                placeholder = line[3 - (n - 1)]
                line[3 - (n - 1)] = LABEL_BLANK_SLOT
                line[x] = placeholder
                n -= 1
        if line[0] == "Temp":
            line[0] = LABEL_BLANK_SLOT


def store_constrained_and_ordered_timetable(schedule_by_day):
    global schedule, x
    for row in schedule:
        for x in range(1, 5):
            for y in range(1, 6):
                schedule[x][y] = schedule_by_day[y - 1][x - 1]


def popup_message_box():
    # window = tkinter.Tk()
    # window.wm_withdraw()
    message = "Egy héten %s %sóra, %s %sóra és %s %sóra lesz. Ez összesen %s óra. A generált órarendet az orarend.csv fájlban találod." \
              % (subjects.subject1.subject_number, subjects.subject1.subject_name, subjects.subject2.subject_number,
                 subjects.subject2.subject_name, subjects.subject3.subject_number, subjects.subject3.subject_name,
                 subjects.calculate_sum_of_lessons())
    mbox.showinfo(ORARENDKESZITO, message)


def write_csv_file():
    import csv
    output = csv.writer(open("orarend.csv", "w"), delimiter=';',
                        lineterminator='\n')  # the name of the output file variable
    for row in schedule:
        output.writerow(row)


def schedule_main():
    """
    This is the main entry point.
    :return:
    """
    init_window()
    create_blank_scheduler_table()
    read_and_create_model()
    distribute_all_subjects()
    schedule_by_day = calculate_schedule_by_day()
    define_empty_slots(schedule_by_day)
    store_constrained_and_ordered_timetable(schedule_by_day)
    popup_message_box()
    write_csv_file()


if __name__ == "__main__":
    schedule_main()
