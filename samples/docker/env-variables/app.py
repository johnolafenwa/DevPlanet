import os 

if "USERNAME" in os.environ:
  username = os.environ["USERNAME"]
  print("Username: ",username)