from pygame import Surface, Rect
from pygame.mouse import get_pos as get_mouse_pos


from config import settings

from maths import (
	clamp,
	lerp, lerp_colour,
)

from window.colour import colour
Colour = colour.Colour
colour = colour.flat_ui.gb

from window.components import ComponentBase
from window.tools import stretched_circle, circle


class Slider(ComponentBase):
	HORIZONTAL: int = 0
	VERTICAL:   int = 1
	
	directions = HORIZONTAL, VERTICAL

	def __init__(self, rect: Rect, c_on: Colour, c_off: Colour, action, direction: int = -1):
		super().__init__(rect)
		self._name = 'Slider'

		self.c_on = c_on
		self.c_off = c_off
		self.action = action
		self.direction = direction if direction in Slider.directions else (
			Slider.HORIZONTAL if self.rect.width > self.rect.height else Slider.VERTICAL
		)
		self.value = 0
		self.selected = False

	def __call__(self, x, y, direction):
		clicked = self.rect.collidepoint(x, y)

		if direction == 0:
			self.on_release()
		
		if clicked:
			if direction == 1:
				self.on_press(x, y)
			elif direction == 2:
				self.on_drag(x, y)

	def render(self):
		if self.selected:
			x, y = get_mouse_pos()
			self.on_drag(x, y)

		c = self.c_off
		stretched_circle(self.surface, self.rect, c)

		r = self.rect.copy()
		r.width *= self.value
		c = self.c_on
		stretched_circle(self.surface, r, c)

		c = settings.colour_scheme.handle
		# c = lerp_colour(self.c_off, self.c_on, self.value)
		circle(
			self.surface,
			self.rect.left + self.rect.width * self.value, self.rect.centery,
			min(self.rect.width, self.rect.height) * 1.125, c
		)

	def on_press(self, x, y):
		self.selected = True
		self.on_drag(x, y)

	def on_drag(self, x, y):
		if self.direction == self.HORIZONTAL:
			self.value = (x - self.rect.left) / self.rect.width
		elif self.direction == self.VERTICAL:
			self.value = (y - self.rect.top) / self.rect.height

		self.value = clamp(self.value)

		self.action(self.value)

	def on_release(self):
		self.selected = False
