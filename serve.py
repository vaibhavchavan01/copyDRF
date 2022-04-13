"""
To start server on prodution.
"""
import os
import sys
import waitress
from moviedatabase.wsgi import application
BASE_DIR = os.path.join(os.path.dirname(__file__), 'moviedatabase')
sys.path.append(BASE_DIR)
waitress.serve(
    application,
    host='0.0.0.0',
    port=os.getenv('PORT', '8080')
)