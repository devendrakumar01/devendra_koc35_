class Table:
    def __init__(self):
        self.a=int(input("enter up to which you want table : \n"))
    def multi (self):
            for i in range (1,self.a+1):
                    for j in range(1,11):
                        print(i,"*",j,"=",i*j)
                        j+=1
                    i+=1
                    print("**********")
ob1=Table()
ob1.multi()
                        
