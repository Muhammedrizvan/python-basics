#stopiteration
#stop after 20 th iterations ?
from logging.config import stopListening


class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = mynumber()
myobject = iter(myclass)

for x in myobject:
    print(x)
