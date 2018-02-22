import numpy as np, matplotlib.pyplot as plt

def h_error(n_0, h):
	h_vals = np.geomspace(.0001, .1, num = 20)
	position = np.zeros(n_0)
	velocity = np.zeros(n_0)
	actual_pos = np.zeros(n_0)
	position[0] = 0
	velocity[0] = 1
	max_error = np.zeros(20)
	for j, h in enumerate(h_vals):
		n = int(n_0 / h)
		position = np.zeros(n)
		velocity = np.zeros(n)
		actual_pos = np.zeros(n)
		position[0] = 0
		velocity[0] = 1
		for i in range(1, n):
			position[i] = position[i - 1] + h * velocity[i - 1]
			velocity[i] = velocity[i - 1] - h * position[i - 1]
		for i in range(0, n):
			actual_pos[i] = np.sin(h * i)
		max_error[j] = np.amax(np.abs(position - actual_pos))
	plt.plot(h_vals, max_error, 'bo' ,label = 'Error')
	plt.title('Max Error vs. h')
	plt.xlabel('h')
	plt.ylabel('Max Error for that h value')
	plt.loglog()
	t = np.arange(.0001, .1001, .01)
	plt.plot(t, t, label = 'Linear Plot')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.show()

def pos_vel(n, h):
	n = int(n / h)
	position = np.zeros(n)
	velocity = np.zeros(n)
	time = np.linspace(0, h * n, n)
	position[0] = 0
	velocity[0] = 1
	for i in range(1, n):
		position[i] = position[i - 1] + h * velocity[i - 1]
		velocity[i] = velocity[i - 1] - h * position[i - 1]
	actual_pos = np.zeros(n)
	actual_vel = np.zeros(n)
	for i in range(0, n):
		actual_pos[i] = np.sin(h * i)
		actual_vel[i] = np.cos(h * i)
	plt.plot(time, position, label = 'Position')
	plt.plot(time, velocity, label = 'Velocity')
	# plt.plot(time, actual_pos, label = 'Actual Position')
	# plt.plot(time, actual_vel, label = 'Actual Velocity')
	plt.xlabel('Time')
	plt.ylabel('Position or Velocity')
	plt.title('Position and Velocity vs. Time')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.show()
	plt.plot(time, np.abs(position - actual_pos), label = 'Position Error')
	plt.plot(time, np.abs(velocity - actual_vel), label = 'Velocity Error')
	plt.xlabel('Time')
	plt.ylabel('Error')
	plt.title('Global Error vs. Time')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	# plt.show()

def energy(n, h):
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
	plt.show()

def implicit_xv(n, h):
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
	plt.show()

def energy_comp(n, h):
	n = int(n / h)
	i_position = np.zeros(n)
	i_velocity = np.zeros(n)
	i_energy = np.zeros(n)
	time = np.linspace(0, h * n, n)
	i_position[0] = 0
	i_velocity[0] = 1
	i_energy[0] = 1
	position = np.zeros(n)
	velocity = np.zeros(n)
	E = np.zeros(n)
	position[0] = 0
	velocity[0] = 1
	E[0] = 1
	for i in range(1, n):
		i_position[i] = (i_position[i - 1] + h * i_velocity[i - 1]) / (1 + h**2)
		i_velocity[i] = (i_velocity[i - 1] - h * i_position[i - 1]) / (1 + h**2)
		i_energy = i_position ** 2 + i_velocity ** 2
		position[i] = position[i - 1] + h * velocity[i - 1]
		velocity[i] = velocity[i - 1] - h * position[i - 1]
		E[i] = position[i]**2 + velocity[i]**2
	plt.plot(time, i_energy, label = 'Implicit Energy')
	plt.plot(time, E, label = 'Explicit Energy')
	plt.xlabel('Time')
	plt.ylabel('Energy')
	plt.title('Energy vs. Time')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.show()

def phase_space(n, h):
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
	
	
	s_position = np.zeros(n)
	s_velocity = np.zeros(n)
	s_position[0] = 0
	s_velocity[0] = 1
	for i in range(1, n):
		s_position[i] = s_position[i - 1] + h * s_velocity[i - 1]
		s_velocity[i] = s_velocity[i - 1] - h * s_position[i]
	plt.plot(s_position, s_velocity, label = 'Symplectic Method')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.axis('equal')
	plt.show()

def symp_energy(n, h):
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
	plt.show()



if __name__ == '__main__':
	n = 30
	h =  .1
	pos_vel(n, h)
    # h_error(n, h)
	# energy(n, h)
	# implicit_xv(n, h)
	# energy_comp(n, h)
	# phase_space(n ,h)
	# symp_energy(n ,h)