'''
Created on 25/04/2013

@author: cristian
'''

from app import app
@app.route('/proyecto')
def proyecto():
    return 'Hello World!'