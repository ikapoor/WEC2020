import json

class Output:

    def __init__(self):
        self.robots = []
        self.actions = []

    def addRobot(self, name, coordinates):
        self.robots.append([name, coordinates])

    def addAction(self, name, type, parameters):
        self.actions.append([name, type, parameters])

    def writeJSON(self, filepath):
        output_dict = {
            "robots": self.robots,
            "actions": self.actions,
        }
        with open(filepath, 'w') as file:
            json.dump(output_dict, file)

if __name__ == '__main__':

    # Initialize variables
    fluid_capacity = 0
    fuel_capacity = 0
    row_count = 4
    col_count = 7
    grid = []
    file = open("test_cases/case1.txt")
    lines = file.readlines()
    for i, line in enumerate(lines):
        data = line.split(' ')
        if i == 0:
            fluid_capacity = data[0].strip()
            fuel_capacity = data[1].strip()
        elif i == 1:
            row_count = data[0].strip() 
            col_count = data[1].strip()
        else:
            row = [value.strip() for value in data]
            grid.append(row)
    file.close()

    output = Output()
    output.addRobot("Jerry", [1, 1])
    output.addAction("Jerry", "move", [1, 2])

    output.writeJSON("output.json")
