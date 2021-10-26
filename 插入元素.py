class MyArray:
    def __init__(self,capacity):
        self.array=[None]*capacity
        self.size=0


    def insert(self,index,element):
        if index<0 or index> self.size:
            #判断访问下表是否超出范围
            raise  Exception("超出数组实际元素范围")
        #从右往左循环，每个元素向右挪一位置
        for  i in range(self.size-1,-1,-1):
            self.array[i+1]=self.array[i]
            #腾出位置放入新元素
            self.array[index]=element
            self.size+=1

    def output(self):
        for i in range(self.size):
            print(self.array[i])





array=MyArray(4)
array.insert_v2(0,10)
array.insert_v2(0,11)


array.output()