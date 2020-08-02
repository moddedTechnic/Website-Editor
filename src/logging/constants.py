
class constants:
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
