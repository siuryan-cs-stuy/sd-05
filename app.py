from flask import Flask, render_template
from utils import occupations
from utils.occupations import generate_occupations, random_occupation

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Index')

@app.route('/occupations')
def occupations():
    occ_dict = generate_occupations()
    random_occ = random_occupation(occ_dict)
    occ_link = occ_dict[random_occ][1]
    return render_template('occupations.html', title = 'Occupations', occ_dict = occ_dict, random_occ = random_occ, occ_link = occ_link)

if __name__ == '__main__':
    app.debug = True
    app.run()
