class Type:
  # Represents a type in the language.
  #
  # T ::= Bool | Int
  pass

class BoolType(Type):
  # Represents the type 'Bool'
  def __str__(self):
    return "Bool"

class IntType(Type):
  # Represents the type 'Int'
  def __str__(self):
    return "Int"

class Expr:
  # Represents the set of expressions in the
  # pure (or untyped) lambda calculus. This is
  # defined as:
  #
  #   e ::= b                     -- boolean literals (true and false)
  #         e1 and e2             -- logical and
  #         e1 or e2              -- logical or
  #         not e1                -- logical negation
  #         if e1 then e2 else e3 -- conditionals
  #         n                     -- integer literals
  #         e1 + e2               -- addition
  #         e1 - e2               -- subtraction
  #         e1 * e2               -- multiplication
  #         e1 / e2               -- quotient of division
  #         e1 % e2               -- remainder of division
  #         -e1                   -- negation
  #         e1 == e2              -- equality
  #         e1 != e2              -- distinction
  #         e1 < e2               -- less than
  #         e1 > e2               -- greater than
  #         e1 <= e2              -- less than or equal to
  #         e1 >= e2              -- greater than or equal to
  def __init__(self):
    # The type of the expression. This is computed 
    # by the check() function.
    self.type = None

## Boolean expressions

class BoolExpr(Expr):
  def __init__(self, val):
    Expr.__init__(self)
    self.value = val

  def __str__(self):
    return "true" if self.value else "false"

class AndExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} or {self.rhs})"

class NotExpr(Expr):
  def __init__(self, e):
    Expr.__init__(self)
    self.expr = expr(e)

  def __str__(self):
    return f"(not {self.expr})"

class IfExpr(Expr):
  # Represents expressions of the form `if e1 then e2 else e3`.
  def __init__(self, e1, e2, e3):
    Expr.__init__(self)
    self.cond = express(e1)
    self.true = express(e2)
    self.false = express(e3)

  def __str__(self):
    return f"(if {self.cond} then {self.true} else {self.false})"

## Integer expressions

class IntExpr(Expr):
  # Represents numeric literals.
  def __init__(self, val):
    Expr.__init__(self)
    self.value = val

  def __str__(self):
    return str(self.value)

class AddExpr(Expr):
  # Represents expressions of the form `e1 + e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} + {self.rhs})"

class SubExpr(Expr):
  # Represents expressions of the form `e1 + e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} + {self.rhs})"

class MulExpr(Expr):
  # Represents expressions of the form `e1 - e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} - {self.rhs})"

class DivExpr(Expr):
  # Represents expressions of the form `e1 / e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} / {self.rhs})"

class RemExpr(Expr):
  # Represents expressions of the form `e1 % e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} % {self.rhs})"

class NegExpr(Expr):
  # Represents expressions of the form `-e1`.
  def __init__(self, e1):
    Expr.__init__(self)
    self.expr = expr(e1)

  def __str__(self):
    return f"(-{self.expr})"

## Relational expressions

class EqExpr(Expr):
  # Represents expressions of the form `e1 == e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} == {self.rhs})"

class NeExpr(Expr):
  # Represents expressions of the form `e1 != e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} != {self.rhs})"

class LtExpr(Expr):
  # Represents expressions of the form `e1 < e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} < {self.rhs})"

class GtExpr(Expr):
  # Represents expressions of the form `e1 > e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} > {self.rhs})"

class LeExpr(Expr):
  # Represents expressions of the form `e1 <= e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} <= {self.rhs})"

class GeExpr(Expr):
  # Represents expressions of the form `e1 >= e2`.
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} >= {self.rhs})"


def expr(x):
  # Turn a Python object into an expression. This is solely
  # used to make simplify the writing expressions.
  if type(x) is bool:
    return BoolExpr(x)
  if type(x) is int:
    return IntExpr(x)
  if type(x) is str:
    return IdExpr(x)
  return x

  #Reduce
  def is_value(e):
  # Returns true if the expression is designated as a value (i.e., 
  # that the expression is irreducible).
  return type(e) in (BoolExpr, IntExpr)

def is_reducible(e):
  # Returns true if the expression is reducible.
  return not is_value(e)

def step_unary(e, Node, op):
  # Compute the next step of a unary expression.
  #
  #     e1 ~> e1'
  # ----------------- Not-1
  # op e1 ~> op e1'
  #
  # ----------------- Not-1
  # op v1 ~> [op `v1`]
  if is_reducible(e.expr):
    return Node(step(e.expr))

  return expr(op(e.expr.value))

def step_binary(e, Node, op):
  # Compute the next step of a binary expression.
  #
  #   ---------------------------
  #   v1 op v2 ~> [`v1` op `v2`]
  #
  #          e1 ~> e1'
  #   -----------------------
  #   e1 op e2 ~> e1' op e2
  #
  #          e2 ~> e2'
  #   -----------------------
  #   v1 op e2 ~> v1 op e2'
  
  # LHS first
  if is_reducible(e.lhs):
    return Node(step(e.lhs), e.rhs)

  # RHS next
  if is_reducible(e.rhs):
    return Node(e.lhs, step(e.rhs))

  # Combine the results.
  return expr(op(e.lhs.value, e.rhs.value))

def step_and(e):
  return step_binary(e, AndExpr, lambda x, y: x and y)

def step_or(e):
  return step_binary(e, OrExpr, lambda x, y: x or y)

def step_not(e):
  return step_unary(e, NotExpr, lambda x: not x)

def step_if(e):
  # Compute the next step of a not expression.
  #
  #                     e1 ~> e1'
  # ---------------------------------------------- Cond-1
  # if e1 then e2 else e3 ~> if e1' then e2 else e3
  #
  # ------------------------------ Cond-true
  # if true then e2 else e3 ~> e2
  #
  # ------------------------------ Cond-true
  # if false then e2 else e3 ~> e3
  #
  # Note that this selects either e2 or e3, but does not "advance"
  # the selected expression.

  if is_reducible(e.cond):
    return NotExpr(step(e.cond), e.true, e.false)

  if e.cond.val:
    return e.true
  else:
    return e.false

def step_add(e):
  return step_binary(e, AddExpr, lambda x, y: x + y)

def step_sub(e):
  return step_binary(e, SubExpr, lambda x, y: x - y)

def step_mul(e):
  return step_binary(e, MulExpr, lambda x, y: x * y)

def step_div(e):
  return step_binary(e, DivExpr, lambda x, y: x / y)

def step_rem(e):
  return step_binary(e, RemExpr, lambda x, y: x % y)

def step_eq(e):
  return step_binary(e, EqExpr, lambda x, y: x == y)

def step_ne(e):
  return step_binary(e, NeExpr, lambda x, y: x != y)

def step_lt(e):
  return step_binary(e, LtExpr, lambda x, y: x < y)

def step_gt(e):
  return step_binary(e, GtExpr, lambda x, y: x > y)

def step_le(e):
  return step_binary(e, LeExpr, lambda x, y: x <= y)

def step_ge(e):
  return step_binary(e, GeExpr, lambda x, y: x >= y)

def step(e):
  assert isinstance(e, Expr)
  assert is_reducible(e)

  if type(e) is AndExpr:
    return step_and(e)

  if type(e) is OrExpr:
    return step_or(e)

  if type(e) is NotExpr:
    return step_not(e)

  if type(e) is IfExpr:
    return step_if(e)

  if type(e) is AddExpr:
    return step_add(e)

  if type(e) is SubExpr:
    return step_sub(e)

  if type(e) is MulExpr:
    return step_mul(e)

  if type(e) is DivExpr:
    return step_div(e)

  if type(e) is RemExpr:
    return step_rem(e)

  if type(e) is NegExpr:
    return step_neg(e)

  if type(e) is EqExpr:
    return step_eq(e)

  if type(e) is NeExpr:
    return step_ne(e)

  if type(e) is LtExpr:
    return step_lt(e)

  if type(e) is GtExpr:
    return step_gt(e)

  if type(e) is LeExpr:
    return step_le(e)

  if type(e) is GeExpr:
    return step_ge(e)

  assert False

def reduce(e):
  while not is_value(e):
    e = step(e)
    print(e)
  return e

  #Check
  boolType = BoolType()

# The (only) integer type
intType = IntType()

def is_bool(x):
  # Returns true if x either is boolType (when
  # x is a Type) or if x has boolType (when x
  # is an expression). The latter case will
  # recursively compute the the type of the
  # expression as a "convenience".
  if isinstance(x, Type):
    return x == boolType
  if isinstance(x, Expr):
    return is_bool(check(x))

def is_int(x):
  # Same as above, but for int.
  if isinstance(x, Type):
    return x == intType
  if isinstance(x, Expr):
    return is_int(check(x))

def is_same_type(t1, t2):
  # Returns true if t1 and t2 are the same
  # type (if both are types).

  # Quick reject. t1 and t2 are not objects
  # of the same type.
  if type(t1) is not type(t2):
    return False

  if type(t1) is BoolType:
    return True
  
  if type(t1) is IntType:
    return True

  assert False

def has_same_type(e1, e2):
  # Returns true if e1 and e2 have the
  # same type (recursively computing the
  # types of both expressions.)
  return is_same_type(check(e1), check(e2))

def check_bool(e):
  # -------- T-Bool
  # b : Bool
  return boolType

def check_int(e):
  # -------- T-Int
  # n : Int
  return intType

def check_and(e):
  # e1 : Bool   e2 : Bool
  # --------------------- T-And
  #   e1 and e2 : Bool
  if is_bool(e1) and is_bool(e2):
    return boolType
  raise Exception("invalid operands to 'and'")

def check_add(e):
  # e1 : Int   e2 : Int
  # ------------------- T-Add
  #   e1 + e2 : Int
  if is_int(e.lhs) and is_int(e.rhs):
    return intType
  raise Exception("invalid operands to '+'")

def check_sub(e):
  # e1 : Int   e2 : Int
  # ------------------- T-Sub
  #   e1 - e2 : Int
  if is_int(e.lhs) and is_int(e.rhs):
    return intType
  raise Exception("invalid operands to '-'")

def check_eq(e):
  # e1 : T1   e2 : T2
  # ----------------- T-Eq
  #   e1 == e2 : Bool
  if has_same_type(e.lhs, e.rhs):
    return boolType
  raise Exception("invalid operands to '=='")

def do_check(e):
  # Compute the type of e.
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return check_bool(e)

  if type(e) is AndExpr:
    return check_and(e)

  if type(e) is OrExpr:
    return check_or(e)

  if type(e) is NotExpr:
    return check_not(e)

  if type(e) is IfExpr:
    return check_if(e)

  if type(e) is IntExpr:
    return check_int(e)

  if type(e) is AddExpr:
    return check_add(e)

  if type(e) is SubExpr:
    return check_sub(e)

  if type(e) is MulExpr:
    return check_mul(e)

  if type(e) is DivExpr:
    return check_div(e)

  if type(e) is RemExpr:
    return check_rem(e)

  if type(e) is NegExpr:
    return check_neg(e)

  if type(e) is EqExpr:
    return check_eq(e)

  if type(e) is NeExpr:
    return check_ne(e)

  if type(e) is LtExpr:
    return check_lt(e)

  if type(e) is GtExpr:
    return check_gt(e)

  if type(e) is LeExpr:
    return check_le(e)

  if type(e) is GeExpr:
    return check_ge(e)

  assert False


def check(e):
  # Accepts an expression and returns its type.

  # If we've computed the type already, return it.
  if not e.type:
    e.type = do_check(e)

  return e.type

  #Evaluate
def eval_bool(e):
  return e.value

def eval_and(e):
  return evaluate(e.lhs) and evaluate(e.rhs)

def eval_or(e):
  return evaluate(e.lhs) or evaluate(e.rhs)

def eval_not(e):
  return not evaluate(e.expr)

def eval_if(e):
  if evaluate(e.cond):
    return evaluate(e.true);
  else:
    return evaluate(e.false);

def eval_int(e):
  return e.value

def eval_add(e):
  return evaluate(e.lhs) + evaluate(e.rhs)

def eval_sub(e):
  return evaluate(e.lhs) - evaluate(e.rhs)

def eval_mul(e):
  return evaluate(e.lhs) * evaluate(e.rhs)

def eval_div(e):
  return evaluate(e.lhs) / evaluate(e.rhs)

def eval_rem(e):
  return evaluate(e.lhs) % evaluate(e.rhs)

def eval_neg(e):
  return -evaluate(e.expr)

def eval_eq(e):
  return evaluate(e.lhs) == evaluate(e.rhs)

def eval_ne(e):
  return evaluate(e.lhs) != evaluate(e.rhs)

def eval_lt(e):
  return evaluate(e.lhs) < evaluate(e.rhs)

def eval_gt(e):
  return evaluate(e.lhs) > evaluate(e.rhs)

def eval_le(e):
  return evaluate(e.lhs) <= evaluate(e.rhs)

def eval_ge(e):
  return evaluate(e.lhs) >= evaluate(e.rhs)

def evaluate(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return eval_bool(e)

  if type(e) is AndExpr:
    return eval_and(e)

  if type(e) is OrExpr:
    return eval_or(e)

  if type(e) is NotExpr:
    return eval_not(e)

  if type(e) is IfExpr:
    return eval_if(e)

  if type(e) is IntExpr:
    return eval_int(e)

  if type(e) is AddExpr:
    return eval_add(e)

  if type(e) is SubExpr:
    return eval_sub(e)

  if type(e) is MulExpr:
    return eval_mul(e)

  if type(e) is DivExpr:
    return eval_div(e)

  if type(e) is RemExpr:
    return eval_rem(e)

  if type(e) is NegExpr:
    return eval_neg(e)

  if type(e) is EqExpr:
    return eval_eq(e)

  if type(e) is NeExpr:
    return eval_ne(e)

  if type(e) is LtExpr:
    return eval_lt(e)

  if type(e) is GtExpr:
    return eval_gt(e)

  if type(e) is LeExpr:
    return eval_le(e)

  if type(e) is GeExpr:
    return eval_ge(e)

  assert False

