class RotateMatrix:


	def __init__(self, given_matrix):
		self.matrix = given_matrix
		self.max_pos = len(given_matrix) - 1

	def rotate(self):
		x = 0
		y = 0
		while x * 2 <= self.max_pos:
			while y * 2 < self.max_pos + 1:
				self._rotate_coordinates(x,y)
				y +=1
			x+=1

	def _rotate_coordinates(self, x_pos, y_pos):
		count = 0
		value = self.matrix[x_pos][y_pos]
		while count < 4:
			x_pos, y_pos, value = self._shift_values(x_pos, y_pos, value)
			count += 1

	def _shift_values(self, old_x, old_y, new_value):
		new_x = abs(old_y - self.max_pos)
		new_y = old_x
		moving_value = self.matrix[new_x][new_y]
		self.matrix[new_x][new_y] = new_value
		return new_x, new_y, moving_value
