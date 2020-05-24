from flask import Flask, request
import pickle
from function_process_sentence import *

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home_page():
	if request.method == 'POST':
		loaded_model = pickle.load(open('/code/trained_model.sav', 'rb'))
		count_vect = pickle.load(open('/code/vectorizer_file.sav', 'rb'))
		text_input  = request.form.get('please input your text')
		predicted_category = loaded_model.predict(count_vect.transform([process_sentences(text_input)]))
		return """
		<center>
		<br><br>
		<h2>Your text input:</h2> <br>{}<br><br>
		<h3>predicted category:</h3> <h2>{}</h2>
		</center>
		""".format(text_input,predicted_category[0])
	return """
	<center>
	<H1>Get the category of the youtube video using it's decription</H1><br><br>
	<form method="POST">
	<H3> Copy and paste from a youtube video description for better accuracy</H3><br> 
	<H3> Please input your text below:</H3><br><br>
	<H3> <input type ="text" name='please input your text'</H3><br>
	<input type="submit" value="Submit">
	</H3>
	</form>
	</center>


	"""

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port =5000)
