def success():
  print("login successful")

def wrong_user():
  print("username is wrong, cant login")

def wrong_password():
  print("password is wrong")

def login(username,password):
  if username == "admin":
    if password == "root@1234":
      success()
    else:
      wrong_password()
  else:
    wrong_user()

login("admin","root@12345")
