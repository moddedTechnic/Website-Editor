from pygame import (
	init as pg_init,
	Surface,
	quit as pg_quit,
	QUIT as QUIT_EVENT,
	MOUSEBUTTONDOWN as MOUSEBUTTONDOWN_EVENT, MOUSEBUTTONUP as MOUSEBUTTONUP_EVENT,
	MOUSEMOTION as MOUSEMOTION_EVENT,
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


from config import settings

from .components import ComponentBase
from .components.button import ButtonBase
from .components.slider import Slider

from .event import Event


pg_init()


class App:
	'''
	Base application
	'''

	def __init__(self):
		self.surface: Surface = set_mode((settings.width, settings.height))
		self.clock = Clock()
		self.running = True

		self.buttons = []
		self.sliders = []
		self.components = []

	def __call__(self):
		while self.running:
			for e in get_events():
				event: EventType = e
				if event.type == QUIT_EVENT:
					self.running = False
				else:
					self.dispatch(event.type, event.dict)

			self.surface.fill(settings.colour_scheme.background)

			[c.render() for c in self.components]
			[b.render() for b in self.buttons]
			[s.render() for s in self.sliders]

			update_display()
			self.clock.tick(60)

		pg_quit()

	def __iadd__(self, other):
		print(f'Attempting to mount component: {other}')

		if issubclass(type(other), ComponentBase):
			other.mount(self.surface)

			if issubclass(type(other), ButtonBase):
				self.buttons.append(other)
			elif isinstance(other, Slider):
				self.sliders.append(other)
			else:
				self.components.append(other)

		else:
			raise NotImplementedError(f'Cannot add object of type {type(other)} to an app')

		return self

	def __isub__(self, other):
		if issubclass(type(other), ComponentBase):
			if issubclass(type(other), ButtonBase):
				self.buttons.remove(other)
			elif isinstance(other, Slider):
				self.sliders.remove(other)
			else:
				self.components.remove(other)

		return self

	def dispatch(self, event_type: Event, event_data: Dict):
		if event_type in (MOUSEBUTTONDOWN_EVENT, MOUSEBUTTONUP_EVENT,):
			direction = 0 if event_type == MOUSEBUTTONUP_EVENT else 1
			x, y = event_data['pos']
			button = event_data['button']
			
			if button == 1:
				[b(x, y, direction) for b in self.buttons]
				[s(x, y, direction) for s in self.sliders]

		elif event_type == MOUSEMOTION_EVENT:
			button_pressed = event_data['buttons'][0] == 1
			x, y = event_data['pos']

			if button_pressed:
				[s(x, y, 2) for s in self.sliders]
