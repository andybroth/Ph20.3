import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n = 30
	h = .1
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
	plt.savefig('explicit_plot.pdf')
	plt.plot(time, np.abs(position - actual_pos), label = 'Position Error')
	plt.plot(time, np.abs(velocity - actual_vel), label = 'Velocity Error')
	plt.xlabel('Time')
	plt.ylabel('Error')
	plt.title('Global Error vs. Time')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
	plt.savefig('error_plot.pdf')