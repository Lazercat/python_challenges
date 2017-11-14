def fib(x):
  if(x<=1):
    return x
  else:
    return (fib(x-1)+fib(x-2))
x = int(input("Give me a number. "))
for item in range(x):
  print fib(item)
