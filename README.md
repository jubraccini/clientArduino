# Sistema de Cuidados para Pacientes com Fotossensibilidade

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Sobre o Projeto

O clientArduino é um sistema simples que monitora o nível de luminosidade ambiente utilizando um sensor conectado a um Arduino. O sistema envia os dados para uma Raspberry Pi, que processa as informações e exibe um alerta caso a luz esteja forte demais (ALERTA) ou uma indicação de que a luz está fraca e segura (OK).

**Ideia principal:** ajudar no cuidado de pacientes com fotossensibilidade, alertando para condições que possam causar desconforto ou danos.

Atividade da disciplina "Hardware Architecture" do Curso de Ciência da Computação - Atitus Educação.

## 🧩 Funcionalidades

- Leitura serial do sensor de luminosidade no Arduino.
- Envio dos dados via socket para a Raspberry Pi.
- Processamento simples para determinar status da luz.
- Impressão de alertas no console.

---

# Como executar a aplicação localmente

### Pré Requisitos 📌

- ``Python``
- ``pyserial`` - comunicação com Arduino
- ``Sockets TCP`` - comunicação entre dispositivos
- ``Arduino`` - sensor de luminosidade

### Instalação ⬇️

1. Clone o repositório:
```bash
   git clone https://github.com/jubraccini/clientArduino.git
```

2. Instale as dependências Python:
```bash
   pip install pyserial
```

### Configuração e Uso ⚙️

1. Ajuste o arquivo ``leitor_luminosidade.py`` com o IP do Raspberry Pi (variável ``HOST``) e a porta TCP (``PORT``).
2. Verifique a porta serial do Arduino (``porta_serial``) e a ``baud_rate``.
3. Conecte o Arduino e o Raspberry Pi na mesma rede.
4. Execute o script no Raspberry Pi:
```bash
    python leitor_luminosidade.py
```
 
5. Observe os alertas no console:
    - **ALERTA** para luz forte
    - **OK** para luz fraca

---

## Exemplos de Saída
```bash
[RPi1] Enviando: ALERTA  
[RPi1] Enviando: OK
```

## 👩‍💻 Contribuidores
- Elisiane M. Brand

## ✨ Agradecimentos

Agradecimentos especiais para quem ajudou no projeto:

- Maria Eduarda C. Dornelles  
- Carolline Piccoli

## 👾 Autores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/117121095?v=4" width=115><br><sub>Julia Braccini</sub>](https://github.com/jubraccini) |
| :---: |
