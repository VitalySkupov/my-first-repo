

def get_vat(payment, precent=18):
    try:
        payment = float(payment)
        precent = int(precent)
        vat = payment/ (100 + precent) * precent
        vat = round(vat, 2)
        return 'НДС: {}' .format(vat)
    except (TypeError, ValueError):
        return 'Не могу посчитать, проверьте вводимые данные!'

result = get_vat(76, 10)
print(result)
