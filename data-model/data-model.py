class Polynomial:
	def __init__(self,*coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{})'.format(self.coeffs)

	def add(self,other):
		return Polynomial(*(x + y for x,y in zip(self.coeffs,other.coeffs)))
	# zip does ?
	def __len__(self):
		return len(self.coeffs)
# some behaviours that i want to implement --> write som e __function__
# data model methods or dunder methods
# top level function /syntax, ---> some corresponding 

# x + y ---> __add__


class Polynomial:
	pass
p1 = Polynomial(1,2,3) 
p2 = Polynomial(3,4,5)
# p1.coeffs = 1,2,3 # x^2 + 2x +3
# p2.coeff = 3,4,3 # 3x^2 + 4x +3		