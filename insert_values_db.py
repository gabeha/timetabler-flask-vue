import json
import sqlite3
import collections

def insert_modules():
    courses = ['BIO2003', 'CHE2001', 'INT1003', 'INT3010', 'HUM2051', 'BIO2005', 'BIO2010',
               'MAT2008', 'MAT2006', 'PHY3005', 'BIO2007', 'CHE1101', 'INT2010', 'NEU1001',
               'PHY2002', 'BIO2001', 'CHE3009', 'INT3003', 'PHY2008', 'PHY3008', 'SCI2031',
               'BIO3010', 'INT3008', 'INT1007', 'PHY1101', 'PHY2004', 'PRA1101', 'PRA1005',
               'PRA2002', 'PRA2008', 'PRA2011', 'PRA2014', 'PRA2022', 'PRA3012', 'PRA3014',
               'PRA3017', 'PRA3020', 'PRA3024']

    types = ['L', 'T', 'T']
    modules = []

    for i in range(len(courses)):
        for j in range(3):
            level = 0
            if courses[i][3] == '1':
                level = 1000
            elif courses[i][3] == '2':
                level = 2000
            elif courses[i][3] == '3':
                level = 3000

            if courses[i][0:3] != 'PRA':
                temp = [types[j], courses[i], level, 6]
                modules.append(temp)

        if courses[i][0:3] == 'PRA':
            level = 0
            if courses[i][3] == '1':
                level = 1000
            elif courses[i][3] == '2':
                level = 2000
            elif courses[i][3] == '3':
                level = 3000
            temp = ['P', courses[i], level, 28]
            modules.append(temp)

    cur.execute("DROP TABLE IF EXISTS modules")
    cur.execute("CREATE TABLE modules (id integer primary key, type text, name text, level int, duration int)")

    for i in range(len(modules)):
        cur.execute("INSERT INTO modules (type, name, level, duration) VALUES (?,?,?,?)",
                    (modules[i][0], modules[i][1], modules[i][2], modules[i][3]))

def insert_instructors():

    cur.execute("DROP TABLE IF EXISTS instructors")
    instructors = [
        ['Jessica Nelson', json.dumps([1, 2, 3, 83])],
        ['Hanne Dilien', json.dumps([4, 5, 6, 81])],
        ['Federico De Martino', json.dumps([7, 8, 9])],
        ['Vivian van Saaze', json.dumps([10, 11, 12])],
        ['Patricia de Vries', json.dumps([13, 14, 15])],
        ['Linnea van Griethuijsen', json.dumps([16, 17, 18])],
        ['Aaron Isaacs', json.dumps([19, 20, 21])],
        ['Claire Blackman', json.dumps([22, 23, 24, 73, 74, 75])],
        ['Otti dHuys', json.dumps([25, 26, 27])],
        ['Stefan Danilishin', json.dumps([28, 29, 30])],
        ['Leon de Windt', json.dumps([31, 32, 33])],
        ['Chris Bahn', json.dumps([34, 35, 36, 87])],
        ['Ian Anthony', json.dumps([37, 38, 39])],
        ['Laurence de Nijs', json.dumps([40, 41, 42])],
        ['Jessica Steinlechner', json.dumps([43, 44, 45])],
        ['Martijn van Griensven', json.dumps([46, 47, 48, 88])],
        ['Giuditta Perversi', json.dumps([49, 50, 51, 89])],
        ['Carlos Mota', json.dumps([52, 53, 54])],
        ['Chad Ellington', json.dumps([55, 56, 57])],
        ['Lorenzo Reverberi', json.dumps([58, 59, 60])],
        ['K. Wouters', json.dumps([61, 62, 63])],
        ['Maarten Honing', json.dumps([64, 65, 66])],
        ['Lorenzo Moroni', json.dumps([67, 68, 69])],
        ['Jesse Hennekam', json.dumps([70, 71, 72])],
        ['Benedikt Poser', json.dumps([76, 77, 78])],
        ['Chris Pawley', json.dumps([79])],
        ['Mark Roberts', json.dumps([80])],
        ['Slava Vieru', json.dumps([82])],
        ['Serve Olieslagers', json.dumps([84])],
        ['Pim Martens', json.dumps([85])],
        ['Bart van Grinsven', json.dumps([86])],
        ['Jacco de Vries', json.dumps([90])],
    ]
    cur.execute("CREATE TABLE instructors (id integer primary key, name text, modules_taught text)")

    for i in range(len(instructors)):
        cur.execute("INSERT INTO instructors (name, modules_taught) VALUES (?,?)",
                    (instructors[i][0], instructors[i][1]))


def insert_rooms():
    rooms = [
        [1, 'B.001', 50],
        [2, 'B.002', 50],
        [3, 'B.003', 50],
        [4, 'B.004', 50],
        [5, 'B.005', 50],
        [6, 'B.006', 50],
        [7, 'B.007', 50],
        [8, 'B.008', 50],
        [9, 'B.009', 50],
        [10, 'B.010', 50],
        [11, 'B.011', 50],
        [12, 'B.012', 50],
        [13, 'B.013', 50],
        [14, 'B.014', 50],
        [15, 'B.015', 50],
        [16, 'B.016', 50],
        [17, 'B.017', 50],
        [18, 'B.018', 50],
        [19, 'B.019', 50],
        [20, 'B.020', 50],
        [21, 'B.021', 50],
        [22, 'B.022', 50],
        [23, 'B.023', 50],
        [24, 'B.024', 50],
        [25, 'B.025', 50],
        [26, 'B.026', 50],
        [27, 'B.027', 50],
        [28, 'B.028', 50],
        [29, 'B.029', 50],
        [30, 'B.030', 50],
    ]

    cur.execute("DROP TABLE IF EXISTS rooms")
    cur.execute("CREATE TABLE rooms (id integer, name text, capacity integer)")

    for i in range(len(rooms)):
        cur.execute("INSERT INTO rooms (id, name, capacity) VALUES (?,?,?)",
                    (rooms[i][0], rooms[i][1], rooms[i][2]))


def insert_start_times():
    start_times = []
    for i in range(42):  # last start time is 18:30
        start_times.append([i + 1, i * 15])

    cur.execute("DROP TABLE IF EXISTS start_times")
    cur.execute("CREATE TABLE start_times (id integer, start_time integer)")

    for i in range(len(start_times)):
        cur.execute("INSERT INTO start_times (id, start_time) VALUES (?,?)",
                    (start_times[i][0], start_times[i][1]))


def insert_days():
    days = [
        [1, 'Mon'],
        [2, 'Tue'],
        [3, 'Wed'],
        [4, 'Thu'],
        [5, 'Fri']
    ]

    cur.execute("DROP TABLE IF EXISTS days")
    cur.execute("CREATE TABLE days (id integer, day text)")

    for i in range(len(days)):
        cur.execute("INSERT INTO days (id, day) VALUES (?,?)",
                    (days[i][0], days[i][1]))


def insert_schedules(schedule):

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS schedules")
    cur.execute(
        "CREATE TABLE schedules (course_title text, course_id integer, course_type text, room_name text, room_id integer, "
        "instructor_name text, instructor_id integer, start_time integer, start_time_id integer, duration integer, "
        "day_name text, day_id integer)")

    classes = schedule.get_classes()
    objects_list = []

    for i in range(len(classes)):
        course_title = classes[i].get_module().get_name()
        course_id = classes[i].get_module().get_id()
        course_type = classes[i].get_module().get_type()

        room_name = classes[i].get_room().get_name()
        room_id = classes[i].get_room().get_id()

        instructor_name = classes[i].get_instructor().get_name()
        instructor_id = classes[i].get_instructor().get_id()

        start_time = classes[i].get_start_time().get_start_time()
        start_time_id = classes[i].get_start_time().get_id()

        duration = classes[i].get_duration()

        day_name = classes[i].get_day().get_day()
        day_id = classes[i].get_day().get_id()

        cur.execute(
            "INSERT INTO schedules (course_title, course_id, course_type, room_name, room_id, instructor_name, instructor_id, "
            "start_time, start_time_id, duration, day_name, day_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (course_title, course_id, course_type, room_name, room_id, instructor_name, instructor_id, start_time,
             start_time_id,
             duration, day_name, day_id))

        d = collections.OrderedDict()
        d['course_title'] = course_title
        d['course_id'] = course_id
        d['course_type'] = course_type
        d['room_name'] = room_name
        d['room_id'] = room_id
        d['instructor_name'] = instructor_name
        d['instructor_id'] = instructor_id
        d['start_time'] = start_time
        d['start_time_id'] = start_time_id
        d['duration'] = duration
        d['day_name'] = day_name
        d['day_id'] = day_id
        objects_list.append(d)

        conn.commit()

    j = json.dumps(objects_list)
    with open('optimal_schedule.json', 'w') as f:
        f.write(j)

def get_modules():
    # returns all modules
    cur.execute("SELECT * FROM modules")
    fetched_modules = cur.fetchall()
    type_adjusted_modules = []
    for m in fetched_modules:
        type_adjusted_modules.append([m[0], m[1], m[2], m[3], json.loads(m[4])])
    return type_adjusted_modules


def get_instructors():
    # returns all instructors
    cur.execute("SELECT * FROM instructors")
    fetched_instructors = cur.fetchall()
    type_adjusted_instructors = []
    for i in fetched_instructors:
        type_adjusted_instructors.append([i[0], i[1], json.loads(i[2])])
    return type_adjusted_instructors


def get_rooms():
    # returns all rooms
    cur.execute("SELECT * FROM rooms")
    fetched_rooms = cur.fetchall()
    return fetched_rooms


def get_module_via_module_id(id):
    # returns one module that corresponds to the given id
    cur.execute("SELECT * FROM modules WHERE id = ?", (id,))
    fetched_modules = cur.fetchall()
    return fetched_modules


def get_module_via_instructor_id(id):
    # returns all modules that a given instructor identified by their id teaches
    cur.execute("SELECT * FROM instructors WHERE id = ?", (id,))
    fetched_instructors = cur.fetchall()
    modules_per_instructor = []
    for i in fetched_instructors:
        for m in json.loads(i[2]):
            modules_per_instructor.append(get_module_via_module_id(m))
    return modules_per_instructor


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    insert_modules()
    insert_instructors()
    insert_rooms()
    insert_start_times()
    insert_days()
    # insert_schedules()

    conn.commit()
