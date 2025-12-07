import tkinter as tk
from tkinter import ttk

# Tasas promedio anuales USD→ARS
TASAS = {
    2000: 1.00,
    2001: 1.00,
    2002: 3.13,
    2003: 2.95,
    2004: 2.94,
    2005: 2.92,
    2006: 3.07,
    2007: 3.11,
    2008: 3.16,
    2009: 3.73,
    2010: 3.91,
    2011: 4.12,
    2012: 4.55,
    2013: 5.47,
    2014: 8.11,
    2015: 9.26,
    2016: 14.77,
    2017: 16.56,
    2018: 28.08,
    2019: 48.19,
    2020: 70.53,
    2021: 95.08,
    2022: 130.88,
    2023: 296.43,
    2024: 916.85,
    2025: 1215.46,
}

def convertir(*args):
    texto = entrada_valor.get()
    try:
        valor_inicial = float(texto)

        año_origen = int(combo_origen.get())
        año_destino = int(combo_destino.get())

        tasa_origen = TASAS[año_origen]
        tasa_destino = TASAS[año_destino]

        # Convertir valor → USD
        usd = valor_inicial / tasa_origen

        # Convertir USD → año destino
        valor_destino = usd * tasa_destino

        resultado_usd.set(f"{usd:,.2f} USD")
        resultado_final.set(f"{valor_destino:,.2f} ARS")
    except:
        resultado_usd.set("—")
        resultado_final.set("—")

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversor ARS por año → USD → ARS")

# Variables
resultado_usd = tk.StringVar()
resultado_final = tk.StringVar()

tk.Label(ventana, text="Valor en pesos del año origen:").pack(pady=5)
entrada_valor = tk.Entry(ventana, width=20)
entrada_valor.pack()
entrada_valor.bind("<KeyRelease>", convertir)

# Menú desplegable origen
tk.Label(ventana, text="Año origen:").pack(pady=5)
combo_origen = ttk.Combobox(ventana, values=list(TASAS.keys()), width=10, state="readonly")
combo_origen.set(2014)
combo_origen.pack()
combo_origen.bind("<<ComboboxSelected>>", convertir)

# Menú desplegable destino
tk.Label(ventana, text="Año destino:").pack(pady=5)
combo_destino = ttk.Combobox(ventana, values=list(TASAS.keys()), width=10, state="readonly")
combo_destino.set(2025)
combo_destino.pack()
combo_destino.bind("<<ComboboxSelected>>", convertir)

# Resultados
tk.Label(ventana, text="Equivalente en USD:").pack(pady=5)
tk.Label(ventana, textvariable=resultado_usd, font=("Arial", 12, "bold")).pack()

tk.Label(ventana, text="Equivalente en pesos del año destino:").pack(pady=5)
tk.Label(ventana, textvariable=resultado_final, font=("Arial", 14, "bold")).pack(pady=5)

ventana.mainloop()