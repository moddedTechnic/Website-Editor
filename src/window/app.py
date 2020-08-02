from pygame import (
	init as pg_init,
	Surface,
	QUIT as pg_QUIT,
	quit as pg_quit
)
from pygame.display import (
	set_mode, set_caption,
	update as update_display
)
from pygame.event import (
	get as get_events,
	EventType,
)
from pygame.time import (
	Clock,
)

from .constants import constants


pg_init()


class App:
	'''
	Base application
	'''

	def __init__(self):
		self.surface: Surface = set_mode((constants.WIDTH, constants.HEIGHT))

		self.clock = Clock()
		
		self.running = True

	def __call__(self):
		while self.running:
			for e in get_events():
				event: EventType = e
				if event.type == pg_QUIT:
					self.running = False

			self.surface.fill(constants.colour.LIGHT_GREY)

			update_display()
			self.clock.tick(60)

		pg_quit()
