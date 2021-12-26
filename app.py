from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import model.show_tools as st
from medias.demo.image_demo import load_img_demo
import plotly
import json
from model.predict import predict, load_nii
from datetime import datetime

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = 'medias/users_files/'

@app.route("/")
@app.route('/accueil/')
def view_home():
    np_no_lbl, np_lbl = load_img_demo()

    image_no_lbl = json.dumps(st.slice_img3D(np_no_lbl, "IRM en entrée"), cls=plotly.utils.PlotlyJSONEncoder)
    image_lbl = json.dumps(st.slice_img3D(np_lbl, "Segmentation attendue"), cls=plotly.utils.PlotlyJSONEncoder)

    context = {'image_no_lbl': image_no_lbl,
               'image_lbl': image_lbl}
    return render_template("index.html", context=context)

@app.route("/presentation-du-projet/")
def view_pres_proj():
    return render_template("presentation-du-projet.html")

@app.route("/a-propos/")
def view_a_propos():
    return render_template("a-propos.html")

@app.route('/prediction/', methods = ['POST', 'GET'])
def prediction():
    context = {'image_upload_no_lbl': 'empty',
               'image_predict_lbl': 'empty',
               }

    if request.method == "POST": #upload de l'user
        file_upload = request.files['file']
        filename = secure_filename(file_upload.filename)
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_upload_path = app.config['UPLOAD_FOLDER'] + current_datetime + '_' + filename
        file_upload.save(file_upload_path)

        np_upload_no_lbl = load_nii(file_upload_path)[0]
        image_upload_no_lbl = json.dumps(st.slice_img3D(np_upload_no_lbl, "IRM envoyé"), cls=plotly.utils.PlotlyJSONEncoder)
        context['image_upload_no_lbl'] = image_upload_no_lbl

        np_predict_lbl = predict(file_upload_path   )
        image_predict_lbl = json.dumps(st.slice_img3D(np_predict_lbl, "IRM segmenté"),
                                       cls=plotly.utils.PlotlyJSONEncoder)
        context['image_predict_lbl'] = image_predict_lbl

    return render_template("prediction.html", context=context)


if __name__ == '__main__':
    app.run()
