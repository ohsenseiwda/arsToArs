import customtkinter as ctk
from tkinter import StringVar


# ---------------------------------------------------------
# Tasas promedio anuales USD→ARS
# ---------------------------------------------------------
TASAS = {
    2000: 1.00, 2001: 1.00, 2002: 3.13, 2003: 2.95, 2004: 2.94,
    2005: 2.92, 2006: 3.07, 2007: 3.11, 2008: 3.16, 2009: 3.73,
    2010: 3.91, 2011: 4.12, 2012: 4.55, 2013: 5.47, 2014: 8.11,
    2015: 9.26, 2016: 14.77, 2017: 16.56, 2018: 28.08, 2019: 48.19,
    2020: 70.53, 2021: 95.08, 2022: 130.88, 2023: 296.43,
    2024: 916.85, 2025: 1215.46,
}

# ---------------------------------------------------------
# Función de conversión (igual que tu original)
# ---------------------------------------------------------
def convertir(*args):
    texto = entrada_valor.get()

    try:
        valor_inicial = float(texto)
        año_origen = int(combo_origen.get())
        año_destino = int(combo_destino.get())

        tasa_origen = TASAS[año_origen]
        tasa_destino = TASAS[año_destino]

        usd = valor_inicial / tasa_origen
        valor_destino = usd * tasa_destino

        resultado_usd.set(f"{usd:,.2f} USD")
        resultado_final.set(f"{valor_destino:,.2f} ARS")

    except:
        resultado_usd.set("—")
        resultado_final.set("—")

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA APP CTK
# ---------------------------------------------------------
ctk.set_appearance_mode("dark")      # "light" | "dark" | "system"
ctk.set_default_color_theme("blue")  # temas: blue, dark-blue, green

app = ctk.CTk()
app.title("Conversor ARS por año → USD → ARS (CTK)")
app.geometry("420x520")

# ---------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------
resultado_usd = StringVar()
resultado_final = StringVar()

# ---------------------------------------------------------
# INTERFAZ
# ---------------------------------------------------------
frame = ctk.CTkFrame(app, corner_radius=12)
frame.pack(pady=30, padx=20, fill="both", expand=False)

ctk.CTkLabel(frame, text="Valor en pesos del año origen:").pack(pady=(15, 5))
entrada_valor = ctk.CTkEntry(frame, width=200)
entrada_valor.pack()
entrada_valor.bind("<KeyRelease>", convertir)

# Año origen
ctk.CTkLabel(frame, text="Año origen:").pack(pady=(15, 5))
combo_origen = ctk.CTkComboBox(frame, values=[str(a) for a in TASAS.keys()], width=150)
combo_origen.set("2014")
combo_origen.pack()
combo_origen.bind("<<ComboboxSelected>>", convertir)

# Año destino
ctk.CTkLabel(frame, text="Año destino:").pack(pady=(15, 5))
combo_destino = ctk.CTkComboBox(frame, values=[str(a) for a in TASAS.keys()], width=150)
combo_destino.set("2025")
combo_destino.pack()
combo_destino.bind("<<ComboboxSelected>>", convertir)

# Resultados
ctk.CTkLabel(frame, text="Equivalente en USD:", font=("Arial", 15)).pack(pady=(20, 5))
ctk.CTkLabel(frame, textvariable=resultado_usd, font=("Arial", 20, "bold")).pack()

ctk.CTkLabel(frame, text="Equivalente en pesos del año destino:", font=("Arial", 15)).pack(pady=(20, 5))
ctk.CTkLabel(frame, textvariable=resultado_final, font=("Arial", 25, "bold")).pack()

# ---------------------------------------------------------
# LOOP
# ---------------------------------------------------------
app.mainloop()