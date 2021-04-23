class Robot:
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety
        print("Robot")

    def get_info(self):
        return "{} is a {} robot".format(self.name, self.variety)


class ServiceRobot(Robot):
    def __init__(self, name):
        super().__init__(name, variety='service')
        self.name = name


chappi = ServiceRobot("Chappi")
print(chappi.get_info())
