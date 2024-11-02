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
    "LBS": {
        "lat": 29.867996419259715, 
        "lon": 77.89555270184519
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
    "CAUTLEY BHAWAN": {
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
    "JAMES THOMSON": "https://live.staticflickr.com/502/19897756159_eb85bd3a12_h.jpg",
    "LIBRARY": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROapuQcfblPWlqQg_DsGJEp-STXX-EQh0bHg&s",
    "MAC": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_c6vnq3Kx9S3ShC-oiVuyeSZguGBAMvmmqg&s",
    "CHURCH": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREov9tvU7N54fa9iROGkqninG8nbadsWLezg&s",
    "HOSPITAL": "https://iitr.ac.in/Institute/assets/81aacf180df34c201f6a2e365d48ff3e2881985e51514703f1938e2901318a52_1.jpg",
    "RJB": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFoLCmvrLKyS6dlPGS0hCFDJgPr-WI61KFyg&s",
    "LBS": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSInsvUbWP5O9-a2Zq86xEMxr2wwrzx_zujEQ&s",
    "RAJIV": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7HtGGstvJhgN3dZN4tTOJQv-JMGrByEB4RQ&s",
    "SARASWATI MANDIR": "https://iitr.ac.in/Campus%20Life/Facilities/assets/dbae772db29058a88f9bd830e957c695347c41b6162a7eb9a9ea13def34be56b_temple.jpeg",
    "CONVOCATION": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_AGi_ShWhH3cWOJIF9J_IlD5xLBB4V0XyHA&s",
    "GATE NO 5": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_r5xUpklIZf5CG-0cDzpjwRzp8rg6ay3lFg&s",
    "KASTURBA": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHL9YCYa6BJ9x2orGf2AlPdK4Ue4j_HpTerg&s",
    "GATE NO 2": "https://images.shiksha.com/mediadata/images/1570610774php52UF0f.png",
    "RADHAKRISHNA BHAWAN": "https://content.jdmagicbox.com/comp/roorkee/d5/9999p1332.1332.180810133417.v7d5/catalogue/radhakrishnan-bhawan-civil-lines-roorkee-hostel-for-boy-students-zj33vi3ecl.jpg",
    "RAILWAY TICKET COUNTER": "https://scriet.ccsuniversity.ac.in/assets/images/railway01.jpg",
    "ABN GROUND": "https://i.ytimg.com/vi/8bA3Swg1dzM/maxresdefault.jpg",
    "RAVINDRA BHAWAN": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_wkLoid3Hhm6PcP88EszeLIXJKOndpYEwbQ&s",
    "CAUTLEY BHAWAN": "https://images.picxy.com/cache/2019/7/8/f8c74e6cf63aab86c2c0b8d4f45e7a8e.jpg",
    "SAROJINI BHAWAN": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoyJc_nJ8ow90xttuWy_TGUPrIRrJjMhx1bw&s",
    "GOVIND BHAWAN": "https://content.jdmagicbox.com/comp/roorkee/g5/9999p1332.1332.180810112231.w2g5/catalogue/govind-bhawan-civil-lines-roorkee-hostel-for-boy-students-gcn44q02j0.jpg",
    "TINKERING": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRw9semA400bNx9ZMzQa66tMLihAGWGRz6fg&s",
    "APJ": "https://images.picxy.com/cache/2019/7/8/061592d9ecb66f51b38d2515de1b5bbe.jpg",
    "GARGI BLOCK": "https://images.picxy.com/cache/2019/7/8/fe882d04dec3ceca830f418154a0d689.jpg",
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
