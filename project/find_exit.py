import random, math
from threading import Lock
i=j=0
class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class FindExit(metaclass=SingletonMeta):
    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.counter = 0
        self.table = self.generate_table()


    def current_pos(self, posI=0, posJ=0):
        table_pos = self.table
        table_pos = self.generate_table()
        if posI < 0 or posJ < 0 or posJ > self.__width-1 or posI > self.__height-1:
            return "Fail"
        elif table_pos[posI][posJ] == 999:
            return "Congratulation"
        else:
            table_pos[posI][posJ] = 1
            self.table = table_pos
            return self.table

    def generate_table(self):
        global i,j
        table = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        #i = math.floor(self.__esc/self.__height)
        #j = abs(i * self.__width - self.__esc) - 1
        #print(i, j, self.__height, self.__width)
        if self.counter == 0:
            i = random.randint(0,self.__height-1)
            j = random.randint(0,self.__width-1)
        table[i][j] = 999
        return table