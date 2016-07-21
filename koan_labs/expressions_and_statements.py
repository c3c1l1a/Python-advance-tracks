import math
def compounded_principal(time):
	principle=10000.0
	rate =8.0
	amount = principle *  ((1.0 + rate/100.0)**time)
	return math.floor(amount)
