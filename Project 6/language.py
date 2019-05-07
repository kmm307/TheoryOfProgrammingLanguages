class VarDecl:
  def __init__(self, id, t):
    self.id = id
    self.type = typify(t)

  def __str__(self):
    return f"{self.id}:{str(self.type)}"

class FieldDecl:
  def __init__(self, id, t):
    self.id = id
    self.type = typify(t)

  def __str__(self):
    return f"{self.id}:{str(self.type)}"

class FieldInit:
  def __init__(self, id, e):
    self.id = id
    self.value = expr(e)

  def __str__(self):
    return f"{self.id}={str(self.value)}"

class Type:
  pass

class BoolType(Type):
  def __str__(self):
    return "Bool"

class IntType(Type):
  def __str__(self):
    return "Int"

class FnType(Type):
  def __init__(self, parms, ret):
    self.parms = list(map(typify, parms))
    self.ret = typify(ret)

  def __str__(self):
    parms = ",".join([str(p) for p in self.parms])
    return f"({parms})->{str(self.ret)}"

class RefType(Type):
  def __init__(self, t):
    self.ref = typify(t)

  def __str__(self):
    return f"Ref {str(self.ref)}"

class TupleType(Type):
  def __init__(self, ts):
    self.elems = list(map(typify, ts))

  def __str__(self):
    es = ",".join([str(t) for t in self.elems])
    return f"{{{es}}}"

class RecordType(Type):
  def __init__(self, fs):
    self.fields = list(map(field, fs))

  def __str__(self):
    fs = ",".join(str(f) for f in self.fields)
    return f"{{{fs}}}"

class VariantType(Type):
  def __init__(self, fs):
    self.fields = list(map(field, fs))

  def __str__(self):
    fs = ",".join(str(f) for f in self.fields)
    return f"<{fs}>"

boolType = BoolType()

intType = IntType()


class Expr:
  def __init__(self):
    self.type = None


class BoolExpr(Expr):
  def __init__(self, val):
    Expr.__init__(self)
    self.value = val

  def __str__(self):
    return "true" if self.value else "false"

class AndExpr(Expr):
  def __init__(self, e1, e2):
    Expr.__init__(self)
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
  def __init__(self, e1, e2):
    Expr.__init__(self)
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} or {self.rhs})"

class NotExpr(Expr):
  def __init__(self, e1):
    Expr.__init__(self)
    self.expr = expr(e1)

  def __str__(self):
    return f"(not {self.expr})"

class IfExpr(Expr):
  def __init__(self, e1, e2, e3):
    Expr.__init__(self)
    self.cond = expr(e1)
    self.true = expr(e2)
    self.false = expr(e3)

  def __str__(self):
    return f"(if {self.cond} then {self.true} else {self.false})"


class IdExpr(Expr):
  def __init__(self, x):
    Expr.__init__(self)
    if type(x) is str:
      self.id = x
      self.ref = None 
    elif type(x) is VarDecl:
      self.id = x.id
      self.ref = x

  def __str__(self):
    return self.id


class IntExpr(Expr):
  def __init__(self, val):
    Expr.__init__(self)
    self.value = val

  def __str__(self):
    return str(self.value)

class AddExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} + {self.rhs})"

class SubExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} + {self.rhs})"

class MulExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} - {self.rhs})"

class DivExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} / {self.rhs})"

class RemExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} % {self.rhs})"

class NegExpr(Expr):
  def __init__(self, e1):
    Expr.__init__(self)
    self.expr = expr(e1)

  def __str__(self):
    return f"(-{self.expr})"


class EqExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} == {self.rhs})"

class NeExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} != {self.rhs})"

class LtExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} < {self.rhs})"

class GtExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} > {self.rhs})"

class LeExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} <= {self.rhs})"

class GeExpr(Expr):
  def __init__(self, lhs, rhs):
    Expr.__init__(self)
    self.lhs = expr(lhs)
    self.rhs = expr(rhs)

  def __str__(self):
    return f"({self.lhs} >= {self.rhs})"


class LambdaExpr(Expr):
 
  def __init__(self, vars, e1):
    Expr.__init__(self)
    self.vars = list(map(decl, vars))
    self.expr = expr(e1)

  def __str__(self):
    parms = ",".join(str(v) for v in self.vars)
    return f"\\({parms}).{self.expr}"

class CallExpr(Expr):
 
  def __init__(self, fn, args):
    Expr.__init__(self)
    self.fn = expr(fn)
    self.args = list(map(expr, args))

  def __str__(self):
    args = ",".join(str(a) for a in self.args)
    return f"{self.fn} ({args})"

class PlaceholderExpr(Expr):
  def __init__(self):
    Expr.__init__(self)

  def __str__(self):
    return "_"


class NewExpr(Expr):

  def __init__(self, e):
    Expr.__init__(self)
    self.expr = expr(e)

  def __str__(self):
    return f"new {self.expr}"

class DerefExpr(Expr):

  def __init__(self, e):
    Expr.__init__(self)
    self.expr = expr(e)

  def __str__(self):
    return f"*{self.expr}"

class AssignExpr(Expr):
  # Represents assignment.
  def __init__(self, e1, e2):
    Expr.__init__(self)
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"{self.lhs} = {self.rhs}"

# Data expressions
class TupleExpr(Expr):
  def __init__(self, es):
    Expr.__init__(self)
    self.elems = list(map(expr, es))

  def __str__(self):
    es = ",".join(str(e) for e in self.elems)
    return f"{{{es}}}"

class ProjExpr(Expr):
  def __init__(self, e1, n):
    Expr.__init__(self)
    self.obj = e1
    self.index = n

  def __str__(self):
    return f"{str(self.obj)}.{self.index}"

class RecordExpr(Expr):
  def __init__(self, fs):
    Expr.__init__(self)
    self.fields = list(map(init, fs))

  def __str__(self):
    fs = ",".join(str(e) for e in self.fields)
    return f"{{{fs}}}"

class MemberExpr(Expr):
  def __init__(self, e1, id):
    Expr.__init__(self)
    self.obj = e1
    self.id = id


    self.Ref = None

  def __str__(self):
    return f"{str(self.obj)}.{self.id}"

class VariantExpr(Expr):

  def __init__(self, f, t):
    Expr.__init__(self)
    self.field = init(f)
    self.variant = typify(t)

  def __str__(self):
    return f"<{str(self.field)}> as {str(self.type)}"

class Case:
 
  def __init__(self, id, n, e):
    self.id = id 
    self.var = VarDecl(n, None) 
    self.expr = expr(e) 
  
  def __str__(self):
    return f"<{str(self.id)}={str(self.var)}> => {str(self.expr)}"

class CaseExpr(Expr):
  def __init__(self, e, cs):
    Expr.__init__(self)
    self.expr = expr(e)
    self.cases = list(map(case, cs))

  def __str__(self):
    cs = " | ".join([str(c) for c in self.cases])
    return f"case {str(self.expr)} of {cs}"

def typify(x):
  if x is bool:
    return BoolType()
  if x is int:
    return IntType()
  return x

def expr(x):
  if type(x) is bool:
    return BoolExpr(x)
  if type(x) is int:
    return IntExpr(x)
  if type(x) is str:
    return IdExpr(x)
  return x

def decl(x):
  if type(x) is str:
    return VarDecl(x)
  return x

def field(x):
  if type(x) is tuple:
    return FieldDecl(x[0], x[1])
  return x

def init(x):
  if type(x) is tuple:
    return FieldInit(x[0], x[1])
  return x

def case(x):
  if type(x) is tuple:
    return Case(x[0], x[1], x[2])
  return x

from lookup import resolve
from check import check
from subst import subst
from reduce import step, reduce
from evaluate import evaluate
