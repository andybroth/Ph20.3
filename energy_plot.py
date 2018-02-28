import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n = 30
	h =  .1
	n = int(n / h)
	time = np.linspace(0, h * n, n)
	position = np.zeros(n)
	velocity = np.zeros(n)
	E = np.zeros(n)
	position[0] = 0
	velocity[0] = 1
	E[0] = 1
	for i in range(1, n ):
			position[i] = position[i - 1] + h * velocity[i - 1]
			velocity[i] = velocity[i - 1] - h * position[i - 1]
			E[i] = position[i]**2 + velocity[i]**2
	plt.plot(time, E, label = 'Explicit')
	plt.title('Energy vs. Time')
	plt.xlabel('Time')
	plt.ylabel('Total Energy')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.savefig('energy_plot.pdf')