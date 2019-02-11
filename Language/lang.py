"""
Implement the AST for the following language:

e ::= true | false | not e1 | e1 and e2 | e1 or e2

Implement the following operations on the abstract syntax tree:

size -- compute the size of an expression
height -- compute the height of an expression
same -- Return true if two expressions are identical
value -- compute the value of an expression
step -- Return an expression representing a single step of evaluation
reduce -- Calls step repeatedly until the expression is non-reducible
"""

class expr:
	pass


class expr:
	def __inti__ (BoolExpr, NotExpr, AndExpr, OrExpr, Bool):


class NotExpr(Expr):
	def __inti__ (self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
	
	def __str__ (self):
		return f"({self.lhs} != {self.rhs})"

class AndExpr(Expr):
	def __inti__ (self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
	
	def __str__ (self):
		return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
	def __inti__ (self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
	
	def __str__ (self):
		return f"({self.lhs} or {self.rhs})"

#true when e1 and e2 are the same string
class same:
	def same(e1, e2):
		if type(e1) != type(e2):
			return False

#when e1 and e2 have the same type
if type(e1) is BoolExpr:
	return e1.value == e2.value

if type(e1) is NotExpr:
	return same (e1.expr, e2.expr)

if type(e1) is AndExpr:
	return same(e1.lhs, e2.rhs) and same(e1.lhs, e2.rhs)


class value:
	def is_value(e):
		return type(e) is Bool

class reducible:
	def is_reducible(e):
		return not is_value(e)

class step:
	def step(e):
		assert is_reducible(e)


	def step_not(e):
		if type(e.expr) is Bool:
			if e.expr.value == True:
				return BoolExpr(False)
					else:
						return BoolExpr(True)

				return Not(step(e.expr))


				if type(e) is NotExpr:
						return step_not(e)


	def step_and(e):
		if is_value(e.lhs) and is_value(e.rhs):
			return BoolExpr(e.lhs.value and e.rhs.value)

		if is_reducible(e.lhs):
			return AndExpr(step(e.lhs), e.rhs)

		if is_reducible(e.rhs):
			return AndExpr(e.lhs, step(e.rhs))


	def step_or(e):
		if is_value(e.lhs) or is_value(e.rhs):
			return BoolExpr(e.lhs.value or e.rhs.value)

		if is_reducible(e.lhs):
			return AndExpr(step(e.lhs), e.rhs)

		if is_reducible(e.rhs):
			return AndExpr(e.lhs, step(e.rhs))

	
	def reduce(e)
		while is_reducible(e):
			e = step(e)
			return e


		assert False
