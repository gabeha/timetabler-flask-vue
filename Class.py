class Class:
    """A Class is a teaching event, i.e. either a lecture, tutorial or a practical"""
    def __init__(self, id, module, duration):
        self._id = id
        self._module = module
        self._instructor = None
        self._start_time = None
        self._duration = duration
        self._day = None
        self._room = None

    def get_id(self): return self._id

    def get_module(self): return self._module

    def get_instructor(self): return self._instructor

    def get_start_time(self): return self._start_time

    def get_duration(self): return self._duration

    def get_day(self): return self._day

    def get_room(self): return self._room

    def set_instructor(self, instructor): self._instructor = instructor

    def set_start_time(self, start_time): self._start_time = start_time

    def set_day(self, day): self._day = day

    def set_room(self, room): self._room = room

    def __str__(self):
        return str(
            str(self._module.get_name()) + "," +
            str(self._room.get_name()) + "," +
            str(self._instructor.get_id()) + "," +
            str(self._instructor.get_name()) + "," +
            str(self._start_time.get_start_time()) + "," +
            str(self._duration) + "," +
            str(self._day.get_day())
        )

#%%
