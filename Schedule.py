import random as rnd

from Class import Class
from Instructor import Instructor


# from Data import Data

class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._num_of_conflicts = 0
        self._type_of_conflicts = []
        self._fitness = -1
        self._num_of_classes = 0
        self._is_fitness_changed = True

    def get_classes(self):
        self._is_fitness_changed = True
        return self._classes

    def get_num_of_conflicts(self):
        return self._num_of_conflicts

    def get_type_of_conflicts(self):
        return self._type_of_conflicts

    def get_fitness(self):
        if self._is_fitness_changed:
            self._fitness = self.calculate_fitness()
            self._is_fitness_changed = False
        return self._fitness

    def initialize(self):
        modules = self._data.get_modules()
        instructors = self._data.get_instructors()
        for i in range(len(modules)):
            new_class = Class(self._num_of_classes, modules[i], modules[i].get_duration())
            self._num_of_classes += 1

            new_class.set_start_time(self._data.get_start_times()[rnd.randrange(0, len(self._data.get_start_times()))])

            new_class.set_day(self._data.get_days()[rnd.randrange(0, len(self._data.get_days()))])

            new_class.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])

            # assigns the correct instructor to the class (should work for professors and tutors)
            for j in range(len(instructors)):
                # print(instructors[j].get_modules_taught())
                instructor_modules = instructors[j].get_modules_taught()
                for k in range(len(instructor_modules)):
                    if modules[i].get_id() == instructor_modules[k]:
                        new_class.set_instructor(
                            Instructor(instructors[j].get_id(), instructors[j].get_name(), instructor_modules[k]))
            self._classes.append(new_class)
        return self

    def calculate_fitness(self):
        self._type_of_conflicts = []
        self._num_of_conflicts = 0
        classes = self.get_classes()

        temp = []

        for i in range(0, len(classes)):
            # punishes any class that ends after 19:45
            if (classes[i].get_start_time().get_start_time() + classes[i].get_duration()) > 705:
                self._num_of_conflicts += 1
                temp.append('late end')

            for j in range(0, len(classes)):
                if j >= i:

                    start_i = classes[i].get_start_time().get_start_time()
                    end_i = classes[i].get_start_time().get_start_time() + classes[i].get_duration()
                    start_j = classes[j].get_start_time().get_start_time()
                    end_j = classes[j].get_start_time().get_start_time() + classes[j].get_duration()
                    day_i = classes[i].get_day().get_id()
                    day_j = classes[j].get_day().get_id()

                    if self.overlap(start_i, end_i, start_j, end_j) and day_i == day_j and classes[i].get_id() != \
                            classes[j].get_id():

                        # punishes two classes given at overlapping times in the same room
                        if classes[i].get_room().get_id() == classes[j].get_room().get_id():
                            self._num_of_conflicts += 1
                            temp.append('same room overlap')

                        # punishes two classes given at overlapping times given by the same instructor
                        if classes[i].get_instructor().get_id() == classes[j].get_instructor().get_id():
                            self._num_of_conflicts += 1
                            temp.append('same instructor overlap')


                    if classes[i].get_module().get_name() == classes[j].get_module().get_name() and classes[i].get_id() != classes[j].get_id():
                        type_i = classes[i].get_module().get_type()
                        type_j = classes[j].get_module().get_type()

                        # punishes tutorial before lecture in the week
                        if (type_i == 'L' and type_j == 'T' and day_i > day_j) or (
                                type_j == 'L' and type_i == 'T' and day_j > day_i):
                            self._num_of_conflicts += 1
                            temp.append('tut before lec in week')

                        # punishes tutorial before lecture on the day
                        if (type_i == 'L' and type_j == 'T' and start_i > start_j and day_i == day_j) or (
                                type_j == 'L' and type_i == 'T' and start_j > start_i and day_j == day_i):
                            self._num_of_conflicts += 1
                            temp.append('tut before lec on day')

                        # punishes two tutorials of the same module on the same day
                        if type_i == 'T' and type_j == 'T':
                            if day_i == day_j:
                                self._num_of_conflicts += 1
                                temp.append('two tuts same day')
        self._type_of_conflicts.append(temp)
        return 1 / (1.0 * self._num_of_conflicts + 1)

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)):
            returnValue += str(self._classes[i]) + "\n"
        # returnValue += str(self._classes[len(self._classes) - 1])
        # returnValue += ""
        return returnValue

    def overlap(self, start1, end1, start2, end2):
        """Does the range (start1, end1) overlap with (start2, end2)?"""
        # from https://nedbatchelder.com/blog/201310/range_overlap_in_two_compares.html
        return end1 >= start2 and end2 >= start1

# data = Data()
# schedule = Schedule(data)
# schedule.initialize()
# schedule.calculate_fitness()
# print(schedule.__str__())
