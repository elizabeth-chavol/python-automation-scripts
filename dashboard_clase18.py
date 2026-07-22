from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('alertas.log', 'r') as f:
        alertas = f.readlines()

    criticas = 0
    medias = 0
    total = 0

    for linea in alertas:
        total += 1
        if "CRITICA" in linea:
            criticas += 1
        elif "MEDIA" in linea:
            medias += 1

    html = f'''
    <html><head><style>
    body {{background: #1a1a1a; color: white; font-family: Arial;}}
    .alerta {{padding: 10px; margin: 10px; background: #2a2a2a;}}
    .fecha {{color: #888; font-size:12px;}}
    </style>
    <meta http-equiv="refresh" content="5">
    </head>
    <body>
    <h1>DASHBOARD SOC</h1>
            <h2 style="color:#ff0000">CRITICAS: {criticas}</h2>
            <h2 style="color:#ffcc00">MEDIA: {medias}</h2>
            <h2 style="color:white">TOTAL: {total}</h2>
    '''

    for alerta in alertas:
        if 'CRITICA' in alerta:
            color = '#ff0000'
            criticas = criticas + 1
        else:
            color = '#ffcc00'
            medias = medias + 1

        total = total + 1

        fecha = alerta[1:20]
        texto = alerta[22:]
        html += f'<div class="alerta" style="border-left: 5px solid {color}">'
        html += f'<div class="fecha">{fecha}</div>'
        html += f'<div>{texto}</div></div>'

    html += '</body></html>'
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
