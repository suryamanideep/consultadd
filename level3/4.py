class Shape:
    def __init__(self):
        pass 

    def area(self):
        return 0 


class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length  

    def area(self):
        return self.length ** 2  


if __name__ == "__main__":

    shape = Shape()
    print(f"Area of shape: {shape.area()}") 

    square = Square(4)
    print(f"Area of square: {square.area()}")  
