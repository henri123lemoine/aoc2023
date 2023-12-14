import sys
import numpy as np

class Platform:
    def __init__(self, platform: np.ndarray):
        self.platform = platform
        self.height = platform.shape[0]
        self.width = platform.shape[1]

        self.cache = {self.platform.tobytes(): 0}
        self.platform_cycle_cache = {0: self.platform.copy()}

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self.platform)
    
    def column_gravity(self, column: np.ndarray) -> np.ndarray:
        new_column = np.full_like(column, '.')
        rock_stack = []
        for i, element in enumerate(column):
            if element == 'O':
                rock_stack.append(element)
            elif element == '#':
                new_column[i-len(rock_stack):i] = rock_stack
                rock_stack = []
                new_column[i] = '#'
        new_column[len(column)-len(rock_stack):] = rock_stack
        return new_column

    def gravity_south(self):
        for column_index in range(self.width):
            column = self.platform[:, column_index]
            self.platform[:, column_index] = self.column_gravity(column)
    
    def gravity_north(self):
        for column_index in range(self.width):
            column = self.platform[:, column_index]
            self.platform[:, column_index] = self.column_gravity(column[::-1])[::-1]

    def gravity_east(self):
        for row_index in range(self.height):
            row = self.platform[row_index, :]
            self.platform[row_index, :] = self.column_gravity(row)

    def gravity_west(self):
        for row_index in range(self.height):
            row = self.platform[row_index, :]
            self.platform[row_index, :] = self.column_gravity(row[::-1])[::-1]
    
    @property
    def total_load(self) -> int:
        load = 0
        for column_index in range(self.width):
            for i, element in enumerate(self.platform[:, column_index]):
                if element == 'O':
                    load += self.height - i
        return load

    def gravity(self, num_cycles: int):
        for i in range(1, num_cycles + 1):
            self.gravity_north()
            self.gravity_west()
            self.gravity_south()
            self.gravity_east()

            if self.platform.tobytes() in self.cache:
                start, end = self.cache[self.platform.tobytes()], i
                cycle_length = end - start
                round = (num_cycles - start) % cycle_length + start
                self.platform = self.platform_cycle_cache[round]
                return self.total_load

            self.cache[self.platform.tobytes()] = i
            self.platform_cycle_cache[i] = self.platform.copy()
        
        return self.total_load


platform = Platform(np.array([list(line) for line in sys.stdin.read().splitlines()]))

print(platform.gravity(1_000_000_000))
    