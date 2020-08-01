from typing import List

class Spinner:
	'''
	A simple spinner

	Args:
		title (str): The title for the spinner
	'''

	def __init__(self, title: str):
		from sys import stdout
		self.stdout: file = stdout

		self.step: int = 0
		self.steps: List[str] = ['-', '\\', '|', '/']
		self.stdout.write(title + ': ' + self.steps[self.step] + chr(8))
		self.stdout.flush()

	def __call__(self):
		''' Advance the spinner '''
		self.step += 1
		self.step %= 4
		self.stdout.write(self.steps[self.step] + chr(8))
		self.stdout.flush()

	def __del__(self):
		''' Finish using the spinner and clean up '''
		self.stdout.write(self.steps[self.step] + '\n')
		self.stdout.flush()
