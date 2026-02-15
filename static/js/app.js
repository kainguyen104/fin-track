
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/account-summary')
        .then(res => res.json())
        .then(data => {
            document.getElementById('account-info').textContent = `Balance: $${data.balance}`;
        })
        .catch(() => {
            document.getElementById('account-info').textContent = 'Unable to load account info.';
        });

    fetch('/api/transactions')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('transaction-list');
            list.innerHTML = '';
            data.slice(0, 5).forEach(tx => {
                const li = document.createElement('li');
                li.textContent = `${tx.date}: $${tx.amount} (${tx.type})`;
                list.appendChild(li);
            });
        })
        .catch(() => {
            document.getElementById('transaction-list').innerHTML = '<li>Unable to load transactions.</li>';
        });
});
