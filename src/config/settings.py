from json import loads

from os.path import (
	abspath, dirname,
	join
)

from window.colour import colour


with open(join(dirname(dirname(dirname(abspath(__file__)))), 'assets', 'settings.json'), 'r') as f:
	data = f.read()

_settings = loads(data)

class settings:
	width  = _settings['width'] or 1280
	height = _settings['height'] or 720

	class colour_scheme:
		background = _settings['colour_scheme']['bg'] or (0, 0, 0)
		base       = _settings['colour_scheme']['base'] or (0, 0, 0)
		handle     = _settings['colour_scheme']['handle'] or (0, 0, 0)

if type(settings.colour_scheme.background) == str:
	if settings.colour_scheme.background[0] == '#':
		hex_code = settings.colour_scheme.background[1:]
		r, g, b = hex_code[:2], hex_code[2:4], hex_code[4:]
		r = int(r, 16)
		g = int(g, 16)
		b = int(b, 16)
		settings.colour_scheme.background = r, g, b
	
	elif settings.colour_scheme.background[0] == '$':
		settings.colour_scheme.background = colour[settings.colour_scheme.background[1:]]

if type(settings.colour_scheme.base) == str:
	if settings.colour_scheme.base[0] == '#':
		hex_code = settings.colour_scheme.base[1:]
		r, g, b = hex_code[:2], hex_code[2:4], hex_code[4:]
		r = int(r, 16)
		g = int(g, 16)
		b = int(b, 16)
		settings.colour_scheme.base = r, g, b
	
	elif settings.colour_scheme.base[0] == '$':
		settings.colour_scheme.base = colour[settings.colour_scheme.base[1:]]

if type(settings.colour_scheme.handle) == str:
	if settings.colour_scheme.handle[0] == '#':
		hex_code = settings.colour_scheme.handle[1:]
		r, g, b = hex_code[:2], hex_code[2:4], hex_code[4:]
		r = int(r, 16)
		g = int(g, 16)
		b = int(b, 16)
		settings.colour_scheme.handle = r, g, b
	
	elif settings.colour_scheme.handle[0] == '$':
		settings.colour_scheme.handle = colour[settings.colour_scheme.handle[1:]]
