from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('alertas.log', 'r') as f:
        alertas = f.readlines()
        alertas = alertas[::-1]

    criticas = 0
    medias = 0
    total = 0

    alertas_html = ""
    for alerta in alertas:
        if 'CRITICA' in alerta:
            color = '#ff0000'
            criticas += 1
        elif 'MEDIA' in alerta:
            color = '#ffcc00'
            medias += 1
        else:
            color = 'white'

        total += 1

        fecha = alerta[1:17].strip()
        texto = alerta[19:].strip()
        alertas_html += f'<div class="alerta" style="border-left: 5px solid {color}>'
        alertas_html += f'<div class="fecha">{fecha}</div>'
        alertas_html += f'<div>{texto}</div></div>'

    html = f"""
    <html><head><style>
    body {{background: #1a1a1a; color: white; font-family: Arial; padding: 5px; margin :0;}}
    .alerta {{padding: 10px; margin: 10px 0; background: #2a2a2a; word-wrap: break-word; overflow-wrap: break-word;}}
    .fecha {{color: #888; font-size:12px;}}
    h1, h2 {{font-size: 16px; margin: 5px 0;}}
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="10">
    </head><body>
    <h1>DASHBOARD SOC</h1>
        <a href="/borrar" style="color:red; border:1px solid red; padding:5px; text-decoration:none;">BORRAR TODAS LAS ALERTAS</a>
        <h2 style="color:#ff0000">CRITICAS: {criticas}</h2>
        <h2 style="color:#ffcc00">MEDIA: {medias}</h2>
        <h2 style="color:white">TOTAL: {total}</h2>
        <h2>ULTIMAS ALERTAS:</h2> 
   """

    html += alertas_html
    html += "</body></html>"
    return render_template_string(html)

@app.route('/borrar')
def borrar():
    open('alertas.log', 'w').close()
    return "Alertas borradas. <a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
