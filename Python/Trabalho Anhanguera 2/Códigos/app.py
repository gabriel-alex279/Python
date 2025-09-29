from flask import Flask, render_template, request

app = Flask(__name__)  # Corrigido: use __name__ entre underscores

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])

        # Validações de entrada
        if salario < 0:
            return "Erro: Salário não pode ser negativo."
        if dependentes < 0:
            return "Erro: Número de dependentes não pode ser negativo."

        # Cálculo do INSS (8%)
        desconto_inss = salario * 0.08

        # Cálculo do IR (15% se salário > 2500)
        desconto_ir = 0
        if salario > 2500:
            desconto_ir = salario * 0.15

        # Desconto por dependentes
        desconto_dependentes = dependentes * 200

        # Salário líquido
        resultado = salario - desconto_inss - desconto_ir + desconto_dependentes

        return f"Salário líquido: R$ {resultado:.2f}"

    except ValueError:
        return "Erro: Insira valores válidos para salário e dependentes."

if __name__ == '__main__':
    app.run(debug=True)
