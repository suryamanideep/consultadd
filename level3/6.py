# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Multiple Inheritance
class Canine:
    def bark(self):
        return "Barking!"

class Pet:
    def play(self):
        return "Playing!"

class Dog2(Canine, Pet):
    def fetch(self):
        return "Fetching the ball!"

# Multilevel Inheritance
class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog3(Animal2):
    def speak(self):
        return f"{self.name} says Woof!"

class Puppy(Dog3):
    def speak(self):
        return f"{self.name} says Yip!"

# Example usage
if __name__ == "__main__":
    # Single Inheritance
    dog = Dog("Buddy")
    print(dog.speak())  # Output: Buddy says Woof!

    # Multiple Inheritance
    dog2 = Dog2()
    print(dog2.bark())   # Output: Barking!
    print(dog2.play())   # Output: Playing!
    print(dog2.fetch())  # Output: Fetching the ball!

    # Multilevel Inheritance
    puppy = Puppy("Max")
    print(puppy.speak())  # Output: Max says Yip!