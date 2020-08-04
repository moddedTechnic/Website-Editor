from typing import Tuple

Colour = Tuple[int, int, int]

class colour:
	Colour = Colour

	BLACK:      Colour =   0,   0,   0
	DARK_GREY:  Colour =  63,  63,  63
	GREY:       Colour = 127, 127, 127
	LIGHT_GREY: Colour = 191, 191, 191
	WHITE:      Colour = 255, 255, 255

	RED:   Colour = 255,   0,   0
	GREEN: Colour =   0, 255,   0
	BLUE:  Colour =   0,   0, 255

	CYAN:    Colour =   0, 255, 255
	MAGENTA: Colour = 255,   0, 255
	YELLOW:  Colour = 255, 255,   0

	class flat_ui:
		class gb:
			PROTOSS_PYLON: Colour =   0, 168, 255
			VANADYL_BLUE:  Colour = 156, 136, 255

			NASTURCIAN_FLOWER:      Colour = 232, 65, 24
			HARLEY_DAVIDSON_ORANGE: Colour = 194, 54, 22

			PERIWINKLE:  Colour = 156, 136, 255
			MATT_PURPLE: Colour = 140, 122, 230

			LYNX_WHITE:      Colour = 245, 246, 250
			HINT_OF_PENSIVE: Colour = 220, 221, 225

			RISE_N_SHINE:     Colour = 251, 197, 49
			NANOHANACHA_GOLD: Colour = 225, 177, 44

			BLUEBERRY_SODA:  Colour = 127, 143, 166
			CHAIN_GANG_GREY: Colour = 113, 128, 147

			DOWNLOAD_PROGRESS: Colour = 76, 209, 55
			SKIRRET_GREEN:     Colour = 68, 189, 50

			MAZARINE_BLUE: Colour = 39, 60, 117
			PICO_VOID:     Colour = 25, 42,  86

			SEABROOK: Colour = 72, 126, 176
			NAVAL:    Colour = 64, 115, 158

			BLUE_NIGHTS:     Colour = 53, 59, 72
			ELECTROMAGNETIC: Colour = 47, 54, 64


	def __getitem__(self, key):
		return {
			'BLACK': colour.BLACK,
			'DARK_GREY': colour.DARK_GREY,
			'GREY': colour.GREY,
			'LIGHT_GREY': colour.LIGHT_GREY,
			'WHITE': colour.WHITE,

			'RED': colour.RED,
			'GREEN': colour.GREEN,
			'BLUE': colour.BLUE,

			'CYAN': colour.CYAN,
			'MAGENTA': colour.MAGENTA,
			'YELLOW': colour.YELLOW,


			# --- Flat UI Colours ---
			# GB
			'GB.PROTOSS_PYLON': colour.flat_ui.gb.PROTOSS_PYLON,
			'GB.VANADYL_BLUE': colour.flat_ui.gb.VANADYL_BLUE,

			'GB.NASTURCIAN_FLOWER': colour.flat_ui.gb.NASTURCIAN_FLOWER,
			'GB.HARLEY_DAVIDSON_ORANGE': colour.flat_ui.gb.HARLEY_DAVIDSON_ORANGE,

			'GB.PERIWINKLE': colour.flat_ui.gb.PERIWINKLE,
			'GB.MATT_PURPLE': colour.flat_ui.gb.MATT_PURPLE,

			'GB.LYNX_WHITE': colour.flat_ui.gb.LYNX_WHITE,
			'GB.HINT_OF_PENSIVE': colour.flat_ui.gb.HINT_OF_PENSIVE,

			'GB.RISE_N_SHINE': colour.flat_ui.gb.RISE_N_SHINE,
			'GB.NANOHANACHA_GOLD': colour.flat_ui.gb.NANOHANACHA_GOLD,

			'GB.BLUEBERRY_SODA': colour.flat_ui.gb.BLUEBERRY_SODA,
			'GB.CHAIN_GANG_GREY': colour.flat_ui.gb.CHAIN_GANG_GREY,

			'GB.DOWNLOAD_PROGRESS': colour.flat_ui.gb.DOWNLOAD_PROGRESS,
			'GB.SKIRRET_GREEN': colour.flat_ui.gb.SKIRRET_GREEN,

			'GB.MAZARINE_BLUE': colour.flat_ui.gb.MAZARINE_BLUE,
			'GB.PICO_VOID': colour.flat_ui.gb.PICO_VOID,

			'GB.SEABROOK': colour.flat_ui.gb.SEABROOK,
			'GB.NAVAL': colour.flat_ui.gb.NAVAL,

			'GB.BLUE_NIGHTS': colour.flat_ui.gb.BLUE_NIGHTS,
			'GB.ELECTROMAGNETIC': colour.flat_ui.gb.ELECTROMAGNETIC,
		}.get(key, colour.BLACK)

colour = colour()
