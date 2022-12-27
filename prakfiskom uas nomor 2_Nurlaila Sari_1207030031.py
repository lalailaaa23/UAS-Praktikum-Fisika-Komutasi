import numpy as np
import matplotlib.pyplot as plt

alpha = np.radians(45)
g = 9.8
v0 = 20

v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

X = ((v0**2)*np.sin(2*alpha))/(2*g)
print("Jarak Horizontal Maksimum = ",X," m")
Y = ((v0**2)*(np.sin(alpha)**2))/(2*g)
print("Jarak Vertikal Maksimum = ",Y," m")
T = (2*v0*np.sin(alpha))/g
print ("Waktu Mencapai Jarak Horizontal Maksimum = ",T," s")
print("\n")

t = np.arange(0.0, T, 0.01)
y = v0y*t - 0.5*g*t**2
x = v0x*t

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x (m)', ylabel= 'y (m)' , title='Grafik Gerak Parabola')
ax.grid()
plt.show()
'''Rumus Fokus Lensa
     1/f = (n-1)[1/R1 + 1/R2]
'''
n  = 1.5   
R1 = 5   
R2 = 10

F = (n-1)*((1/R1)+(1/R2))
F = 1/F

print("-"*40)
print("Jarak Fokus Lensa = ",F)


