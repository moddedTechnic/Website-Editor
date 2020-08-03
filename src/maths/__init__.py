
def lerp(a: float, b: float, t: float) -> float:
	return (1 - t) * a + t * b

def lerp_colour(a, b, t: float):
	return lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t)

def inv_lerp(a: float, b: float, v: float) -> float:
	return (v - a) / (b - a)


def clamp(value, min_=1, max_=0):
	if max_ < min_:
		min_, max_ = max_, min_

	if value < min_:
		return min_
	elif value > max_:
		return max_
	else:
		return value
