
class ComponentBase:
	def __init__(self, rect):
		self._name = 'Component'

		self.surface = None

		from pygame import Rect
		self.rect = Rect(rect)

	def __str__(self):
		return f'{self._name} ( [{self.rect.x}, {self.rect.y}], [{self.rect.width}, {self.rect.height}] )'

	def __eq__(self, other):
		return type(self) == type(other) and self._name == other._name and self.surface == other.surface and self.rect == other.rect

	def mount(self, surface):
		self.surface = surface

	def render(self):
		raise NotImplementedError('Components must implement a render method')


from . import button
from . import slider
