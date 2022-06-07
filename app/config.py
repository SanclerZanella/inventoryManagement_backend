import os
if os.path.exists('env.py'):
    import env


class Config:
  '''
  Config settings and environmental variables
  '''
  SECRET_KEY = os.environ.get("SECRET_KEY")
  DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)),'inventory.db')}"
  
