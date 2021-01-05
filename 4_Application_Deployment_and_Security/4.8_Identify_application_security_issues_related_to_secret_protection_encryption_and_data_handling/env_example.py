import os
from dotenv import load_dotenv
load_dotenv()

# user = os.environ.get('CISCOUSERNAME')
# print(user)

newuser = os.environ.get('CISCOUSER')
print(newuser)