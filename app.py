from time import time
import serial
import threading
import time
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
dados_sensor = {
    "distancia":0,
    "timestamp":"",
    "ultima_gravacao":"--/--/--",
    "ultimo_valor":"--"
}

PORTA_SERIAL = "COM11"
BAUD_RATE = 9600
INTERVALO = 5

distancia_atual = 0.0

def ler_porta_serial():
    global distancia_atual, dados_sensor
    flag = 0
    try:
        ser = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
        time.sleep(2)
        print(f"Conectado na porta: ${PORTA_SERIAL}")

        while True:
            if ser.in_waiting >0:
                linha = ser.readline().decode('utf-8').strip()
                if "Distancia: Analógica -" in linha:
                    try:
                        valor_str = linha.split("-")[1].strip()
                        distancia_atual = float(valor_str)
                        dados_sensor["distancia"] = distancia_atual
                        dados_sensor["timestamp"] = time.time()
                        agora = time.time()
                    except ValueError:
                        pass
    except Exceptionas as e:
        print(f"Erro: ${e}")