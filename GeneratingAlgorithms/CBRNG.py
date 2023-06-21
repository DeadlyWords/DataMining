import time
import matplotlib.pyplot as plt

global duration
duration = []

class CBRN:
    def __init__(self, seed):
        self.counter = seed

    def random(self):
        beforeZufall = time.perf_counter()

        self.counter = (self.counter * 1103515245 + 12345) % (2**31)

        afterZufall = time.perf_counter()
        duration.append(afterZufall-beforeZufall)

        return self.counter


# Example usage to generate and print 1000 random integers
cbrn = CBRN(1234)  # Initialize with seed value
random_numbers = []  # Empty list to store random numbers

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

for _ in range(1000):
    random_number = cbrn.random()
    random_numbers.append(random_number)

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

for number in random_numbers:
        print(number)

plt.plot(duration)
plt.show()