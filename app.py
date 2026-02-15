from flask import Flask, jsonify, render_template
from core import FinTrack
from flask import request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/account-summary')
def account_summary():
    return jsonify({
        'balance': wallet.balance,
        'budget': wallet.budget,
        'savings': wallet.savings
    })

@app.route('/api/transactions')
def transactions():
    txs = [t.to_json() for t in wallet.transactions]
    return jsonify(txs)

@app.route('/api/add-transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    try:
        wallet.add_transaction(
            data['amount'],
            data['name'],
            data['category'],
            data.get('description', ''),
            data['type']
        )
        wallet.save_to_file()
        return jsonify({'message': 'Transaction added successfully.'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/api/analysis')
def analysis():
    # Recompute analysis
    wallet.view_expenses_analysis()
    wallet.view_income_analysis()
    return jsonify({
        'expenses': wallet.expenses_by_category,
        'income': wallet.income_by_category
    })

if __name__ == '__main__':
    app.run(debug=True)
