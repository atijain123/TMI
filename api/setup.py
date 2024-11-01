from flask import Flask, render_template

app = Flask(__name__)

api_key = "AIzaSyCF8z7l1vQC9bbM1ZMRjwr8Cq8rMZKMjw0"
locations = {
    "JAMES THOMSON": {
        "lat": 29.86586949616119,
        "lon": 77.89659660917312
    },
    "LIBRARY": {
        "lat": 29.86540770142045, 
        "lon": 77.89501437155589
    },
    "MAC": {
        "lat": 29.87024498842006, 
        "lon": 77.89623035625037
    },
    "APJ": {
        "lat": 29.864949906347558, 
        "lon": 77.89380230528977
    },
    "GARGI BLOCK": {
        "lat": 29.864600609573657, 
        "lon": 77.8935836372435
    },
    "SAC": {
        "lat": 29.866655991651918,
        "lon": 77.89943869347913
    },
    "CHURCH": {
        "lat": 29.86684837185326, 
        "lon": 77.89131591082639
    },
    "HOSPITAL": {
        "lat": 29.862691899502444,
        "lon": 77.8930253832679
    },
    "RJB": {
        "lat": 29.87039762125359, 
        "lon": 77.8946230469015
    },
    "LBS CIRCLE": {
        "lat": 29.867972658949906, 
        "lon": 77.89383279123994
    },
    "RAJIV": {
        "lat": 29.869808829264905, 
        "lon": 77.89548375060804
    },
    "SARASWATI MANDIR": {
        "lat": 29.86846677231719, 
        "lon": 77.89796550341045
    },
    "CONVOCATION": {
        "lat": 29.868219538378018, 
        "lon": 77.89098029530747
    },
    "GATE NO 5": {
        "lat": 29.8691186971069, 
        "lon": 77.89967080849712
    },
    "KASTURBA": {
        "lat": 29.867519382413825,
        "lon": 77.90180042547826
    },
    "GATE NO 3": {
        "lat": 29.86949126288729, 
        "lon": 77.89529559699169
    },
    "GATE NO 2": {
        "lat": 28.463963909643482, 
        "lon": 77.49274756288443
    },
    "RADHAKRISHNA BHAWAN": {
        "lat": 29.871393379270394, 
        "lon": 77.89589946595285
    },
    "GANGA BHAWAN": {
        "lat": 29.871367538680406,
        "lon": 77.89501823181622
    },
    "RAILWAY TICKET COUNTER": {
        "lat": 29.86120127169366,
        "lon": 77.89353457246298
    },
    "JAWAHAR BHAWAN": {
        "lat": 29.86376602516524, 
        "lon": 77.9009155978279
    },
    "ABN GROUND": {
        "lat": 29.86964547716228,
        "lon": 77.89633761234211
    },
    "RAVINDRA BHAWAN": {
        "lat": 29.864569674912456, 
        "lon": 77.89358748146739
    },
    "CAUTELEY BHAWAN": {
        "lat": 29.870706786648313, 
        "lon": 77.89669648361803
    },
    "SAROJINI BHAWAN": {
        "lat": 29.865013419701977, 
        "lon": 77.90080922177167
    },
    "GOVIND BHAWAN": {
        "lat": 29.862229744199627,
        "lon": 77.89505107759065
    },
    "TINKERING": {
    "lat": 29.863769754464432,
    "lon": 77.89652038065138
    },
}
images = {
    "JAWAHAR BHAWAN": "https://www.iitr.ac.in/jawaharbhawan/Images/card/hero.JPG",
    "GANGA BHAWAN": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlxKJR6jiNjfFnEQ35wztCGLIP8s1WCCKL_w&s",
}

names = locations.keys()
@app.route('/')
def home():
    return render_template('index.html', names=list(names))

@app.route('/initial/<name>')
def initial(name):
    name = name.replace("%20", " ")
    name = name.upper()
    if name not in list(names):
        return render_template('error.html', name=name)
    curr = list(names)
    curr.remove(name)
    return render_template('initial.html', names=curr, name=name, start_image=images[name])

@app.route('/final/<start>/<end>')
def final(start, end):
    start = start.replace("%20", " ")
    end = end.replace("%20", " ")
    start = start.upper()
    end = end.upper()
    if start not in list(names) or end not in list(names):
        return render_template('error.html', name=start + " or " + end)
    return render_template('final.html', api_key=api_key, start=start, end=end, start_lat=locations[start]["lat"], start_lon=locations[start]["lon"], end_lat=locations[end]["lat"], end_lon=locations[end]["lon"], image_start=images[start], image_end=images[end])

if __name__ == '__main__':
    app.run()
