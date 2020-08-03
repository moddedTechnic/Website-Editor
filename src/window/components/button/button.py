from abc import abstractmethod

from pygame import (
	Surface,
	Rect
)
from pygame.draw import (
	rect
)
from pygame.font import (
	Font
)

from window.constants import constants
colour = constants.colour.flat_ui.gb
Colour = constants.colour.Colour

from window.components import ComponentBase
from window.tools import draw_text, fonts, rounded_rect

class ButtonBase(ComponentBase):
	def __init__(self, rect: Rect, action):
		super().__init__(rect)
		self._name = 'ButtonBase'

		self.action = action

	def __call__(self, x, y, direction):
		if self.rect.collidepoint(x, y):
			self.on_press(direction)

		if direction == 0:
			self.on_release()

	@abstractmethod
	def on_press(self, direction):
		pass

	def on_release(self):
		pass


class Button(ButtonBase):
	def __init__(self, rect: Rect, c_on: Colour, c_off: Colour, action, label: str = '', active_high: bool = True):
		super().__init__(rect, action)
		self._name = 'Button'
		
		self.c_on: Colour = c_on
		self.c_off: Colour = c_off
		self.pressed = False
		self.active_high = active_high
		self.label = label

		if not self.active_high:
			self.action()

	def render(self):
		rounded_rect(self.surface, self.rect, self.c_on if self.pressed else self.c_off, min(self.rect.width, self.rect.height) * .1)
		r = Rect(self.rect)
		r.center = self.rect.x + self.rect.width * 19 / 32, self.rect.y + self.rect.height * 19 / 32
		draw_text(self.surface, self.label, Font(fonts.ANONYMOUS_PRO_REGULAR, 24), r, colour.ELECTROMAGNETIC)

	def on_press(self, direction):
		self.pressed = direction == 1

		if self.pressed == self.active_high:
			self.action()

	def on_release(self):
		self.pressed = False


class ToggleButton(Button):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._name = 'ToggleButton'

	def on_press(self, direction):
		if direction == 1:
			self.pressed = not self.pressed
			self.action(self.pressed)

	def on_release(self):
		pass
