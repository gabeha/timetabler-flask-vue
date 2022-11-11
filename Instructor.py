class Instructor:
    def __init__(self, id, name, modules_taught):
        self._id = id
        self._name = name
        self._modules_taught = modules_taught

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_modules_taught(self):
        return self._modules_taught
