from datetime import datetime

class Tarea1:
    def compareStrings(self, a, b):
        if type(a) == type(b) and type(b) == str:
            if len(a) < len(b):
                self.log(self.logFile, "B is bigger\n")
                return b
            else:
                self.log(self.logFile, "A is bigger\n")
                return a
        else:
            self.log(self.logFile, "[E]One of the arguments is not a string.\n")

    def log(self, name, text):
        i = open(name, "a+")
        i.write(datetime.today().ctime()+ " "+ text)

    def __init__(self, logFile):
        self.logFile = logFile
        self.log(logFile, "=====NEW INSTANCE=====")


# Iniciar
T = Tarea1("log.txt")

# Caso 1
print("Caso 1")
print("String A: ")
a = input()
print("String B: ")
b = input()

T.compareStrings(a,b)

# Caso 2
print("Caso 2")
print("String A: ")
a = input()
print("String B: ")
b = input()

T.compareStrings(a,b)

# Caso 3
print("Caso 3")
print("String A: ")
a = input()
print("String B: ")
b = input()

T.compareStrings(a,b)

# Caso 4
print("Caso 4")
T.compareStrings([1,2,3,4],"a")