# age validation

def valid():
  print("you are 18+, you are allowed")

def not_valid():
  print("You are not mature enough, you are not allowed")

def check(age):
  if age>=18:
    valid()
  else:
    not_valid()

check(25)
