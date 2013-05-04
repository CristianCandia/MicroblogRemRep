import sys
import os
os.environ['FLASK_ENV']= 'PRODUCTION'
sys.path.insert(0, '/home/cristian/git/microblogRepo/microblog') 

from app import app as application
