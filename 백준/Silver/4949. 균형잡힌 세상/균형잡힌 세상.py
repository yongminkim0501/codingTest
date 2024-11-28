class stack:
  def __init__(self):
    self.stk = []
    self.top_idx = 0

  def push(self, x):
    self.stk.append(x)
    self.top_idx += 1
  def pop(self):
    if self.isEmpty() == True:
      return None
    else:
      self.top_idx -= 1
      return self.stk.pop()
  def isEmpty(self):
    if self.top_idx == 0:
      return True
    else:
      return False
  def top(self):
    return self.stk[self.top_idx-1]
  def clear(self):
    self.stk = []
    self.top_idx = 0


tmp = stack()
while(True):
  t = input()
  flag = True
  flag_c = True
  flag_d = True
  if t == "." : break
  else:
    tmp.clear()
    for s in t:
      if s == "(" or s == "[":
        tmp.push(s)
      elif s == ")" :
        if tmp.isEmpty() == True:
          flag = False
          flag_c = False
          print("no")
          break
        else:
          if tmp.top() == "(":
            tmp.pop()
          else:
            flag = False
            flag_d = False
            break
      elif s == "]":
        if tmp.isEmpty() == True :
          flag = False
          flag_c = False
          print("no")
          break
        else:
          if tmp.top() == "[":
            tmp.pop()
          else:
            flag = False
            flag_d = False
            break
    if flag == True and len(tmp.stk) == 0:
      print("yes")
    else:
      if (flag_c != False and flag_d == True) or (flag_c == True and flag_d == False):
        print("no")