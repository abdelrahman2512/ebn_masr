import flask ,requests
from flask import * 

app = Flask(__name__)

@app.route("/imge")
def img():
	text = request.args.get("text")
	if not text:
		return {"status":"error"}
	url = f"https://api.dlyar-dev.tk/open-ai-img.json?key=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&text={text}"
	r = requests.get(url).json()
	i = r["data"][0]["url"]
	return {"status":"done",
	"url":i}
	
if __name__ =="__main__":
	app.run(debug=True,host="0.0.0.0",port=81)