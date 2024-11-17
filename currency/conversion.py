#! env python3


pairs = {
        'usd-eur': {'bid': 0.74, 'ask': 0.76},
        'usd-jpy': {'bid': 120, 'ask': 124},
        'usd-gbp': {'bid': 0.64, 'ask': 0.66},
        'eur-jpy': {'bid': 140, 'ask': 144},
        'eur-gbp': {'bid': 0.86, 'ask': 0.88},
        'jpy-gbp': {'bid': 0.006, 'ask': 0.008},
        'gbp-jpy': {'bid': 150, 'ask': 154}
        }

def _convert(amount, currency, target, visited=[]):
    if currency == target:
        print("Sequence: ", visited, f" amount: {amount:.2f} {currency}")
        return

    for cp, rates in pairs.items():
        base, quote = cp.split('-')
        if quote not in visited and base == currency:
            _convert(amount * rates['ask'], quote, target, visited + [quote])

        if base not in visited and quote == currency:
            _convert(amount / rates['bid'], base, target, visited + [base])

def convert(amount, currency, target):
    _convert(amount, currency, target, [currency])

if __name__ == '__main__':
    print("Converting 100 USD to JPY")
    convert(100, 'usd', 'jpy')

    print("Converting 100 USD to EUR")
    convert(100, 'usd', 'eur')
