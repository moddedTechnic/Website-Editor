from pygame import Rect, Surface
from pygame.draw import rect as draw_rect
from pygame.gfxdraw import (
    aacircle,
    filled_circle
)

from window.constants import constants
Colour = constants.colour.Colour


def rounded_rect(surface: Surface, rect: Rect, colour: Colour, corner_radius: int):
    ''' Draw a rectangle with rounded corners.
    Would prefer this: 
        pygame.draw.rect(surface, colour, rect, border_radius=corner_radius)
    but this option is not yet supported in my version of pygame so do it ourselves.

    We use anti-aliased circles to make the corners smoother
    '''
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    corner_radius = int(corner_radius)

    # need to use anti aliasing circle drawing routines to smooth the corners
    aacircle(surface, rect.left  + corner_radius,     rect.top + corner_radius,        corner_radius, colour)
    aacircle(surface, rect.right - corner_radius - 1, rect.top + corner_radius,        corner_radius, colour)
    aacircle(surface, rect.left  + corner_radius,     rect.bottom - corner_radius - 1, corner_radius, colour)
    aacircle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius, colour)

    filled_circle(surface, rect.left + corner_radius,      rect.top + corner_radius,        corner_radius, colour)
    filled_circle(surface, rect.right - corner_radius - 1, rect.top + corner_radius,        corner_radius, colour)
    filled_circle(surface, rect.left + corner_radius,      rect.bottom - corner_radius - 1, corner_radius, colour)
    filled_circle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius, colour)

    rect_tmp = Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    draw_rect(surface, colour, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    draw_rect(surface, colour, rect_tmp)
