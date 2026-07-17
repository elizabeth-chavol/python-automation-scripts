from flask import Flask, render_template_string
import os

app = Flask(__name__)
LOG_FILE = "alertas.log"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SOC Dashboard v1</title>
    <meta http-equiv="refresh" content="5">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0a0a0a; color: #00ff00; font-family: monospace; padding: 10px; margin: 10px 0; }
        h1 { color: #ff0000; text-align: center; }
        .alerta { background: #1a1a1a; border-left: 4px solid red; padding: 10px; margin: 10px 0; }
        .fecha { color: #888; font-size: 12px; }
    </style>
</head>
<body>
    <h1>:rotating_light: SOC DASHBOARD - ELIZABETH :rotating_light:</h1>
    {% if alertas %}
        {% for alerta in alertas %}
        <div class="alerta">
            <div class="fecha">{{ alerta.split(' - ')[0] }}</div>
            <div>{{ alerta.split(' - ')[1] }}</div>
        </div>
        {% endfor %}
    {% else %}
        <p>No hay alertas. Todo tranquilo &#9989;</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def dashboard():
    alertas = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            alertas = f.readlines()
    return render_template_string(HTML, alertas=alertas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


