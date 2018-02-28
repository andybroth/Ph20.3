import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n = 30
	h =  .1
	n = int(n / h)
	position = np.zeros(n)
	velocity = np.zeros(n)
	time = np.linspace(0, h * n, n)
	position[0] = 0
	velocity[0] = 1
	for i in range(1, n):
		position[i] = (position[i - 1] + h * velocity[i - 1]) / (1 + h**2)
		velocity[i] = (velocity[i - 1] - h * position[i - 1]) / (1 + h**2)
	plt.plot(time, position, label = 'Position')
	plt.plot(time, velocity, label = 'Velocity')
	plt.xlabel('Time')
	plt.ylabel('Position or Velocity')
	plt.title('Position and Velocity vs. Time')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.savefig('implicit_plot.pdf')