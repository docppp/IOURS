
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LoaderBase(metaclass=Singleton):
    def __init__(self, file="iou.txt"):
        self.file_path = file
        self.file_content = None
        self.getters = []
        self._raw_lines = {}
        print("Base created", id(self))

    def loadFile(self):
        print("I am base", id(self), "loading")
        with open(self.file_path) as file:
            self.file_content = file.readlines()

    def reload(self):
        print("I am base", id(self), "called reload")
        self.loadFile()
        for call in self.getters:
            getattr(self, call)()

    def _getRawLine(self, line: str, delim='\t') -> list[str]:
        return self.file_content[self._raw_lines[line]].split(delim)
