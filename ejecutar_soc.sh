#!/data/data/com.termux/files/usr/bin/bash
cd /data/data/com.termux/files/home
python analizador_reporte.py
python enviador_reportes.py
echo "SOC ejecutado: $(date)" >> log_soc.txt
