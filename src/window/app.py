from pygame import (
	init as pg_init,
	Surface,
	quit as pg_quit,
	QUIT as QUIT_EVENT,
	MOUSEBUTTONDOWN as MOUSEBUTTONDOWN_EVENT, MOUSEBUTTONUP as MOUSEBUTTONUP_EVENT,
)
from pygame.display import (
	set_mode, set_caption,
	update as update_display,
)
from pygame.event import (
	get as get_events,
	EventType,
)
from pygame.time import (
	Clock,
)

from typing import Dict


from .components import Button, ToggleButton, CheckBox
from .constants import constants
from .event import Event

colour = constants.colour.flat_ui.gb


pg_init()


class App:
	'''
	Base application
	'''

	def __init__(self):
		self.surface: Surface = set_mode((constants.WIDTH, constants.HEIGHT))
		self.clock = Clock()
		self.running = True

		self.buttons = []
		self.buttons.append( Button(
			self.surface,
			(100, 50, 100, 50),
			colour.SKIRRET_GREEN, colour.NASTURCIAN_FLOWER,
			lambda: print('Button'),
			'Button'
		) )
		self.buttons.append( ToggleButton(
			self.surface,
			(50, 150, 200, 50),
			colour.SKIRRET_GREEN, colour.NASTURCIAN_FLOWER,
			lambda state: print(f'Toggle Button: {state}'),
			'Toggle Button'
		) )
		self.buttons.append( CheckBox(
			self.surface,
			(50, 250, 50, 50),
			lambda state: print(f'Check Box: {state}')
		) )

	def __call__(self):
		while self.running:
			for e in get_events():
				event: EventType = e
				if event.type == QUIT_EVENT:
					self.running = False
				else:
					self.dispatch(event.type, event.dict)

			self.surface.fill(colour.BLUE_NIGHTS)

			[b.render() for b in self.buttons]

			update_display()
			self.clock.tick(60)

		pg_quit()

	def dispatch(self, event_type: Event, event_data: Dict):
		if event_type in (MOUSEBUTTONDOWN_EVENT, MOUSEBUTTONUP_EVENT,):
			direction = 0 if event_type == MOUSEBUTTONUP_EVENT else 1
			x, y = event_data['pos']
			button = event_data['button']
			
			if button == 1:
				[b(x, y, direction) for b in self.buttons]
