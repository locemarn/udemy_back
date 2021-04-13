from flask import Flask, request, json
from joblib import load
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
arr = load('vocabulario_slug_title.joblib')
model = load('model.joblib')


@app.route('/')
def index():
	return { "status": 200, "result": "result" }

@app.route('/api', methods=['POST'])
def api():

	body = request.get_json()

	if not body['course']:
		return { "status": 400, "errorMsg": "Ocorreu um erro na requisição do curso." }

	result = controller(body['course'])

	print('result --->', result)

	return { "status": 200, "result": result[0] }


def controller(amostra):
	# amostra = 'The Complete Investment Banking'
	ams = []
	for row in arr:
		if row in amostra.lower().split(' '):
			ams.append(1)
		else:
			ams.append(0)

	return model.predict([ams])




if __name__ == '__main__':
	app.run()
