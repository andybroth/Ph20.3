import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n = 30
	h =  .1
	n = int(n / h)
	s_position = np.zeros(n)
	s_velocity = np.zeros(n)
	energy = np.zeros(n)
	time = np.linspace(0, h * n, n)
	s_position[0] = 0
	s_velocity[0] = 1
	energy[0] = 1
	for i in range(1, n):
		s_position[i] = s_position[i - 1] + h * s_velocity[i - 1]
		s_velocity[i] = s_velocity[i - 1] - h * s_position[i]
		energy[i] = s_position[i]**2 + s_velocity[i]**2
	actual_pos = np.zeros(n)
	actual_vel = np.zeros(n)
	actual_energy = np.zeros(n)
	for i in range(0, n):
		actual_pos[i] = np.sin(h * i)
		actual_vel[i] = np.cos(h * i)
		actual_energy[i] = actual_pos[i]**2 + actual_vel[i]**2
	plt.plot(time, energy, label = 'Symplectic Energy')
	plt.plot(time, actual_energy, label = 'Actual Energy')
	plt.xlabel('Time')
	plt.ylabel('Energy')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.title('Symplectic Energy vs. Actual Energy')
	plt.savefig('symp_energy.pdf')