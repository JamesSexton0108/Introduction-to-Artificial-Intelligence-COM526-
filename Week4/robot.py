from agent import Agent
import utils
import random
import heapq


class Robot(Agent):

    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.water_level = 0
        self.water_station_location = None
        self.known_map = None

    def initialise_map(self, environment):
        if self.known_map is not None:
            return

        rows = len(environment.world)
        cols = len(environment.world[0])
        self.known_map = [["?" for _ in range(cols)] for _ in range(rows)]

        x, y = self.position
        self.known_map[y][x] = " "

    def update_map(self, percept, environment):
        x, y = self.position
        self.known_map[y][x] = " "

        for (nx, ny), space in percept.items():
            if space == " ":
                self.known_map[ny][nx] = " "
            elif space == "x":
                self.known_map[ny][nx] = "x"
            elif utils.is_flame(space):
                self.known_map[ny][nx] = "*"
            elif utils.is_water_station(space):
                self.known_map[ny][nx] = "s"
                self.water_station_location = (nx, ny)


    def decide(self, percept: dict[tuple[int, int], ...]):
        free_spaces = []
        fire_spaces = []

        for k,v in percept.items():
            if v == " ":
                free_spaces.append(k)
            elif utils.is_flame(v):
                fire_spaces.append(k)
            elif utils.is_water_station(v):
                self.water_station_location = k

        if fire_spaces and self.water_level >= 5:
            return "spray", random.choice(fire_spaces), None

        if self.water_level < 5 and self.water_station_location is not None:
            return "refill", self.water_station_location, None

        if free_spaces:
            return "move", random.choice(free_spaces), None

        return "stay", None, None

    def act(self, environment):
        cell = self.sense(environment)

        decision,target,x = self.decide(cell)
        if decision == "move":
            self.move(environment, target)
        elif decision == "spray":
            self.spray(environment, target)
        elif decision == "refill":
            self.move_to_station(environment, target)

        self.initialise_map(environment)
        self.update_map(cell, environment)

    def move(self, environment, to):
        if environment.move_to(self.position, to):
            self.position = to

    def spray(self, environment, target):
        self.water_level -= 5
        fx, fy = target
        environment.world[fy][fx] = " "

    def check_station(self):
        if self.water_station_location is None:
            return None
        wx, wy = self.water_station_location
        possible_spaces = [(wx, wy-1), (wx+1, wy), (wx, wy+1), (wx-1, wy)]
        available_spaces = []

        for x, y in possible_spaces:
            if self.known_map[y][x] == " ":
                available_spaces.append((x, y))

        if len(available_spaces) == 0:
            return None

        available_spaces.sort(key=lambda p: self.calc_distance(self.position,p))

        return available_spaces[0]

    def move_to_station(self, environment, target):
        target = self.check_station()
        if target is None:
            return

        path = self.calc_path(self.position, target, None)
        if path and len(path) >= 2:
            self.move(environment, path[1])
            sx, sy = self.position
            self.known_map[sy][sx] = " "
            print("moving using a*!")

    def refill(self):
        self.water_level = 100


    def __str__(self):
        return '🚒'

    # MANHATTAN DISTANCE FUNCTIONS
    def calc_path(self, start, goal, avoid):
        p_queue = []
        heapq.heappush(p_queue, (0, start))

        directions = {
            "right": (-1, 0),
            "left": (0, 1),
            "up": (1, 0),
            "down": (0, -1)
        }
        predecessors = {start: None}
        g_values = {start: 0}

        while len(p_queue) != 0:
            current_cell = heapq.heappop(p_queue)[1]
            if current_cell == goal:
                return self.get_path(predecessors, start, goal)
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = directions[direction]
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

                if self.viable_move(neighbour[0], neighbour[1], avoid) and neighbour not in g_values:
                    cost = g_values[current_cell] + 1
                    g_values[neighbour] = cost
                    f_value = cost + self.calc_distance(goal, neighbour)
                    heapq.heappush(p_queue, (f_value, neighbour))
                    predecessors[neighbour] = current_cell

        return None

    def get_path(self, predecessors, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = predecessors[current]
        path.append(start)
        path.reverse()
        return path

    def viable_move(self, x, y, types):
        # You will need to do this one
        # Do not move in to a cell containing an obstacle (represented by 'x')
        # Do not move in to a cell containing a flame
        # Do not move in to a cell containing a water station
        # Do not move in to a cell containing a robot.
        # In fact, the only valid cells are blank ones
        # Also, do not go out of bounds.
        if self.known_map[y][x] == " ":
            return True
        else:
            return False

    def calc_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    # END OF MANHATTAN DISTANCE FUNCTIONS
