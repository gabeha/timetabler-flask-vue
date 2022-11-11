import json
import sqlite3
import collections

def insert_modules():
    course = [6, 4, 4]
    practical = [28]
    course_duration = json.dumps(course)
    practical_duration = json.dumps(practical)
    modules = [
        [1, 'L', 'PHY3002', 3000, 6],
        [2, 'T', 'PHY3002', 3000, 6],
        [3, 'T', 'PHY3002', 3000, 6],
        [4, 'L', 'PHY3006', 1000, 6],
        [5, 'T', 'PHY3006', 1000, 6],
        [6, 'T', 'PHY3006', 1000, 6],
        [7, 'L', 'PHY3007', 1000, 6],
        [8, 'T', 'PHY3007', 1000, 6],
        [9, 'T', 'PHY3007', 1000, 6],

        [10, 'L', 'BIO2003', 2000, 6],
        [11, 'T', 'BIO2003', 2000, 6],
        [12, 'T', 'BIO2003', 2000, 6],
        [13, 'L', 'BIO3007', 3000, 6],
        [14, 'T', 'BIO3007', 3000, 6],
        [15, 'T', 'BIO3007', 3000, 6],
        [16, 'P', 'PRA2011', 2000, 28],
        [17, 'P', 'PRA3011', 2000, 28],

        [18, 'L', 'CHE2003', 2000, 6],
        [19, 'T', 'CHE2003', 2000, 6],
        [20, 'T', 'CHE2003', 2000, 6],
        [21, 'L', 'CHE3006', 3000, 6],
        [22, 'T', 'CHE3006', 3000, 6],
        [23, 'T', 'CHE3006', 3000, 6],
        [24, 'L', 'CHE3007', 3000, 6],
        [25, 'T', 'CHE3007', 3000, 6],
        [26, 'T', 'CHE3007', 3000, 6],
        [27, 'P', 'PRA2008', 2000, 28],
        [28, 'P', 'PRA3018', 3000, 28],
    ]
    cur.execute("DROP TABLE IF EXISTS modules")
    cur.execute("CREATE TABLE modules (id integer, type text, name text, level int, duration int)")

    for i in range(len(modules)):
        cur.execute("INSERT INTO modules (id, type, name, level, duration) VALUES (?,?,?,?,?)",
                    (modules[i][0], modules[i][1], modules[i][2], modules[i][3], modules[i][4]))


def insert_instructors():
    instructors = [
        [1, 'Gideon Koekok', json.dumps([1, 2, 3, 4, 5, 6, 7, 8, 9])],
        # [1, 'Gideon Koekok', json.dumps([1, 2, 3])],
        [2, 'Roy Erkens', json.dumps([10, 11, 12, 13, 14, 15, 16, 17])],
        # [2, 'Roy Erkens', json.dumps([10, 11, 12])],
        [3, 'Veaceslav Vieru', json.dumps([18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])]
        # [3, 'Veaceslav Vieru', json.dumps([18, 19, 20])]
    ]

    cur.execute("DROP TABLE IF EXISTS instructors")
    cur.execute("CREATE TABLE instructors (id integer, name text, modules_taught text)")

    for i in range(len(instructors)):
        cur.execute("INSERT INTO instructors (id, name, modules_taught) VALUES (?,?,?)",
                    (instructors[i][0], instructors[i][1], instructors[i][2]))


def insert_rooms():
    rooms = [
        [1, 'B.001', 50],
        [2, 'B.002', 50],
        [3, 'B.003', 50],
        [4, 'B.004', 50],
        [5, 'B.005', 50],
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
