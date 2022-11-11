class Room:
    def __init__(self, id, name, capacity):
        self._id = id
        self._name = name
        self._capacity = capacity

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_capacity(self):
        return self._capacity
