from typing import Tuple

class constants:
	class colour:
		BLACK:      Tuple[int, int, int] =   0,   0,   0
		DARK_GREY:  Tuple[int, int, int] =  63,  63,  63
		GREY:       Tuple[int, int, int] = 127, 127, 127
		LIGHT_GREY: Tuple[int, int, int] = 191, 191, 191
		WHITE:      Tuple[int, int, int] = 255, 255, 255

		RED:   Tuple[int, int, int] = 255,   0,   0
		GREEN: Tuple[int, int, int] =   0, 255,   0
		BLUE:  Tuple[int, int, int] =   0,   0, 255

		CYAN:    Tuple[int, int, int] =   0, 255, 255
		MAGENTA: Tuple[int, int, int] = 255,   0, 255
		YELLOW:  Tuple[int, int, int] = 255, 255,   0

	WIDTH: int = 1280
	HEIGHT: int = 720
