#initiate a clss
class employee:
    #special method/magic method/dunder method -- constructor
    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation = "SDE"

        #clasee ke under koi function method kahlata hain
    def travel(self, destination):
        print(f"employee is travelling to {destination}")    


#creating an object/instance of the class

sam = employee()
print(sam.salary) 
sam.travel("delhi")       