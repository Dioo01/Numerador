def luhn_check(num):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(num)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0



    import random

def generate_credit_card_number(iin):
    while True:
        # Generar 9 dígitos aleatorios para el número de cuenta
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
        # Combinar IIN con el número de cuenta generado
        full_number = iin + account_number
        # Calcular el dígito de verificación
        checksum = (10 - (int(full_number) % 10)) % 10
        # Formar el número completo de la tarjeta de crédito
        credit_card_number = full_number + str(checksum)
        # Validar el número generado
        if luhn_check(credit_card_number):
            return credit_card_number



            from flask import Flask, request

app = Flask(_name_)

@app.route('/generate', methods=['GET'])
def generate_card():
    iin = request.args.get('iin', '453201')  # IIN predeterminado para ejemplo
    card_number = generate_credit_card_number(iin)
    return card_number

if _name_ == '_main_':
    app.run(debug=True)