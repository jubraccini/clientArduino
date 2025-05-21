import serial
import socket
import time

# Configurações da porta serial (ajuste conforme necessário)
porta_serial = '/dev/ttyACM0'  # ou /dev/ttyACM0
baud_rate = 9600

# Configurações do servidor (Raspberry Pi 2)
HOST = '10.25.1.101'  # Substitua pelo IP da Raspberry Pi 2
PORT = 12345

# Inicializa a comunicação serial com o Arduino
arduino = serial.Serial(porta_serial, baud_rate, timeout=1)
time.sleep(2)  # Aguarda a inicialização da porta serial