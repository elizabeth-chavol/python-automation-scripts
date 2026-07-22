# SOC Detector - Termux

Proyecto de Ciberseguridad desarrollado en Termux para Android.

**Descripción:** Detector de intentos de ataque por fuerza bruta que lee logs en tiempo real, extrae IPs atacantes y automatiza bloqueos en el firewall.

---

## 🛠️ Tecnologías Usadas

* **Python 3**
* **Termux** en Android
* **SMTP** Gmail
* **IPTables** (Firewall)
* Variables de entorno con **python-dotenv**

---

## 🚀 Cómo Ejecutar

1. **Instalar dependencias:**
   ```bash
   pip install python-dotenv

3. **Ejecutar el detector:**
   ```bash
   python detector_alertas.py



---

## 📈 Historial de Clases e Incrementos

* **Clase 5:** Envío de alertas por correo usando `smtplib` y variables `.env`.
* **Clase 6:** Registro local en `alertas.log` y configuración de `.gitignore`.
* **Clase 7:** Extracción de IPs con `re` y bloqueo en firewall con `iptables` y `subprocess`.

---

### 📂 Estructura del Proyecto y Archivos

| Archivo 📄 | ¿Para qué sirve? 💡 | Conceptos clave 🛠️ |
| :--- | :--- | :--- |
| `detector_alertas.py` | Guardia activo. Revisa logs, extrae IP, bloquea y avisa. | `re`, `subprocess`, `try/except`. |
| `ataques.log` | Puerta de entrada. Simulación de intentos de acceso. | Lectura de archivos (`r`). |
| `alertas.log` | Caja de evidencias. Registro de incidentes. | Escritura append (`a`). |
| `.gitignore` | Tacho con tapa. Evita subir contraseñas. | Filtros de exclusión. |
| `dashboard.py` | Panel web con Flask para ver las alertas en tiempo real. | `Flask`, `HTML/CSS`. |

## 🏷️ Historial de Versiones (Tags)

El proyecto utiliza tags de Git para documentar la evolución del dashboard web (`dashboard.py`):

* **`v1.1.0` (Versión inicial):** Estructura base del panel web con Flask y renderizado de alertas sin formato avanzado.
* **`v1.2.0` (Lógica y Métricas):** Incorporación de conteo de alertas (Críticas, Medias, Totales), recortador de texto (*slicing*) y estilos dinámicos en HTML.
* **`v1.3.0` (Versión Actual en `main`):** Integración completa del dashboard refactorizado y preparado para auto-refresco.
