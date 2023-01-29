import openai

from flask import *

api = "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"

openai.api_key = api

app = Flask(__name__)

@app.route("/get")

def get():

	text = request.args.get("text")

	response = openai.Completion.create(

	  model="text-davinci-003",

	  prompt=f"{text}",

	  temperature=0.9,

	  max_tokens=1000,

	  top_p=1,

	  frequency_penalty=0.0,

	  presence_penalty=0.6,

	  stop=[" Human:", " AI:"]

	)

	return {"status":"done","text":response["choices"][0]["text"]}

	

if __name__ =="__main__":

	app.run(debug=True,host="0.0.0.0",port=81)

	

	
