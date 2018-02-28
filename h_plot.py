import numpy as np, matplotlib.pyplot as plt

if __name__ == '__main__':
	n_0 = 30
	h =  .1
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
	plt.savefig('h_plot.pdf')