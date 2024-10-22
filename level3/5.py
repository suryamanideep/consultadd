class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
        self.normalize_time()  

    def normalize_time(self):
        """ Normalize the time to ensure minutes are less than 60. """
        if self.minutes >= 60:
            self.hours += self.minutes // 60  
            self.minutes = self.minutes % 60   

    def addTime(self, other):
        """ Add two Time objects and return a new Time object. """
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        return Time(total_hours, total_minutes)

    def displayTime(self):
        """ Print the time in hours and minutes format. """
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        """ Display the total time in minutes. """
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes} min")

if __name__ == "__main__":
    time1 = Time(2, 50)
    time2 = Time(1, 20)

    result_time = time1.addTime(time2)
    #print(f"({time1}) + ({time2}) = ({result_time})")
    print("Result of adding time:")
    result_time.displayTime()

    result_time.displayMinute()
