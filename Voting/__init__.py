"""
The flask application package.
"""

from flask import Flask
import logging

app = Flask(__name__)

app.config.from_object('config_cosmos')
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import Voting.views