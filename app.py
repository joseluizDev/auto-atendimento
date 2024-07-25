from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/webhook')
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        # Aqui você pode processar os dados recebidos
        print(data)
        return jsonify({'status': 'sucesso'}), 200
    else:
        return jsonify({'status': 'método não permitido'}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
