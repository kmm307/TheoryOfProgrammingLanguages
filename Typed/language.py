class Type:
  # Represents a type in the language.
  #
  # T ::= Bool                     -- type of bools
  #       Int                      -- type of ints
  #       T1 -> T2                 -- type of abstractions
  #       (T1, T2, ..., Tn) -> T0  -- type of lambdas
  pass

class BoolType(Type):
  def __str__(self):
    return "Bool"

class IntType(Type):
  def __str__(self):
    return "Int"

class ArrowType(Type):
  def __init__(self, t1, t2):
    self.parm = t1
    self.ret = t2
  
  def __str__(self):
    return f"({self.lhs} -> {self.rhs}"

class FnType(Type):
  def __init__(self, parms, ret):
    self.parms = parms
    self.ret = ret

boolType = BoolType()

intType = IntType()


class Expr:

  pass

class BoolExpr(Expr):
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return "true" if self.val else "false"

class AndExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} or {self.rhs})"

class NotExpr(Expr):
  def __init__(self, e1):
    self.expr = expr(e1)

  def __str__(self):
    return f"(not {self.expr})"

class IfExpr(Expr):
  def __init__(self, e1, e2, e3):
    self.cond = expr(e1)
    self.true = expr(e2)
    self.false = expr(e3)

  def __str__(self):
    return f"(if {self.cond} then {self.true} else {self.false})"

class IdExpr(Expr):
  def __init__(self, x):
    if type(x) is str:
      self.id = x
      self.ref = None
    elif type(x) is VarDecl:
      self.id = x.id
      self.ref = x

  def __str__(self):
    return self.id

class VarDecl:
  def __init__(self, id, t):
    self.id = id
    self.type = t

  def __str__(self):
    return self.id

class AbsExpr(Expr):
  def __init__(self, var, e1):
    self.var = decl(var)
    self.expr = expr(e1)

  def __str__(self):
    return f"\\{self.var}.{self.expr}"

class AppExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} {self.rhs})"

class LambdaExpr(Expr):
  def __init__(self, vars, e1):
    self.vars = list(map(decl, vars))
    self.expr = expr(e1)

  def __str__(self):
    parms = ",".join(str(v) for v in self.vars)
    return f"\\({parms}).{self.expr}"

class CallExpr(Expr):

  def __init__(self, fn, args):
    self.fn = expr(fn)
    self.args = list(map(expr, args))

  def __str__(self):
    args = ",".join(str(a) for a in self.args)
    return f"{self.fn} ({args})"

class PlaceholderExpr(Expr):
  def __str__(self):
    return "_"

def expr(x):

  if type(x) is bool:
    return BoolExpr(x)
  if type(x) is str:
    return IdExpr(x)
  return x

def decl(x):
  if type(x) is str:
    return VarDecl(x)
  return x

#Lookup

def lookup(id, stk):

  for scope in reversed(stk):
    if id in scope:
      return scope[id]
  return None

def resolve(e, stk = []):

  if type(e) is BoolExpr:
    return e

  if type(e) is AndExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is OrExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is NotExpr:
    resolve(e.expr, stk)
    return e

  if type(e) is IfExpr:
    resolve(e.cond, stk)
    resolve(e.true, stk)
    resolve(e.false, stk)
    return e

  if type(e) is IdExpr:
    decl = lookup(e.id, stk)
    if not decl:
      raise Exception("name lookup error")

    e.ref = decl
    return e

  if type(e) is AbsExpr:
    resolve(e.expr, stk + [{e.var.id : e.var}])
    return e

  if type(e) is AppExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e

  if type(e) is LambdaExpr:
    resolve(e.expr, stk + [{var.id : var for var in e.vars}])
    return e

  if type(e) is CallExpr:
    resolve(e.fn, stk)
    for a in e.args:
      resolve(e.fn, stk)
    return e

  assert False

#Substitute

def subst(e, s):
  if type(e) is BoolExpr:
    return e

  if type(e) is AndExpr:
    e1 = subst(e.lhs, s)
    e2 = subst(e.rhs, s)
    return AndExpr(e1, e2)

  if type(e) is OrExpr:
    e1 = subst(e.lhs, s)
    e2 = subst(e.rhs, s)
    return OrExpr(e1, e2)

  if type(e) is NotExpr:
    e1 = subst(e.expr, s)
    return NotExpr(e1)

  if type(e) is IfExpr:
    e1 = subst(e.cond, s)
    e2 = subst(e.true, s)
    e3 = subst(e.false, s)
    return IfExpr(e1, e2, e3)

  if type(e) is IdExpr:
    if e.ref in s:
      return s[e.ref]
    else:
      return e

  if type(e) is AbsExpr:
    e1 = subst(e.expr, s)
    return AbsExpr(e.var, e1)

  if type(e) is AppExpr:
    e1 = subst(e.lhs, s)
    e2 = subst(e.rhs, s)
    return AppExpr(e1, e2)

  if type(e) is LambdaExpr:
    e1 = subst(e.expr, s)
    return LambdaExpr(e.vars, e1)

  if type(e) is CallExpr:
    e0 = subst(e.fn, s)
    args = list(map(lambda x: subst(x, s), e.args))
    return CallExpr(e0, args)

  assert False

#Reduce

def is_value(e):
  return type(e) in (BoolExpr, AbsExpr, LambdaExpr)

def is_reducible(e):
  return not is_value(e)

def step_and(e):
  
  if is_reducible(e.lhs):
    return AndExpr(step(e.lhs), e.rhs)

  if is_reducible(e.rhs):
    return AndExpr(e.lhs, step(e.rhs))

  return BoolExpr(e.lhs.val and e.rhs.val)

def step_or(e):
  
  if is_reducible(e.lhs):
    return OrExpr(step(e.lhs), e.rhs)

  if is_reducible(e.rhs):
    return OrExpr(e.lhs, step(e.rhs))

  return BoolExpr(e.lhs.val or e.rhs.val)

def step_not(e):

  if is_reducible(e.expr):
    return NotExpr(step(e.expr))

  return BoolExpr(not e.expr.val)

def step_if(e):

  if is_reducible(e.cond):
    return NotExpr(step(e.cond), e.true, e.false)

  if e.cond.val:
    return e.true
  else:
    return e.false

def step_app(e):

  
  if is_reducible(e.lhs): 
    return AppExpr(step(e.lhs), e.rhs)

  if type(e.lhs) is not AbsExpr:
    raise Exception("application of non-lambda")

  if is_reducible(e.rhs): 
    return AppExpr(e.lhs, step(e.rhs))

  s = {
    e.lhs.var: e.rhs
  }
  return subst(e.lhs.expr, s);

def step_call(e):


  if is_reducible(e.fn):
    return CallExpr(step(e.fn), e.args)

  if len(e.args) < len(e.fn.vars):
    raise Exception("too few arguments")
  if len(e.args) > len(e.fn.vars):
    raise Exception("too many arguments")

  for i in range(len(e.args)):
    if is_reducible(e.args[i]):
      return CallExpr(e.fn, e.args[:i] + [step(e.args[i])] + e.args[i+1:])

  s = {}
  for i in range(len(e.args)):
    s[e.fn.vars[i]] = e.args[i]

  return subst(e.fn.expr, s);


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

  if type(e) is AppExpr:
    return step_app(e)

  if type(e) is CallExpr:
    return step_call(e)

  assert False

def reduce(e):
  while not is_value(e):
    e = step(e)
    print(e)
  return e

#Evaluate

class Closure:

  def __init__(self, abs, env):
    self.abs = abs
    self.env = clone(env)

def eval_bool(e, store):

  return e.val

def eval_and(e, store):
 
  return evaluate(e.lhs, store) and evaluate(e.rhs, store)

def eval_or(e, store):
  
  return evaluate(e.lhs, store) or evaluate(e.rhs, store)

def eval_not(e, store):
  return not evaluate(e.expr, store)

def eval_cond(e, store):
  if evaluate(e.cond):
    return evaluate(e.true);
  else:
    return evaluate(e.false);

def eval_id(e, store):
 
  return store[e.ref]

def eval_abs(e, store):

  return Closure(e, store)

def eval_app(e, store):

  c = evaluate(e.lhs, store)

  if type(c) is not Closure:
    raise Exception("cannot apply a non-closure to an argument")

  v = evaluate(e.rhs, store)

  return evaluate(c.abs.expr, c.env + {c.abs.var: v})

def eval_lambda(e, store):
  
  return Closure(e, store)

def eval_call(e, store):
  c = evaluate(e.fn, store)
  
  if type(c) is not Closure:
    raise Exception("cannot apply a non-closure to an argument")

  args = []
  for a in e.args:
    args += [evaluate(a, store)]

  env = clone(c.env)
  for i in range(len(args)):
    env[c.abs.vars[i]] = args[i]

  return evaluate(c.abs.expr, env)

def evaluate(e, store = {}):


  if type(e) is BoolExpr:
    return eval_bool(e, store)

  if type(e) is AndExpr:
    return eval_and(e, store)

  if type(e) is OrExpr:
    return eval_or(e, store)

  if type(e) is NotExpr:
    return eval_not(e, store)

  if type(e) is IdExpr:
    return eval_id(e, store)

  if type(e) is AbsExpr:
    return eval_abs(e, store)

  if type(e) is AppExpr:
    return eval_app(e, store)

  if type(e) is LambdaExpr:
    return eval_lambda(e, store)

  if type(e) is CallExpr:
    return eval_call(e, store)
