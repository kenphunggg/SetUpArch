def test(var1, var2, var3 = None, var4 = None):
  if var3 is None:
    print("var 3 is None")
  elif var4 is None:
    print("var 4 is None")
  else:
    print("Completed")

test(1, 2, var3 = 3, var4 = None)