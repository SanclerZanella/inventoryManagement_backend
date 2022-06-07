import os
if os.path.exists('env.py'):
    import env


class Config:
  '''
  Config settings and environmental variables
  '''
  MAP_KEY = os.environ.get("MAP_KEY")
  DATABASE_URI = os.environ.get("DATABASE_URI")
