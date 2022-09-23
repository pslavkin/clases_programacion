#from flask import Flask,render_template
#
#app = Flask(__name__)
#
#
#@app.route('/')
#def home():
#    return render_template('home.html')
#
#@app.route('/about/')
#def about():
#    return render_template('about.html')   
#
#if __name__ == "__main__":
#    app.run(debug=True)
#
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	print(request.method)
	if request.method == 'POST':
		if request.form.get('Encrypt') == 'Encrypt':
			# pass
			print("Encrypted")
		elif  request.form.get('Decrypt') == 'Decrypt':
			# pass # do something else
			print("Decrypted")
		else:
			# pass # unknown
			return render_template("about.html")
	elif request.method == 'GET':
		# return render_template("index.html")
		print("No Post Back Call")
	return render_template("home.html")


if __name__ == '__main__':
	app.run()
