import numpy as np

u = np.array([2, 3])
v = np.array([4, -7])

print(f'Vektori u: {u}')
print(f'Vektori v: {v}')

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

print(f'Vektori uu: {uu}')
print(f'Vektori vv: {vv}')

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_uu = np.linalg.norm(uu)
norm_vv = np.linalg.norm(vv)

print(f'Vektorin u normi: {norm_u}')
print(f'Vektorin v normi: {norm_v}')
print(f'Vektorin uu normi: {norm_uu}')
print(f'Vektorin vv normi: {norm_vv}')
