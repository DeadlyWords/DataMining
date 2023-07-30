import time
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

global duration
duration = []

permutations = int(30000000)

def middle_square(seed, iterations):
    random_numbers = []
    seed_number = seed #4 Digit
    number = seed_number
    counter = 0

    for _ in range(iterations):
        counter += 1
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        random_numbers.append(number)

    return random_numbers
    
    # random_numbers = []
    # for _ in range(iterations):
    #     # beforeZufall = time.perf_counter()
    #     seed_squared = str(seed ** 2).zfill(8)
    #     middle_digits = seed_squared[2:6]
    #     seed = int(middle_digits)
    #     random_numbers.append(seed)
    #     # afterZufall = time.perf_counter()
    #     # duration.append(afterZufall-beforeZufall)
    # return random_numbers


# Set the initial seed
seed = 4598

vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

# Generate 1000 random numbers using the middle square algorithm
random_numbers = middle_square(seed, permutations)
nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

# Print the generated random numbers
# for num in random_numbers:
#    print(num)

#biggestInt = max(random_numbers)

#distribution = (biggestInt + 1) * [0]

# print(len(distribution))
# print(len(random_numbers))

#for i in range(len(random_numbers)):
#    distribution[random_numbers[i]] += 1

# Duration ist being plotted

# upscaled_image = Image.fromarray(d).resize(
#   [300, 300], resample=Image.NEAREST)
# upscaled_image = np.asarray(upscaled_image)

# plt.plot(upscaled_image)
# plt.show()

# print(random_numbers)

# plt.figure(figsize=(15, 8))
# plt.hist(random_numbers, edgecolor="red", bins=len(random_numbers))
# plt.show()

try:
    with open("outSquare.txt", 'w') as file:
        for number in random_numbers:
            #file.write((number).to_bytes(24, byteorder='big', signed=False))
            file.write(str(number)+"\n")
except Exception as e:
    print(e)