from window import App

from window.components.button import (
	Button,
	ToggleButton,
	CheckBox,
	ToggleSwitch,
)
from window.components.slider import (
	Slider,
)
from window.constants import constants
colour = constants.colour.flat_ui.gb


if __name__ == '__main__':
	from os import system
	from platform import system as get_os
	os = get_os()
	if os == 'Windows':
		system('cls')
	else:
		system('clear')

	app = App()

	app += Button(
		(100, 50, 100, 50),
		colour.SKIRRET_GREEN, colour.NASTURCIAN_FLOWER,
		lambda: print('Button'),
		'Button'
	)
	
	app += ToggleButton(
		(50, 150, 200, 50),
		colour.SKIRRET_GREEN, colour.NASTURCIAN_FLOWER,
		lambda state: print(f'Toggle Button: {state}'),
		'Toggle Button'
	)
	
	app += CheckBox(
		(50, 250, 50, 50),
		lambda state: print(f'Check Box: {state}')
	)
	
	app += ToggleSwitch(
		(50, 350, 100, 50),
		colour.SKIRRET_GREEN, colour.NASTURCIAN_FLOWER,
		lambda state: print(f'Toggle Switch: {state}')
	)

	app += Slider(
		(50, 450, 150, 10),
		colour.SKIRRET_GREEN, colour.CHAIN_GANG_GREY,
		lambda level: print(f'Slider: {level}')
	)

	app()
