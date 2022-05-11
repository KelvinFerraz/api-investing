from flask import Flask, request, render_template
import investpy

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/dividendos' , methods = ['POST'])
def dividendos():
    request_data = request.get_json()
    stock = request_data['stock']
    country = request_data['country']
    from_date = request_data['from_date']
    to_date = request_data['to_date']

    result = investpy.get_stock_historical_data(stock=stock, country=country, from_date=from_date, to_date=to_date, as_json=True)
    return result


app.run(host='localhost', port=5000)