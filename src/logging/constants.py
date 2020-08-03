from typing import NewType

def base(n: int) -> str:
	return u'\u001b[' + str(n)

class constants:
	class style:
		class colour:
			BLACK:   str = u'\u001b[30m'
			RED:     str = u'\u001b[31m'
			GREEN:   str = u'\u001b[32m'
			YELLOW:  str = u'\u001b[33m'
			BLUE:    str = u'\u001b[34m'
			MAGENTA: str = u'\u001b[35m'
			CYAN:    str = u'\u001b[36m'
			WHITE:   str = u'\u001b[37m'

			BRIGHT_BLACK:   str = u'\u001b[30;1m'
			BRIGHT_RED:     str = u'\u001b[31;1m'
			BRIGHT_GREEN:   str = u'\u001b[32;1m'
			BRIGHT_YELLOW:  str = u'\u001b[33;1m'
			BRIGHT_BLUE:    str = u'\u001b[34;1m'
			BRIGHT_MAGENTA: str = u'\u001b[35;1m'
			BRIGHT_CYAN:    str = u'\u001b[36;1m'
			BRIGHT_WHITE:   str = u'\u001b[37;1m'

			COLOURS_8 = [u'\u001b[38;5;' + str(x) + 'm' for x in range(256)]

			RESET:   str = u'\u001b[0m'

		BOLD:      str = u'\u001b[1m'
		UNDERLINE: str = u'\u001b[4m'
		REVERSED:  str = u'\u001b[7m'

	class cursor:
		@classmethod
		def up(cls, n: int) -> str:
			return base(n) + 'A'

		@classmethod
		def down(cls, n: int) -> str:
			return base(n) + 'B'

		@classmethod
		def right(cls, n: int) -> str:
			return base(n) + 'C'

		@classmethod
		def left(cls, n: int) -> str:
			return base(n) + 'D'

	class clear:
		mode = NewType('mode', int)

		SCREEN_END:   mode = 0
		SCREEN_START: mode = 1
		SCREEN_WHOLE: mode = 2

		@classmethod
		def screen(cls, n: mode) -> str:
			return base(n) + 'J'
			
		LINE_END:   mode = 0
		LINE_START: mode = 1
		LINE_WHOLE: mode = 2
			
		@classmethod
		def line(cls, n: mode) -> str:
			return base(n) + 'K'

	@classmethod
	def next_line(cls, n: int) -> str:
		return base(n) + 'E'

	@classmethod
	def prev_line(cls, n: int) -> str:
		return base(n) + 'F'
	
	@classmethod
	def set_col(cls, n: int) -> str:
		return base(n) + 'G'

	@classmethod
	def next_line(cls, n: int, m: int) -> str:
		return base(n) + str(m) + 'H'
