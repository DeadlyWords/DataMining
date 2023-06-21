import time
import matplotlib.pyplot as plt
import numpy as np


f = open("GeneratedData/blumdata","x")

global duration
duration = []

class BBSRandom:
    def __init__(self, p, q, seed):
        self.p = p
        self.q = q
        self.n = p * q
        self.state = seed

    def _next_state(self):
        self.state = pow(self.state, 2, self.n)

    def get_random_bit(self):
        self._next_state()
        return self.state % 2

    def get_random_int(self, bits):
        beforeZufall = time.perf_counter()
        result = 0
        for _ in range(bits):
            result = (result << 1) | self.get_random_bit()
        afterZufall = time.perf_counter()
        duration.append(afterZufall-beforeZufall)
        return result


# Example usage
p = 1097
q = 2447
seed = 123456789

random_generator = BBSRandom(p, q, seed)

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

# Generate and store 1000 random integers with 16 bits each
random_numbers = []
for _ in range(29000):
    for i in range(10):
        random_int = random_generator.get_random_int(32)
        print(format(random_int, '08x'))
        f.write(format(random_int, '08x'))
        random_numbers.append(random_int)
    f.write("\n")    

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

plt.plot(random_numbers)
plt.show()
