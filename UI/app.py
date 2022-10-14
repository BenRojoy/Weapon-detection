import subprocess
import os
from flask import Flask,render_template,jsonify,request,url_for,flash,redirect,send_from_directory
import webbrowser
import json

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'mp4','avi','mkv'}

app = Flask(__name__)  
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


data={}

@app.route('/detect', methods=['GET', 'POST'])
def run_detect():
       proc= subprocess.Popen('python ../yolov5/detect.py --weights ../best2.pt --img 416 --conf 0.5 --source ../UI/static/input.mp4')
       proc.wait()
       proc.terminate
       proc= subprocess.Popen('python extract.py wielded')
       proc.wait()
       proc.terminate
       proc= subprocess.Popen('python extract.py unwielded')
       proc.wait()
       proc.terminate
       return jsonify(dict(redirect='output'))

@app.route('/output')   
def output():
    global data
    f = open('static/output/results.json')
    data = json.load(f)
    f.close()
    file_list1=os.listdir('static/snapshots/high_severity')
    for i in range(len(file_list1)):
        file_list1[i]="snapshots/high_severity/"+file_list1[i]
    file_list2=os.listdir('static/snapshots/medium_severity')
    for i in range(len(file_list2)):
        file_list2[i]="snapshots/medium_severity/"+file_list2[i]
    return render_template('output.html',details=data,filenames1=file_list1,filenames2=file_list2) 

@app.route('/severity')   
def severity():
   global data
   severity = 0
   high_severity=["Wielded small guns","Wielded big guns"]
   medium_severity=["Small guns","Big guns"]
   for i in high_severity:
       if(data[i]>0):
           severity=2
           break
   if(severity==0):
       for i in medium_severity:
           if(data[i]>0):
               severity=1
               break
   return str(severity)
    
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], "input.mp4")):
      os.remove(os.path.join(app.config['UPLOAD_FOLDER'], "input.mp4"))
   if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "input.mp4"))
            return redirect(url_for('download_file', name="input.mp4"))
            
@app.route('/')
def home():
   if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], "input.mp4")):
       os.remove(os.path.join(app.config['UPLOAD_FOLDER'], "input.mp4"))
   return render_template('home.html')

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(port=5000)