import numpy as np

w = int(input("Szerokość okna: "))
h = int(input("Wysokość okna: "))
print("c = a + bi")
c = complex(float(input("Wartość a: ")), float(input("Wartość b: ")))

r_min = -2.0
r_max = 2.0
i_min = -2.0
i_max = 2.0

name = "julia.pgm"
r_range = np.arange(r_min, r_max, (r_max - r_min)/w)
i_range = np.arange(i_min, i_max, (i_max - i_min)/h)

output = open(name, "w")
output.write(f"P2\n{w} {h}\n255\n")

for u in i_range:
    for r in r_range:
        z = complex(r, u)
        n = 255

        while abs(z) < 10 and n != 0:
            z = z*z + c
            n -= 5

        output.write(f"{n} ")
    output.write("\n")
output.close()
