height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

bmi=np_weight / np_height ** 2

print(bmi)

print(bmi > 23)
print(bmi[bmi > 23])


weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight = np.array(weight_kg)

weight_lb = np_weight * 2.2

print(weight_lb)
