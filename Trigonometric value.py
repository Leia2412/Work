import math

while True:
    angle_deg = float(input("Enter angle in degrees (or type -1 to exit): "))
    if angle_deg == -1:
        print("Goodbye!")
        break
    angle_rad = math.radians(angle_deg)
    print(f"sin({angle_deg}) = {math.sin(angle_rad)}")
    print(f"cos({angle_deg}) = {math.cos(angle_rad)}")
    print(f"tan({angle_deg}) = {math.tan(angle_rad)}\n")
print(f"{'Angle':>10} | {'Sin':>10} | {'Cos':>10} | {'Tan':>10}")
print("-" * 45)
print(f"{angle_deg:>10.2f} | {math.sin(angle_rad):>10.4f} | {math.cos(angle_rad):>10.4f} | {math.tan(angle_rad):>10.4f}")
import random

print(random.choice(facts))
import matplotlib.pyplot as plt
import numpy as np

angles = np.linspace(0, 360, 360)
radians = np.radians(angles)
sin_vals = np.sin(radians)
cos_vals = np.cos(radians)
tan_vals = np.tan(radians)

plt.plot(angles, sin_vals, label='sin')
plt.plot(angles, cos_vals, label='cos')
plt.plot(angles, tan_vals, label='tan')
plt.title("Trigonometric Functions")
plt.xlabel("Angle (degrees)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
import math

angle = 30
user_answer = float(input(f"What is sin({angle})? "))
correct = round(math.sin(math.radians(angle)), 2)
if round(user_answer, 2) == correct:
    print("Correct!")
else:
    print(f"Oops! The correct answer is {correct}")
