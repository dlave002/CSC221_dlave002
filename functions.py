def number(a, b):
  if(b <= 0):
    b = 3.14
  sum = a + b
  resarr = []
  if (a < b):
    resarr.append(a)
    resarr.append(b)
  else:
    resarr.append(b)
    resarr.append(a)
  return (sum, resarr)

""" sum,resarr = number(1, 0)
print(sum)
print(resarr) """

def number2(a, b, verbose):
  if(b <= 0):
    b = 3.14
  sum = a + b
  resarr = []
  if (a < b):
    resarr.append(a)
    resarr.append(b)
  else:
    resarr.append(b)
    resarr.append(a)
  if (verbose):
    return (sum, resarr, "verbose is true")
  else:
    return ("Sum is not Available because of Verbose is false", "array is not Available because of Verbose is false", "Verbose is false ")

""" sum,resarr, verbose = number(1, -2, True)
print(sum)
print(resarr)
print(verbose) """
