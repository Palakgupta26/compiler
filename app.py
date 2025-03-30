from flask import Flask, request, jsonify, render_template
from src.my_ast import Number, BinOp
from src.lexer import lex
from src.parser_1 import parse
from src.interpreter import interpret 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.json
    code = data.get('code', '')

    try:
        tokens = lex(code)
        ast = parse(tokens)
        result = interpret(ast)
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)