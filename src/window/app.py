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


pg_init()


class App:
	'''
	Base application
	'''

	def __init__(self):
		self.width: int = 640
		self.height: int = 480
		self.surface: Surface = set_mode((self.width, self.height))

		self.clock = Clock()
		
		self.running = True

	def __call__(self):
		while self.running:
			for e in get_events():
				event: EventType = e
				if event.type == pg_QUIT:
					self.running = False

			update_display()
			self.clock.tick(60)

		pg_quit()
