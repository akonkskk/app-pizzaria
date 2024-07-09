from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'pizzaria'
}

# Funções para manipulação das tabelas
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cliente (nome, telefone) VALUES (%s, %s)", (nome, telefone))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('cadastro_cliente.html')

@app.route('/cadastro_pizza', methods=['GET', 'POST'])
def cadastro_pizza():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pizza (nome, preco) VALUES (%s, %s)", (nome, preco))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('cadastro_pizza.html')

@app.route('/fazer_pedido', methods=['GET', 'POST'])
def fazer_pedido():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        pizza_id = request.form['pizza_id']
        quantidade = request.form['quantidade']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedido (cliente_id, pizza_id, quantidade) VALUES (%s, %s, %s)", (cliente_id, pizza_id, quantidade))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    cursor.execute("SELECT * FROM pizza")
    pizzas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('fazer_pedido.html', clientes=clientes, pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)