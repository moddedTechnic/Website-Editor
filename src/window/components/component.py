
class ComponentBase:
	def __init__(self, rect):
		self._name = 'Component'

		self.surface = None
		self.rect = Rect(rect)

	def __str__(self):
		return f'{self._name} ( [{self.rect.x}, {self.rect.y}], [{self.rect.width}, {self.rect.height}] )'

	def mount(self, surface):
		self.surface = surface

	@abstractmethod
	def render(self):
		pass
