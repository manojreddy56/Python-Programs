class Demo:
    def __init__(self): 
        self.x = 1

    def change(self):
        self.x = 10

class Demo_derived (Demo):
    def change(self):
        self.x=self.x+1
        return self.x

def main():
    obj = Demo_derived()
    print(obj.change())

main()