from pygame import (
	Surface, Rect
)
from pygame.draw import (
	rect,
	aalines as lines,
)
from pygame.gfxdraw import (
	aapolygon as polygon_edge,
	filled_polygon as polygon_fill,
)

from typing import List, Tuple


from config import settings

from window.colour import colour
Colour = colour.Colour
from window.tools import rounded_rect

from .button import ButtonBase


class CheckBox(ButtonBase):
	def __init__(self, rect: Rect, action):
		super().__init__(rect, action)
		self._name = 'CheckBox'
		
		self.pressed: bool = False

	def render(self):
		rounded_rect(self.surface, self.rect, settings.colour_scheme.base, min(self.rect.width, self.rect.height) * .1)
		if self.pressed:
			points: List[ Tuple[float, float] ] = [
				( .125,  .5625 ), # 0
				( .3333, .8125 ), # 1
				( .875,  .1875 ), # 2
				( .8125, .125  ), # 3
				( .3333, .6875 ), # 4
				( .1875, .5    ), # 5
			]
			
			polygon_fill(
				self.surface,
				[ (self.rect.x + self.rect.width * a, self.rect.y + self.rect.height * b) for a, b in points ],
				settings.colour_scheme.handle
			)

	def on_press(self, direction):
		if direction == 1:
			self.pressed = not self.pressed
			self.action(self.pressed)
