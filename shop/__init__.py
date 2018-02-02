from flask import Flask

app = Flask(__name__)

import shop.api
import shop.index

