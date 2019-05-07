from lang import *

import copy

clone = copy.deepcopy


class Closure:
  
  def __init__(self, abs, env):
    self.abs = abs
    self.env = clone(env)

  def __str__(self):
    return f"<{str(self.abs)}>"

class Location:
  def __init__(self, ix):
    self.index = ix

  def __str__(self):
    return f"@{self.index}"

class Tuple:
  def __init__(self, vs : list):
    self.values = vs

  def __str__(self):
    vs = ",".join([str(v) for v in self.values])
    return f"{{{vs}}}"

class Field:
  def __init__(self, n, v):
    self.id = n
    self.value = v

  def __str__(self):
    return f"{self.id}={self.value}"

class Record:
  def __init__(self, fs : list):
    self.fields = fs

    self.select = {f.id:f.value for f in fs}

  def __str__(self):
    fs = ",".join([str(e) for e in self.fields])
    return f"{{{fs}}}"

class Variant:
  
  def __init__(self, l, v):
    self.tag = l
    self.value = v

  def __str__(self):
    return f"<{self.tag}={self.value}>"

@checked
def eval_binary(e : Expr, stack : dict, heap : list, fn : object):
 
  v1 = evaluate(e.lhs, stack, heap)
  v2 = evaluate(e.rhs, stack, heap)
  return fn(v1, v2)

@checked
def eval_unary(e : Expr, stack : dict, heap : list, fn : object):
 
  v1 = evaluate(e.lhs, stack, heap)
  return fn(v1)

@checked
def eval_bool(e : Expr, stack : dict, heap : list):
  
  return e.value

@checked
def eval_and(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 and v2)

@checked
def eval_or(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 or v2)

@checked
def eval_not(e : Expr, stack : dict, heap : list):
  return eval_unary(e, stack, heap, lambda v1: not v1)

def eval_cond(e, stack, heap : list):
  if evaluate(e.cond):
    return evaluate(e.true);
  else:
    return evaluate(e.false);

@checked
def eval_int(e : Expr, stack : dict, heap : list):
  return e.value

@checked
def eval_add(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 + v2)

@checked
def eval_sub(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 - v2)

@checked
def eval_mul(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 * v2)

@checked
def eval_div(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 / v2)

@checked
def eval_rem(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 % v2)

@checked
def eval_neg(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1: -v1)

@checked
def eval_eq(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 == v2)

@checked
def eval_ne(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 != v2)

@checked
def eval_lt(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 < v2)

@checked
def eval_gt(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 > v2)

@checked
def eval_le(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 <= v2)

@checked
def eval_ge(e : Expr, stack : dict, heap : list):
  return eval_binary(e, stack, heap, lambda v1, v2: v1 >= v2)

@checked
def eval_id(e : Expr, stack : dict, heap : list):

  return stack[e.ref]

@checked
def eval_lambda(e : Expr, stack : dict, heap : list):
 
  return Closure(e, stack)

def eval_call(e : Expr, stack : dict, heap : list):
  c = evaluate(e.fn, stack, heap)
  
  if type(c) is not Closure:
    raise Exception("cannot apply a non-closure to an argument")

  args = []
  for a in e.args:
    args += [evaluate(a, stack, heap)]

  env = clone(c.env)
  for i in range(len(args)):
    env[c.abs.vars[i]] = args[i]

  return evaluate(c.abs.expr, env, heap)

@checked
def eval_new(e : Expr, stack : dict, heap : list):
  
  v1 = evaluate(e.expr, stack, heap)
  l1 = Location(len(heap))
  heap += [v1]
  return l1

@checked
def eval_deref(e : Expr, stack : dict, heap : list):
 
  l1 = evaluate(e.expr, stack, heap)
  if type(l1) is not Location:
    raise Exception("invalid reference")
  return heap[l1.index]

@checked
def eval_assign(e : Expr, stack : dict, heap : list):
  v2 = evaluate(e.rhs, stack, heap)
  l1 = evaluate(e.lhs, stack, heap)
  if type(l1) is not Location:
    raise Exception("invalid reference")
  heap[l1.index] = v2

@checked

def eval_variant(e : Expr, stack : dict, heap : list):
  v1 = evaluate(e.field.value)
  return Variant(e.field.id, v1)

def eval_case(e : Expr, stack : dict, heap : list):
  v1 = evaluate(e.expr, stack, heap)

  case = None
  for c in e.cases:
    if c.id == v1.tag:
      case = c
      break
  assert case != None

  env = clone(stack)
  env[c.var] = v1.value
  return evaluate(c.expr, env, heap)


def evaluate(e : Expr, stack : dict = {}, heap = []):


  if type(e) is BoolExpr:
    return eval_bool(e, stack, heap)

  if type(e) is AndExpr:
    return eval_and(e, stack, heap)

  if type(e) is OrExpr:
    return eval_or(e, stack, heap)

  if type(e) is NotExpr:
    return eval_not(e, stack, heap)

  if type(e) is IfExpr:
    return eval_if(e, stack, heap)

  # Arithmetic expressions

  if type(e) is IntExpr:
    return eval_int(e, stack, heap)

  if type(e) is AddExpr:
    return eval_add(e, stack, heap)

  if type(e) is SubExpr:
    return eval_sub(e, stack, heap)

  if type(e) is MulExpr:
    return eval_mul(e, stack, heap)

  if type(e) is DivExpr:
    return eval_div(e, stack, heap)

  if type(e) is RemExpr:
    return eval_rem(e, stack, heap)

  if type(e) is NegExpr:
    return eval_neg(e, stack, heap)

  # Relational expressions

  if type(e) is EqExpr:
    return eval_eq(e, stack, heap)

  if type(e) is NeExpr:
    return eval_ne(e, stack, heap)

  if type(e) is LtExpr:
    return eval_lt(e, stack, heap)

  if type(e) is GtExpr:
    return eval_gt(e, stack, heap)

  if type(e) is LeExpr:
    return eval_le(e, stack, heap)

  if type(e) is GeExpr:
    return eval_ge(e, stack, heap)

  # Functional expressions

  if type(e) is LambdaExpr:
    return eval_lambda(e, stack, heap)

  if type(e) is CallExpr:
    return eval_call(e, stack, heap)

  # Reference expressions

  if type(e) is NewExpr:
    return eval_new(e, stack, heap)

  if type(e) is DerefExpr:
    return eval_deref(e, stack, heap)

  if type(e) is AssignExpr:
    return eval_assign(e, stack, heap)

  # Data expressions

  if type(e) is TupleExpr:
    return eval_tuple(e, stack, heap)

  if type(e) is ProjExpr:
    return eval_proj(e, stack, heap)

  if type(e) is RecordExpr:
    return eval_record(e, stack, heap)

  if type(e) is MemberExpr:
    return eval_member(e, stack, heap)

  if type(e) is VariantExpr:
    return eval_variant(e, stack, heap)

  if type(e) is CaseExpr:
    return eval_case(e, stack, heap)

  assert False
