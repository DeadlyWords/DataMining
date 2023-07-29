import time
import matplotlib.pyplot as plt

global duration
duration = []


class MersenneTwister:
    def __init__(self, seed):
        self.w = 32
        self.n = 624
        self.m = 397
        self.r = 31
        self.a = 0x9908B0DF
        self.u = 11
        self.d = 0xFFFFFFFF
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.f = 1812433253

        self.MT = [0] * self.n
        self.index = self.n + 1
        self.lower_mask = (1 << self.r) - 1
        self.upper_mask = (1 << self.w) - 1 - self.lower_mask

        self.seed(seed)

    def seed(self, seed):
        self.index = self.n
        self.MT[0] = seed
        for i in range(1, self.n):
            self.MT[i] = self.f * \
                (self.MT[i-1] ^ (self.MT[i-1] >> (self.w-2))) + i

    def extract_number(self):
        beforeZufall = time.perf_counter()
        if self.index >= self.n:
            self.twist()

        y = self.MT[self.index]
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)

        self.index += 1
        afterZufall = time.perf_counter()
        duration.append(afterZufall-beforeZufall)
        return y & ((1 << self.w) - 1)

    def twist(self):
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + \
                (self.MT[(i+1) % self.n] & self.lower_mask)
            xA = x >> 1
            if x % 2 != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA
        self.index = 0


vorTausend = time.perf_counter()
print("Before 1000 = ", vorTausend)

# Example usage
mt = MersenneTwister(1234)
random_numbers = [mt.extract_number() for _ in range(1000000)]

nachTausend = time.perf_counter()
print("After 1000 = ", nachTausend)
print("Time for 1000 = " + str(nachTausend - vorTausend))

# for number in random_numbers:
#     print(number)

# plt.figure(figsize=(15, 8))
# plt.hist(random_numbers, edgecolor="red", bins=len(random_numbers))
# plt.show()

try:
    with open("outLehmer.txt", 'w') as file:
        for number in random_numbers:
            # file.write((number).to_bytes(24, byteorder='big', signed=False))
            file.write(str(number) + "\n")
except Exception as e:
    print(e)