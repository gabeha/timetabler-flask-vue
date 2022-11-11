class Module:
    def __init__(self, id, type, name, level, duration):
        self._id = id
        self._type = type
        self._name = name
        self._level = level
        self._duration = duration*15

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_duration(self):
        return self._duration
