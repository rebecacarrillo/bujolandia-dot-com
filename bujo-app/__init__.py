from flask import Flask, Blueprint, render_template, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True



Bootstrap(app)






@app.route('/')
def index():
    return render_template('index.html')