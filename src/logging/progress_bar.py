from typing import Optional

class ProgressBar:
	'''
	A simple progress bar

	Args:
		title (str): The name for the progress bar
		length (int): The length of the progress bar
		fill (str): The fill character
		blank (str): The blank character

	Attributes:
		length (int): The length of the bar in characters
		fill (str): The fill character
		blank (str): The blank character
		progress_x (float): The current fill level
	'''

	def __init__(self, title: str, length: Optional[int] = 40, fill: Optional[str] = '#', blank: Optional[str] = '-'):
		from sys import stdout
		self.stdout: file = stdout

		self.length: int = length
		self.fill: str = fill
		self.blank: str = blank

		self.stdout.write(f'{title}: [{self.blank * self.length}]{chr(8) * (self.length+1)}')
		self.stdout.flush()
		self.progress_x: float = 0

	def __call__(self, x: float):
		'''
		Set the progress

		Args:
			x (int): The progress level
		'''

		x = int(x * self.length)
		self.stdout.write(self.fill * (x - self.progress_x))
		self.stdout.flush()
		self.progress_x = x

	def __del__(self):
		''' Finish using the bar and clean up '''
		self.stdout.write(self.fill * (self.length - self.progress_x) + ']\n')
		self.stdout.flush()
