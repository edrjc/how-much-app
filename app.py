import numpy as np
import pandas as pd
import joblib
import pickle
import logging
from flask import Flask, render_template, flash, request, jsonify

app = Flask(__name__)

model = None
encoders = None
options = None
sample = None
faixa_etaria_labels = None

def how_much(sample):
  # Prepare new sample
  new_sample = pd.DataFrame()
  for col in encoders:
    new_sample[col] = [0]

  for col in sample.columns:
    new_col = col + '_' + str(sample.iloc[0][col])
    if new_col in new_sample:
      new_sample[[new_col]] = 1

  res_log = model.predict(new_sample)
  # From log to mensalidade
  res_mensalidade = np.expm1(res_log)
  return res_mensalidade[0]

@app.before_first_request
def startup():
	global model
	global encoders
	global options
	global sample
	global faixa_etaria_labels

	with open('./models/mlpregressor_v1.pickle', 'rb') as f:
		model = pickle.load(f)

	encoders = joblib.load('./encoders/new_dataset_dummy_first_true_encoders.bin')
	options = joblib.load('./encoders/options.bin')
	sample = joblib.load('./encoders/sample.bin')
	faixa_etaria_labels = joblib.load('./encoders/faixa_etaria_labels.bin')

@app.errorhandler(500)
def server_error(e):
	logging.exception('some error')
	return """
	And internal error <pre>{}</prep>
	""".format(e), 500

@app.route('/get_how_much', methods = ['POST', 'GET'])
def get_how_much():
	global sample

	for opt in options.keys():
		if opt == 'ano_mes':
			sample['ano'] = request.args.get(opt).split('-')[0]
			sample['mes'] = request.args.get(opt).split('-')[1]
		else:
			sample[opt] = request.args.get(opt)

	new_sample = pd.DataFrame(data=[list(sample.values())], columns=list(sample.keys()))
	how_much_res = how_much(new_sample)

	return jsonify({'how_much': str(round(how_much_res, 2))})

@app.route('/get_options', methods = ['POST', 'GET'])
def get_options():
	global options

	return jsonify(options)

@app.route('/get_select_options', methods = ['POST', 'GET'])
def get_select_options():
	global options
	global faixa_etaria_labels
	
	select = request.args.get('select')
	res = ''
	for opt in options[select]:
		if select in ["in_odonto", "in_obstetricia"]:
			res += '<option value="' + str(opt) + '">' + ('Sim' if opt == 1 else 'Não') + '</option>'
		elif select == 'cd_faixa_etaria':
			res += '<option value="' + str(opt) + '">' + faixa_etaria_labels[str(opt)] + '</option>'
		else:
			res += '<option value="' + str(opt) + '">' + str(opt) + '</option>'

	return jsonify(res)

@app.route('/', methods = ['POST', 'GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()