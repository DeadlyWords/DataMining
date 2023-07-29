import time
import matplotlib.pyplot as plt

global duration
duration = []

class Xoroshiro128Plus:
    def __init__(self, seed):
        self.state = [0, 0]
        self.seed(seed)

    def seed(self, seed):
        self.state[0] = self._splitmix64(seed)
        self.state[1] = self._splitmix64(seed + 1)

    def _splitmix64(self, x):
        z = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB
        return z ^ (z >> 31)

    def generate(self, count):
        result = []
        for _ in range(count):
            beforeZufall = time.perf_counter()
            s0, s1 = self.state
            value = (s0 + s1) & 0xFFFFFFFFFFFFFFFF

            s1 ^= s0
            self.state[0] = ((s0 << 55) | (s0 >> 9) ^ s1 ^ (s1 << 14)) & 0xFFFFFFFFFFFFFFFF
            self.state[1] = ((s1 << 36) | (s1 >> 28)) & 0xFFFFFFFFFFFFFFFF

            afterZufall = time.perf_counter()
            duration.append(afterZufall-beforeZufall)

            result.append(value)
        return result

# Example usage:
rng = Xoroshiro128Plus(12345)

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

random_numbers = rng.generate(30000000)
print(random_numbers)

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

# plt.plot(duration)
# plt.show()

try:
    with open("outXiro.bin", 'wb') as file:
        for number in random_numbers:
            file.write((number).to_bytes(24, byteorder='big', signed=False))
            # file.write(str(number) + "\n")
except Exception as e:
    print(e)
