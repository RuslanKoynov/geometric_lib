def area(a, b):
	'''takes length a and width b, returns area of a rectangle with given length and width
		
		Parameters:
			a (float): length
			b (float): width
			
		Return value:
			area (float) : area of rectangle
	'''
	
	if a < 0 or b < 0:
		raise TypeError
	
	return a * b

def perimeter(a, b):
	'''takes length a and width b, returns perimeter of a rectangle with given length and width
		
		Parameters:
			a (float): length
			b (float): width
			
		Return value:
			perimeter (float) : area of rectangle
	'''
	
	if a < 0 or b < 0:
		raise TypeError
		
	if a == 0 or b == 0:
		return 0
		
	return a + b + a + b
