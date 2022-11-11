import json
import sqlite3 as sql

from Instructor import Instructor
from Module import Module
from Room import Room
from StartTime import StartTime
from Day import Day


class Data:
    def __init__(self):
        self._conn = sql.connect('test.db')
        self._cur = self._conn.cursor()

        self._modules = self.select_modules()
        self._rooms = self.select_rooms()
        self._start_times = self.select_start_times()
        self._days = self.select_days()
        self._instructors = self.select_instructors()
        self._numberOfClasses = len(self._modules)

    def select_modules(self):
        # returns all modules
        self._cur.execute("SELECT * FROM modules")
        fetched_modules = self._cur.fetchall()
        return_modules = []
        for i in range(len(fetched_modules)):
            return_modules.append(
                Module(
                    fetched_modules[i][0],
                    fetched_modules[i][1],
                    fetched_modules[i][2],
                    fetched_modules[i][3],
                    fetched_modules[i][4],
                ))
        return return_modules

    def select_instructors(self):
        # returns all instructors
        self._cur.execute("SELECT * FROM instructors")
        fetched_instructors = self._cur.fetchall()
        type_adjusted_instructors = []
        return_instructors = []
        for i in fetched_instructors:
            type_adjusted_instructors.append([i[0], i[1], json.loads(i[2])])
        for i in range(len(type_adjusted_instructors)):
            return_instructors.append(
                Instructor(
                    type_adjusted_instructors[i][0],
                    type_adjusted_instructors[i][1],
                    type_adjusted_instructors[i][2],
                )
            )
        return return_instructors

    def select_rooms(self):
        # returns all rooms
        self._cur.execute("SELECT * FROM rooms")
        rooms = self._cur.fetchall()
        return_rooms = []
        for i in range(len(rooms)):
            return_rooms.append(Room(rooms[i][0], rooms[i][1], rooms[i][2]))
        return return_rooms

    def select_start_times(self):
        self._cur.execute("SELECT * FROM start_times")
        times = self._cur.fetchall()
        return_times = []
        for i in range(len(times)):
            return_times.append(StartTime(times[i][0], times[i][1]))
        return return_times

    def select_days(self):
        self._cur.execute("SELECT * FROM days")
        days = self._cur.fetchall()
        return_days = []
        for i in range(len(days)):
            return_days.append(Day(days[i][0], days[i][1]))
        return return_days

    def get_rooms(self):
        return self._rooms

    def get_start_times(self):
        return self._start_times

    def get_days(self):
        return self._days

    def get_modules(self):
        return self._modules

    def get_instructors(self):
        return self._instructors



