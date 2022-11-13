import prettytable as prettytable
from convertTime import convert_time

class DisplayData:

    def __init__(self, data):
        self._data = data

    def print_available_data(self):
        print("> All Available Data")
        # self.print_dept()
        self.print_module()
        self.print_room()
        self.print_instructor()
        # self.print_meeting_times()

    # def print_dept(self):
    #     depts = data.get_depts()
    #     availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
    #     for i in range(0, len(depts)):
    #         courses = depts.__getitem__(i).get_courses()
    #         tempStr = "["
    #         for j in range(0, len(courses) - 1):
    #             tempStr += courses[j].__str__() + ", "
    #         tempStr += courses[len(courses) - 1].__str__() + "]"
    #         availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
    #     print(availableDeptsTable)

    def print_module(self):
        availableCoursesTable = prettytable.PrettyTable(['Course Type', 'Course Name', 'Instructors'])
        modules = self._data.get_modules()
        instructors = self._data.get_instructors()
        for i in range(0, len(modules)):
            tempStr = ""
            # assigns the correct instructor to the class (should work for professors and tutors)
            for j in range(len(instructors)):
                # print(instructors[j].get_modules_taught())
                instructor_modules = instructors[j].get_modules_taught()
                for k in range(len(instructor_modules)):
                    if modules[i].get_id() == instructor_modules[k]:
                        tempStr = instructors[j].get_name()
            availableCoursesTable.add_row(
                [modules[i].get_type(), modules[i].get_name(), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructor'])
        instructors = self._data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['Room ID', 'Room Name', 'Capacity'])
        rooms = self._data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_id()), rooms[i].get_name(), str(rooms[i].get_capacity())])
        print(availableRoomsTable)

    # def print_meeting_times(self):
    #     availableMeetingTimeTable = prettytable.PrettyTable(['id', 'Meeting Time'])
    #     meetingTimes = self._data.get_meetingTimes()
    #     for i in range(0, len(meetingTimes)):
    #         availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
    #     print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'type of conflicts'])
        schedules = population.get_schedules()
        for i in range(0, 1):
            table1.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_num_of_conflicts(), schedules[i].get_type_of_conflicts()])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            ['Class #', 'Module (ID)', 'Room (Capacity)', 'Instructor', 'Meeting Time'])
        for i in range(0, len(classes)):
            table.add_row([str(i),
                           classes[i].get_module().get_name() + " (" + str(classes[i].get_module().get_id()) + ")",

                           classes[i].get_room().get_name() + " (" + str(classes[i].get_room().get_capacity()) + ")",

                           classes[i].get_instructor().get_name() + " (" + str(classes[i].get_instructor().get_id()) + ")",

                           str(convert_time(classes[i].get_start_time().get_start_time())) + " (" + str(classes[i].get_start_time().get_id()) + ")"
                           ])
        print(table)

    def print_schedule_as_table_good(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            ['Time', 'Class #', 'Module (ID)', 'Room (Capacity)', 'Instructor'])
        for i in range(0, len(classes)):
            table.add_row([str(i),
                           classes[i].get_module().get_name() + " (" + str(classes[i].get_module().get_id()) + ")",

                           classes[i].get_room().get_name() + " (" + str(classes[i].get_room().get_capacity()) + ")",

                           classes[i].get_instructor().get_name() + " (" + str(classes[i].get_instructor().get_id()) + ")",

                           str(convert_time(classes[i].get_start_time().get_start_time())) + " (" + str(classes[i].get_start_time().get_id()) + ")"
                           ])
        print(table)
