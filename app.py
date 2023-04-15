from flask import Flask, render_template, request
from suggest import suggest

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def main():
    if request.method=='POST':
        songname=request.form.get('songname')
        name,artists,images=suggest.find(songname)
        return render_template('recommend.html',name=name,artists=artists,images=images)
    name,artists,images=suggest.trending()
    return render_template('index.html',name=name,artists=artists,images=images)

app.run(debug=True)