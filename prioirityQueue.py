class PriorityQueue():
    def __init__(self,array):
        self.array = array
        self.buildHeap()
    def buildHeap(self):
        mid = len(self.array)//2
        for i in range(mid,-1,-1):
            self.shiftDown(i)
    def shiftDown(self,i):
        maxI = i
        left = i * 2 + 1
        if((left>0 and left<len(self.array))):
            if(self.array[left] > self.array[maxI]):
                maxI = left
        right = i * 2 + 2
        if((right>0 and right<len(self.array))):
            if(self.array[right] > self.array[maxI]):
                maxI = right
        if(maxI != i):
            self.array[maxI],self.array[i] = self.array[i],self.array[maxI]
            self.shiftDown(maxI)
    def shiftUp(self,i):
        if(i>0):
            parent = i // 2
            if(i == 2):
                parent = 0
            if((parent>=0 and parent<len(self.array))):
                if(self.array[parent]<self.array[i]):
                    self.array[parent],self.array[i] = self.array[i],self.array[parent]
                    self.shiftUp(parent)
    def extractMax(self):
        prior = self.array[0]
        self.array[0] = self.array.pop(len(self.array)-1)
        self.shiftDown(0)
        return prior
    def addNew(self,value):
        self.array.append(value)
        self.shiftUp(len(self.array)-1)
    def getElement(self,element):
        if(element in self.array):
            ind = self.array.index(element)
            self.array[ind] = 9999999
            self.shiftUp(ind)
            self.extractMax()
            return ind
        else:
            return -1
    def changePriority(self,element):
        if(element in self.array):
            value = int(input("Enter the Value to which Element priority Should be Changed:"))
            ind  = self.array.index(element)
            self.array[ind] = value
            if(value > element):
                self.shiftUp(ind)
            else:
                self.shiftDown(ind)
    def printQueue(self):
        print(self.array)
priorityQueue = PriorityQueue(array = [1,2,5,8,9,3])
print("Building PriorityQueue with Sample Data:[1,2,5,8,9,3]")
print("Generated Binary(Max) Heap")
priorityQueue.printQueue()
print("Select One of the Operation to be performed on Queue")
while(True):
    print("1: Insert 2: Extract Max 3:PrintQueue 4:ChangePriority 5:GetElement 6:Exit")
    user_input  = int(input())
    if(user_input == 1):
        priorityQueue.addNew(int(input("Please Enter the Value to Be Inserted:")))
    elif(user_input == 2):
        print(priorityQueue.extractMax())
    elif(user_input == 3):
        priorityQueue.printQueue()
    elif(user_input == 4):
        priorityQueue.changePriority(int(input("Enter the Element to change Priority:")))
    elif(user_input == 5):
        print(f'Element Found at Index:{priorityQueue.getElement(int(input("Enter the Element to be Fetched:")))}',end='\n')
    else:
        break