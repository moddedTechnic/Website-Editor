from os.path import (
	abspath, dirname,
	join
)

from pygame import Rect
from pygame.font import Font

# def draw_text(surface, text, font, size, x, y, c, bg = None):
# 	text_surface = Font(font, size).render(text, True, c, bg)
# 	text_rect = text_surface.get_rect()
# 	text_rect.center = x, y
# 	surface.blit(text_surface, text_rect)

def draw_text(surface, text, font, rect, color, bkg=None):
	aa = True

	rect = Rect(rect)
	y = rect.top
	lineSpacing = -2

	# get the height of the font
	fontHeight = font.size("Tg")[1]

	while text:
		i = 1

		# determine if the row of text will be outside our area
		if y + fontHeight > rect.bottom:
			break

		# determine maximum width of line
		while font.size(text[:i])[0] < rect.width and i < len(text):
			i += 1

		# if we've wrapped the text, then adjust the wrap to the last word      
		if i < len(text): 
			i = text.rfind(" ", 0, i) + 1

		# render the line and blit it to the surface
		if bkg:
			image = font.render(text[:i], 1, color, bkg)
			image.set_colorkey(bkg)
		else:
			image = font.render(text[:i], aa, color)

		surface.blit(image, (rect.left, y))
		y += fontHeight + lineSpacing

		# remove the text we just blitted
		text = text[i:]

	return text


class fonts:
	FONTS_DIR: str = join(dirname(dirname(dirname(dirname(abspath(__file__))))), 'assets', 'fonts')

	ANONYMOUS_PRO_REGULAR: str = join(FONTS_DIR, 'AnonymousPro-Regular.ttf')
