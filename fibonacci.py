import time
#An iterator is a data structure for storing infinite data. 
class FiboIter():
    #Class constructor
    def __init__(self, max=None):
        self.max = max       

    def __iter__(self):
    #The iter method is used to have elements or attributes that will be needed for the iterator to work.
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
    #The next method is the one needed to have the next function in Python.
    #This method allows you to extract each of the iterator elements.   
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if  not self.max or self.counter <= self.max:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration
        

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.3)