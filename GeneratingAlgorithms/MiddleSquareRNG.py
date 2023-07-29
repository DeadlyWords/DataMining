import time
import matplotlib.pyplot as plt

global duration
duration = []

def middle_square(seed, iterations):
    random_numbers = []
    for _ in range(iterations):
        beforeZufall = time.perf_counter()
        seed_squared = str(seed ** 2).zfill(8)
        middle_digits = seed_squared[2:6]
        seed = int(middle_digits)
        random_numbers.append(seed)
        afterZufall = time.perf_counter()
        duration.append(afterZufall-beforeZufall)
    return random_numbers

# Set the initial seed
seed = 636774378

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

# Generate 1000 random numbers using the middle square algorithm
random_numbers = middle_square(seed, 1000)

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

# Print the generated random numbers
for num in random_numbers:
    print(num)

#Duration ist being plotted
plt.plot(duration)
plt.show()
