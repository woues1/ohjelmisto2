class House:
    def __init__(self, top_floor, bottom_floor, number_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        self.add_elevator()

    def add_elevator(self):
        for i in range(1, self.number_of_elevators+1):
            self.elevators.append(Elevator(self.top_floor, self.bottom_floor, i))

    def move_elevators(self, elevator_number, floor):
        try:
            self.elevators[elevator_number-1].move_to_floor(floor)
        except IndexError:
            print("Elevator does not exist")


class Elevator:
    def __init__(self, top_floor, bottom_floor, elevator_number):
        self.elevator_number = elevator_number
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor = bottom_floor

    def move_to_floor(self, floor):
        if self.top_floor < floor or self.bottom_floor > floor:
            return print("Floor does not exist")
        if self.floor < floor:
            for i in range(self.floor, floor+1):
                self.floor = i
                print(f"Elevator: {self.elevator_number} | current floor: {self.floor}\n")

        elif self.floor > floor:
            for i in range(self.floor, floor - 1, -1):
                self.floor = i
                print(f"Elevator: {self.elevator_number} | current floor: {self.floor}\n")

        else:
            return print("Elevator is already at this floor")

house = House(10, 0, 3)
house.move_elevators(3, 5)
house.move_elevators(1, 1)
house.move_elevators(4, 10)
house.move_elevators(1, 20)