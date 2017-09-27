from flask import Flask, render_template
import random

app = Flask(__name__)
FILENAME = 'occupations.csv'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Index')

def generate_occupations():
    occ_dict = {}

    f = open(FILENAME, 'r')

    for line in f:
        line = line.strip()
        if line[0] == '"':
            line = line.strip('"').split('"')
            rest_of_line = line[1].strip(',').split(',')
            occ_dict[line[0]] = (float(rest_of_line[0]), rest_of_line[1])
        else:
            line = line.split(',')
            if not line[1].isalpha():
                occ_dict[line[0]] = (float(line[1]), line[2])
                
    f.close()
    return occ_dict

def random_occupation(occ_dict):
    count = 0
    random_num = random.random()*100
    for key in occ_dict:
        count += occ_dict[key][0]
        if random_num < count:
            return key
    
@app.route('/occupations')
def occupations():
    occ_dict = generate_occupations()
    random_occ = random_occupation(occ_dict)
    occ_link = occ_dict[random_occ][1]
    return render_template('occupations.html', title = 'Occupations', occ_dict = occ_dict, random_occ = random_occ, occ_link = occ_link)

if __name__ == '__main__':
    app.debug = True
    app.run()
