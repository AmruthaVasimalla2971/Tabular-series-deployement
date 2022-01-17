from flask import Flask ,render_template , request
import model
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        feature0 = request.form['feature0']
        feature1 = request.form['feature1']
        feature2 = request.form['feature2']
        feature3 = request.form['feature3']
        feature4 = request.form['feature4']
        feature5 = request.form['feature5']
        feature6 = request.form['feature6']
        feature7 = request.form['feature7']
        feature8 = request.form['feature8']
        feature9 = request.form['feature9']
        feature10 = request.form['feature10']
        feature11 = request.form['feature11']
        feature12 = request.form['feature12']
        feature13 = request.form['feature13']
        feature14 = request.form['feature14']
        feature15 = request.form['feature15']
        feature16 = request.form['feature16']
        feature17 = request.form['feature17']
        feature18 = request.form['feature18']
        feature19 = request.form['feature19']
        feature20 = request.form['feature20']
        feature21 = request.form['feature21']
        feature22 = request.form['feature22']
        feature23 = request.form['feature23']
        feature24 = request.form['feature24']
        feature25 = request.form['feature25']
        feature26 = request.form['feature26']
        feature27 = request.form['feature27']
        feature28 = request.form['feature28']
        feature29 = request.form['feature29']
        feature30 = request.form['feature30']
        feature31 = request.form['feature31']
        feature32 = request.form['feature32']
        feature33 = request.form['feature33']
        feature34 = request.form['feature34']
        feature35 = request.form['feature35']
        feature36 = request.form['feature36']
        feature37 = request.form['feature37']
        feature38 = request.form['feature38']
        feature39 = request.form['feature39']
        feature40 = request.form['feature40']
        feature41 = request.form['feature41']
        feature42 = request.form['feature42']
        feature43 = request.form['feature43']
        feature44 = request.form['feature44']
        feature45 = request.form['feature45']
        feature46 = request.form['feature46']
        feature47 = request.form['feature47']
        feature48 = request.form['feature48']
        feature49 = request.form['feature49']
        features = np.array([[feature0,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,
                                feature11,feature12,feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,
                                feature21,feature22,feature23,feature24,feature25,feature26,feature27,feature28,feature29,feature30,
                                feature31,feature32,feature33,feature34,feature35,feature36,feature37,feature38,feature39,feature40,
                                feature41,feature42,feature43,feature44,feature45,feature46,feature47,feature48,feature49]])
        features.reshape(1,-1)
        classP = model.predict_class(features)

    return render_template('submit.html',n=classP)


if __name__ == "__main__":
    app.run(debug=True)