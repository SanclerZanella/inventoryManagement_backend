import os
if os.path.exists('env.py'):
    import env


class Config:
  '''
  Config settings and environmental variables
  '''
  SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
  DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)),'inventory.db')}"
  
