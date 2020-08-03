from pygame import (
	Surface, Rect
)
from pygame.draw import (
	rect
)

from window.constants import constants
colour = constants.colour.flat_ui.gb
Colour = constants.colour.Colour
from window.tools import rounded_rect, stretched_circle, circle

from .check_box import CheckBox

class ToggleSwitch(CheckBox):
	HORIZONTAL: int = 0
	VERTICAL:   int = 1
	
	directions = HORIZONTAL, VERTICAL

	def __init__(self, surface: Surface, rect: Rect, c_on: Colour, c_off: Colour, action, direction: int = -1):
		super().__init__(surface, rect, action)
		self.c_on = c_on
		self.c_off = c_off
		self.direction = direction if direction in ToggleSwitch.directions else (
						 ToggleSwitch.HORIZONTAL if self.rect.width > self.rect.height else ToggleSwitch.VERTICAL
		)

	def render(self):
		stretched_circle(self.surface, self.rect, colour.CHAIN_GANG_GREY)
		c = self.c_on if self.pressed else self.c_off
		r = self.rect.copy()
		r.x += r.width * .05
		r.y += r.height * .05
		r.width *= .9
		r.height *= .9
		stretched_circle(self.surface, r, c)

		r.x += r.width / 4 * (3 if self.pressed else 1)
		r.y += r.height / 2
		circle(self.surface, r.x, r.y, min(r.width, r.height) / 2, colour.MAZARINE_BLUE)
