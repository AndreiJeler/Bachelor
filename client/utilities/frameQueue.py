class FrameQueue:
    def __init__(self, capacity=10):
        self.__len = 0
        self.__capacity = capacity
        self.__elems = []

    def pop(self):
        '''
        Remove the first element of the queue
        '''
        self.__elems.pop(0)

    def insert(self, elem):
        '''
        Insert an element and removes the first if the max capacity is reached
        :param elem: The element to be added
        :return: True if the max capacity was reached or False otherwise
        '''
        self.__elems.append(elem)
        self.__len += 1
        if self.__len > self.__capacity:
            self.pop()
            self.__len -= 1
            return True
        return False

    @property
    def len(self):
        return self.__len

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def elems(self):
        return self.__elems

    @elems.setter
    def elems(self, value):
        self.__elems = value
