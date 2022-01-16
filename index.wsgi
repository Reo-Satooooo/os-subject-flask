import sys, os
import logging

logging.basicConfig(stream = sys.stderr)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.src.main import app as application