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

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            self.elevators[i].move_to_floor(self.bottom_floor)


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
            for i in range(self.floor, floor):
                self.floor_up()
                print(f"Elevator: {self.elevator_number} | current floor: {self.floor}\n")

        elif self.floor > floor:
            for i in range(self.floor, floor, -1):
                self.floor_down()
                print(f"Elevator: {self.elevator_number} | current floor: {self.floor}\n")

        else:
            return print("Elevator is already at this floor")

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1

h_top_floor = int(input("House top floor: "))
h_bottom_floor = int(input("House bottom floor: "))
elevator_number = int(input("Number of elevators: "))
house = House(h_top_floor, h_bottom_floor, elevator_number)

while True:
    elevator_number = input("Choose an elevator: ")
    target_floor = input("Choose a target floor: ")
    if elevator_number == "-1" or target_floor == "-1":
        break
    elif elevator_number == "Alarm" or target_floor == "Alarm":
        house.fire_alarm()
    else:
        house.move_elevators(int(elevator_number), int(target_floor))