import mindai

from flask import *

import random

ai = mindai.Ai()

app = Flask(__name__)

@app.route("/get")

def get():

		text = request.args.get("text")

	

	imgs = ai.image_search(text)

	

	return {"status":"done","url":random.choice(imgs["images"])}

	

if __name__ =="__main__":

	app.run(debug=True,port=81,host="0.0.0.0")
