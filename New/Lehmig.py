import time
import matplotlib.pyplot as plt
from numpy import ndarray
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
random_generator = LehmerRandomGenerator(seed=425172342)

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

random_numbers = [random_generator.generate_uniform() for _ in range(30000000)]

print(len(random_numbers))
nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

# for number in random_numbers:
#    print(number)

# print(random_numbers)

# biggestInt = max(random_numbers)

# distribution = (biggestInt + 1) * [0]

# print(len(distribution))
# print(len(random_numbers))

# for i in range(len(random_numbers)):
#    distribution[random_numbers[i]] += 1

# distribution = {}
# for i in random_numbers:
#    if distribution.get(i):
#        distribution[i] += 1
#    else:
#        distribution[i] = 1

# print(distribution)

# plt.plot(distribution)
# plt.show()

# plt.hist(distribution, bins=np.arange(
#    min(distribution), max(distribution)+1))
# plt.gca().set(title="Histogram", ylabel="Frequency")

# df = pd.DataFrame(distribution)
# df.plot.bar()

# xValues = []
# yValues = []

# for i in distribution:
#    xValues.append(i)
#    yValues.append(distribution[i])

# print(xValues)
# print(yValues)


# plt.figure(figsize=(15, 8))
# plt.hist(random_numbers, edgecolor="red", bins=len(random_numbers))
# plt.show()

try:
    with open("outLehmer.txt", 'w') as file:
        for number in random_numbers:
            #file.write((number).to_bytes(24, byteorder='big', signed=False))
            file.write(str(number) + "\n")
except Exception as e:
    print(e)
