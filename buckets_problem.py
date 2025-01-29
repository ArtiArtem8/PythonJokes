import unittest

class TestPourWater(unittest.TestCase):
    def test_empty_buckets(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 3), [1, 1, 1])
        
    def test_full_buckets(self):
        self.assertEqual(pour_water([1, 1, 1], [1, 1, 1], 0), [1, 1, 1])
        
    def test_all_buckets_the_same(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 3), [1, 1, 1])
        
    def test_all_buckets_different(self):
        self.assertEqual(pour_water([3, 2, 1], [0, 0, 0], 3), [1, 1, 1])
        
    def test_water_is_zero(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 0), [0, 0, 0])
        
    def test_water_is_less_than_capacity(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 2), [1, 1, 0])
        
    def test_water_is_more_than_capacity(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 4), [1, 1, 1])
        
    def test_water_is_equal_to_capacity(self):
        self.assertEqual(pour_water([1, 1, 1], [0, 0, 0], 3), [1, 1, 1])
        
    # def test_water_is_negative(self):
    #     with self.assertRaises(ValueError):
    #         pour_water([1, 1, 1], [0, 0, 0], -1)
        
    # def test_capacity_is_zero(self):
    #     self.assertEqual(pour_water([0, 0, 0], [0, 0, 0], 1), [0, 0, 0])
        
    # def test_capacity_is_negative(self):
    #     with self.assertRaises(ValueError):
    #         pour_water([-1, -1, -1], [0, 0, 0], 1)
        
    # def test_level_is_greater_than_capacity(self):
    #     self.assertEqual(pour_water([1, 1, 1], [2, 2, 2], 1), [1, 1, 1])
        
    # def test_level_is_negative(self):
    #     with self.assertRaises(ValueError):
    #         pour_water([1, 1, 1], [-1, -1, -1], 1)

def pour_water(capacities, levels, water):
    while water > 0:
        for level, i, cap in sorted(zip(levels, range(len(capacities)), capacities)):
            if level < cap:
                levels[i] += 1
                water -= 1
                break
        else:
            break
    return levels

def pour_water_2(capacities: list[int], levels: list[int], W: int):
    current = levels[:]
    N = len(capacities)
    while W > 0:
        # Find all non-full buckets
        non_full = [i for i in range(N) if current[i] < capacities[i]]
        if not non_full:
            break  # All buckets are full, can't pour more
        
        # Find the minimum current among non-full buckets
        min_current = min(current[i] for i in non_full)
        current_buckets = [i for i in non_full if current[i] == min_current]
        
        # Determine the next minimum current in non-full buckets not in current_buckets
        others = [current[i] for i in non_full if i not in current_buckets]
        next_min = min(others) if others else float('inf')
        delta_candidate = next_min - min_current if next_min != float('inf') else float('inf')
        
        # Calculate the maximum delta we can pour
        delta_max_per_bucket = min(capacities[i] - current[i] for i in current_buckets)
        available_water = W // len(current_buckets)
        delta = min(delta_candidate, delta_max_per_bucket, available_water)
        
        if delta > 0:
            for i in current_buckets:
                current[i] += delta
            W -= delta * len(current_buckets)
        else:
            # Distribute remaining water one by one
            pour = min(W, len(current_buckets))
            for i in range(pour):
                current[current_buckets[i]] += 1
            W -= pour
    
    return current

size = 1000
levels = []
capacities = []
water_values = []

for j in range(1, size + 1):
    levels.append([i for i in range(j, -1, -1)])
    capacities.append([size for i in range(j, -1, -1)])
    water_values.append(j * size)


import time
import matplotlib.pyplot as plt

times = []

for i in range(len(water_values), 10):
    start_time = time.time()
    result = pour_water(capacities[i], levels[i][:], water_values[i])
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

times2 = []

for i in range(len(water_values)):
    start_time = time.time()
    result = pour_water_2(capacities[i], levels[i][:], water_values[i])
    elapsed_time = time.time() - start_time
    times2.append(elapsed_time)

plt.plot(water_values, times, label='pour_water')
plt.plot(water_values, times2, label='pour_water_2')
plt.xlabel('water')
plt.ylabel('time (seconds)')
plt.legend()
plt.show()

