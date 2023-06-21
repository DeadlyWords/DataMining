import time
import matplotlib.pyplot as plt

global duration
duration = []

class LehmerRandomGenerator:
    def __init__(self, seed=1):
        self.modulus = 2 ** 31 - 1
        self.multiplier = 16807
        self.seed = seed

    def generate_random(self):
        self.seed = (self.multiplier * self.seed) % self.modulus
        return self.seed

    def generate_uniform(self):
        vorZufall = time.perf_counter()

        random_num = self.generate_random()

        afterZufall = time.perf_counter()
        duration.append(afterZufall-vorZufall)

        return int(random_num % self.modulus)


# Example usage:
random_generator = LehmerRandomGenerator(seed=1234)

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

random_numbers = [random_generator.generate_uniform() for _ in range(1000)]

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

for number in random_numbers:
    print(number)


plt.plot(duration)
plt.show()