from flask import Flask, render_template

app = Flask(__name__)

api_key = "AIzaSyCoY9iM8S5mx81-2wPzAOT7JKCeKRlfe20"
locations = {
    "JAWAHAR BHAWAN": {
        "lat": 29.86376602516524,
        "lon": 77.9009155978279
    },
    "GANGA BHAWAN": {
        "lat": 29.86120127169366,
        "lon": 77.89353457246298
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