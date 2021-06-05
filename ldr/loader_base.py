
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


_global_base = None


class LoaderBase(metaclass=Singleton):

    def __new__(cls, *args, **kwargs):
        global _global_base
        if _global_base is None:
            _global_base = super(LoaderBase, cls).__new__(cls, *args, **kwargs)
        return _global_base

    def __init__(self):
        self.file_path = None
        self.file_content = None
        self.getters = []
        self._raw_lines = {}

    def loadFile(self, file="iou.txt"):
        self.file_path = file
        with open(self.file_path) as file:
            self.file_content = file.readlines()

    def reload(self):
        self.loadFile()
        for call in self.getters:
            getattr(self, call)()

    def _getRawLine(self, line: str, delim='\t') -> list[str]:
        return self.file_content[self._raw_lines[line]].split(delim)
