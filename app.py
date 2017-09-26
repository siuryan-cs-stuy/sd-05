from flask import Flask, render_template
import random

app = Flask(__name__)
FILENAME = 'occupations.csv'

@app.route('/')
def index():
    return 'hi'
#return render_template('base.html')

def generate_occupations():
    occ_dict = {}

    f = open(FILENAME, 'r')

    for line in f:
        line = line.strip()
        if line[0] == '"':
            line = line.strip('"').split('"')
            line[1] = line[1].strip(',')
        if not line[1].isalpha():
            occ_dict[line[0]] = float(line[1])
        else:
            line = line.split(',')
            if not line[1].isalpha():
                occ_dict[line[0]] = float(line[1])
                    
    f.close()
    return occ_dict

def random_occupation(occ_dict):
    count = 0
    random_num = random.random()*100
    for key in occ_dict:
        count += occ_dict[key]
        if random_num < count:
            return key
    
@app.route('/occupations')
def occupations():
    occ_dict = generate_occupations()
    random_occ = random_occupation(occ_dict)
    return render_template('occupations.html', occ_dict = occ_dict, random_occ = random_occ)

if __name__ == '__main__':
    app.debug = True
    app.run()
