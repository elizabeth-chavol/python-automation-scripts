SOC Detector - Termux

Proyecto de Ciberseguridad desarrollado en Termux para Android.

Descripción
Detector de intentos de ataque por fuerza bruta que lee logs en tiempo real y envía alertas por correo electrónico cuando detecta más de 3 intentos fallidos desde la misma IP.

Tecnologías Usadas
- Python 3
- Termux en Android
- SMTP Gmail
- Variables de entorno con python-dotenv

Cómo Ejecutar

1. Instalar dependencia:
pip install python-dotenv

2. Configurar credenciales:
Copiar .env.example a .env y poner tu correo y contraseña de aplicación de Gmail.

3. Ejecutar:
python detector_alertas.py
o con el script:
bash ejecutar_soc.sh

Clase 5: Mejora
Se agregó envío de alertas por correo usando smtplib y variables de entorno seguras.

Autor
Proyecto del curso de SOC Analyst - Nivel 3

