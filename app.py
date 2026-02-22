from flask import Flask, jsonify, request
from core import FinTrack

app = Flask(__name__)

wallet = FinTrack()
wallet.load_current_user()

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

@app.route('/api/set-budget', methods=['POST'])
def set_budget():
    data = request.get_json()
    try:
        budget = float(data['budget'])
        if budget < 0:
            raise ValueError('Budget must be positive.')
        if budget > wallet.balance:
            raise ValueError(f'Budget must be lower than balance (${wallet.balance}).')
        wallet.budget = budget
        wallet.save_to_file()
        return jsonify({'status': 'success', 'message': 'Budget updated.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/set-savings', methods=['POST'])
def set_savings():
    data = request.get_json()
    try:
        savings = float(data['savings'])
        if savings < 0:
            raise ValueError('Savings must be positive.')
        wallet.savings = savings
        wallet.save_to_file()
        return jsonify({'status': 'success', 'message': 'Savings updated.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/set-balance', methods=['POST'])
def set_balance():
    data = request.get_json()
    try:
        balance = float(data['balance'])
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        wallet.balance = balance
        wallet.save_to_file()
        return jsonify({'status': 'success', 'message': 'Balance updated.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
