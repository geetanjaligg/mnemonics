import urllib2
import flask
from flask import Flask
from flask import render_template
from settings import APP_STATIC
from flask import request
from BeautifulSoup import BeautifulSoup


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index(name=None):
	mnemonic = ''
	if request.method == 'GET':
		if(request.args.get('word')):
			print request.args.get('word')
			url = 'http://mnemonicdictionary.com/?word=' + request.args.get('word')
			res = urllib2.urlopen(url)
			soup = BeautifulSoup(res)

			mnemonic = soup.findAll('div',{'class':'span6'})[0]

	return render_template('search.html',mnemonic = mnemonic)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')