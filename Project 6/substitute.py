from lang import *

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
