import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n = 30
	h =  .1
	n = int(n / h)
	i_position = np.zeros(n)
	i_velocity = np.zeros(n)
	time = np.linspace(0, h * n, n)
	i_position[0] = 0
	i_velocity[0] = 1
	position = np.zeros(n)
	velocity = np.zeros(n)
	position[0] = 0
	velocity[0] = 1
	for i in range(1, n):
		i_position[i] = (i_position[i - 1] + h * i_velocity[i - 1]) / (1 + h**2)
		i_velocity[i] = (i_velocity[i - 1] - h * i_position[i - 1]) / (1 + h**2)
		position[i] = position[i - 1] + h * velocity[i - 1]
		velocity[i] = velocity[i - 1] - h * position[i - 1]
	plt.plot(position, velocity, label = 'Explicit')
	plt.plot(i_position, i_velocity, label = 'Implicit')
	plt.xlabel('Position')
	plt.ylabel('Velocity')
	plt.title('Phase Space Geometry')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.axis('equal')
	plt.show()
	plt.savefig('phase_space.pdf')