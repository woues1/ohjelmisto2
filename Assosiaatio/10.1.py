class elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor = bottom_floor

    def move_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            return print("Floor does not exist")

        if self.floor < floor:
            for i in range(self.floor, floor+1):
                self.floor = i
                print(f"current floor: {self.floor}\n")

        elif self.floor > floor:
            for i in range(self.floor, floor - 1, -1):
                self.floor = i
                print(f"current floor: {self.floor}\n")

        else:
            return print("Elevator is already at this floor")

h = elevator(10, 0)
h.move_to_floor(5)
h.move_to_floor(2)