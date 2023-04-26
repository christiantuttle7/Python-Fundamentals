import matplotlib.pyplot as plt

x_vals = [1,2,3,4,5]
y_vals = [10.2, 4, 60, 0, 10]

more_vals = [3,4,6,1,6]

plt.title("Weather Data")
plt.xlabel("Time")
plt.ylabel("Temperatures")

#plt.subplot(1,1,1)
plt.plot(x_vals, y_vals, 'o-g')

#plt.subplot(1,1,2)
plt.plot(more_vals, 'o:r')



plt.show()