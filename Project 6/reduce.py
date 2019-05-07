from lang import *

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
