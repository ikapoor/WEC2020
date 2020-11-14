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
    output = Output()

    output.addRobot("Jerry", [1, 1])
    output.addAction("Jerry", "move", [1, 2])

    output.writeJSON("output.json")
