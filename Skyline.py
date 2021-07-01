import random


class Skyline:
    def __init__(self):
        self.buildings = []
        self.area = 0
        self.height = 0

    def union(self, other):
        i = j = height_self = height_other = height_current = 0
        result = Skyline()
        while i < len(self.buildings) and j < len(other.buildings):
            x_self = self.buildings[i][0]
            x_other = other.buildings[j][0]
            if x_self <= x_other:
                height_self = self.buildings[i][1]
                i += 1
            if x_other <= x_self:
                height_other = other.buildings[j][1]
                j += 1
            if max(height_self, height_other) != height_current:
                height_current = max(height_self, height_other)
                result.buildings.append((min(x_self, x_other), height_current))
        result.buildings.extend(self.buildings[i:])
        result.buildings.extend(other.buildings[j:])
        self.buildings = result.buildings
        self.calculate_area()
        self.height = max(self.height, other.height)

    def right_shift(self, N):
        if N < 0:
            raise ValueError
        for i in range(len(self.buildings)):
            self.buildings[i] = (self.buildings[i][0] + N, self.buildings[i][1])

    def left_shift(self, N):
        if N < 0:
            raise ValueError
        for i in range(len(self.buildings)):
            self.buildings[i] = (self.buildings[i][0] - N, self.buildings[i][1])

    def intersection(self, other):
        i = j = height_self = height_other = height_current = 0
        result = Skyline()
        while i < len(self.buildings) and j < len(other.buildings):
            x_self = self.buildings[i][0]
            x_other = other.buildings[j][0]
            if x_self <= x_other:
                height_self = self.buildings[i][1]
                i += 1
            if x_other <= x_self:
                height_other = other.buildings[j][1]
                j += 1
            if min(height_self, height_other) != height_current:
                height_current = min(height_self, height_other)
                result.buildings.append((min(x_self, x_other), height_current))
                if result.height < height_current:
                    result.height = height_current
        self.buildings = result.buildings
        self.calculate_area()
        self.height = result.height

    def replication(self, N):
        if N < 0:
            raise ValueError
        length = len(self.buildings)
        width = self.buildings[length - 1][0] - self.buildings[0][0]
        self.buildings.pop()
        for i in range(1, N):
            if self.buildings[0][1] != self.buildings[length - 2][1]:
                self.buildings.append((self.buildings[0][0] + width*i, self.buildings[0][1]))
            for j in range(1, length - 1):
                self.buildings.append((self.buildings[j][0] + width*i, self.buildings[j][1]))
        self.buildings.append((self.buildings[0][0] + width*N, 0))
        self.area *= N

    def mirror(self):
        result = Skyline()
        offset = self.buildings[0][0] + self.buildings[len(self.buildings) - 1][0]
        for i in range(len(self.buildings) - 1):
            result.buildings.append((offset - self.buildings[len(self.buildings) - 1 - i][0], self.buildings[len(self.buildings) - 2 - i][1]))
        result.buildings.append((offset - self.buildings[0][0], 0))
        self.buildings = result.buildings

    def building(self, x_min, height, x_max):
        if x_min >= x_max or height < 0:
            raise ValueError
        self.buildings = [(x_min, height), (x_max, 0)]
        self.area = (x_max - x_min)*height
        self.height = height

    def random_rec(self, building_list, l, r):
        if r - l == 1:
            return building_list[l]
        m = (l + r)//2
        result_l = self.random_rec(building_list, l, m)
        result_r = self.random_rec(building_list, m, r)
        result_l.union(result_r)
        return result_l

    def random(self, n, h, w, x_min, x_max):
        if x_min >= x_max or h < 0 or n < 0 or w < 1:
            raise ValueError
        building_list = []
        for i in range(n):
            height = random.randint(0, h)
            width = random.randint(1, w)
            x = random.randint(x_min, x_max - width)
            other = Skyline()
            other.building(x, height, x + width)
            building_list.append(other)
        result = self.random_rec(building_list, 0, len(building_list))
        self.buildings = result.buildings
        self.area = result.area
        self.height = result.height

    def calculate_area(self):
        self.area = 0
        for i in range(len(self.buildings) - 1):
            self.area += (self.buildings[i + 1][0] - self.buildings[i][0])*self.buildings[i][1]
