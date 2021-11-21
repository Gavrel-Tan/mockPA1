# Q2
class Vehicle:
    pass


# Q3
class Vehicle:
    engine_capacity = "1,6 Turbo"


# Q4
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.");


# Q5
vios = Vehicle('4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)
# Q6
vios.drive()


# Q7
class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)


# Q8
blueSG = ElectricCar('4', 5, 150)
blueSG.drive()


# Q10 Challenge. Create another class named Computer and subclass laptop and desktop with the function
# playGame(<Parameter: Name of Game>).
class Computer:
    def __init__(self, name_of_game):
        self.name_of_game = name_of_game

    def play(self):
        print("The computer is running")


mario = Computer("mario")
mario.play()
# Additional Challenge Q11


