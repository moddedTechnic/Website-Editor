from typing import Tuple

Colour = Tuple[int, int, int]

class constants:
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

	WIDTH: int = 1280
	HEIGHT: int = 720
