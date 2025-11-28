#initiate a clss
class employee:
    #special method/magic method/dunder method -- constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

        #clasee ke under koi function method kahlata hain
    def travel(self, destination):
        print("this travel method was called manually")
        print(f"employee is travelling to {destination}") 

sam = employee()         


#hence special method is itself get called automatically when we simpley just create an object
#but in order to print the line(        print("this travel fun was called manually")
#>>we need to call fun by this type like>> sam.travel("surat")
