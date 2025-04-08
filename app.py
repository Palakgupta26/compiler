from flask import Flask, request, jsonify, render_template
from src.my_ast import Number, BinOp
from src.lexer import lex
from src.parser_1 import parse
from src.interpreter import interpret
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'request_count', 'App Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency',
    ['endpoint']
)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    # Start timer for latency
    start_time = time.time()
    
    data = request.json
    code = data.get('code', '')

    try:
        tokens = lex(code)
        ast = parse(tokens)
        result = interpret(ast)
        
        # Record successful request
        REQUEST_COUNT.labels('POST', '/compile', 200).inc()
        REQUEST_LATENCY.labels('/compile').observe(time.time() - start_time)
        
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        # Record failed request
        REQUEST_COUNT.labels('POST', '/compile', 500).inc()
        REQUEST_LATENCY.labels('/compile').observe(time.time() - start_time)
        
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)