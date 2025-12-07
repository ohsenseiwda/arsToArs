import customtkinter as ctk
from tkinter import StringVar



TASAS = {
    2000: 1.00, 2001: 1.00, 2002: 3.13, 2003: 2.95, 2004: 2.94,
    2005: 2.92, 2006: 3.07, 2007: 3.11, 2008: 3.16, 2009: 3.73,
    2010: 3.91, 2011: 4.12, 2012: 4.55, 2013: 5.47, 2014: 8.11,
    2015: 9.26, 2016: 14.77, 2017: 16.56, 2018: 28.08, 2019: 48.19,
    2020: 70.53, 2021: 95.08, 2022: 130.88, 2023: 296.43,
    2024: 916.85, 2025: 1215.46,
}

YEARS = sorted(TASAS.keys())
PLACEHOLDER = "—"


def format_amount(value: float, suffix: str = "ARS") -> str:
    """Formatea un número con separador de miles y 2 decimales.

    No depende de locale para mantener consistencia en diferentes entornos.
    """
    return f"{value:,.2f} {suffix}"


def compute_conversion(text: str, origen: int, destino: int) -> tuple:
    """Convierte `text` (valor en ARS del año `origen`) a USD y ARS del `destino`.

    Lanza ValueError si la entrada no es numérica y KeyError si falta una tasa.
    """
    if not text or text.strip() == "":
        raise ValueError("valor vacío")

    # Permitimos comas en la entrada (p.ej. "1,234.56") y espacios
    cleaned = text.replace(",", "").replace(" ", "")
    valor_inicial = float(cleaned)

    tasa_origen = TASAS[origen]
    tasa_destino = TASAS[destino]

    usd = valor_inicial / tasa_origen
    valor_destino = usd * tasa_destino

    return usd, valor_destino


class ArsConverterApp:
    """Encapsula la aplicación CTk para convertir ARS (por año) → USD → ARS."""

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Conversor ARS por año → USD → ARS (CTK)")
        self.app.geometry("420x520")

        # Variables de estado
        self.resultado_usd = StringVar(value=PLACEHOLDER)
        self.resultado_final = StringVar(value=PLACEHOLDER)

        # Interfaz
        self._build_ui()

    def _label(self, parent, text, font=None, pady=(0, 0)):
        ctk.CTkLabel(parent, text=text, font=font).pack(pady=pady)

    def _crear_combobox_anio(self, parent, default: int):
        combo = ctk.CTkComboBox(parent, values=[str(y) for y in YEARS], width=150)
        combo.set(str(default))
        combo.pack()
        combo.bind("<<ComboboxSelected>>", lambda e: self.on_change())
        return combo

    def _build_ui(self):
        frame = ctk.CTkFrame(self.app, corner_radius=12)
        frame.pack(pady=30, padx=20, fill="both", expand=False)

        self._label(frame, "Valor en pesos del año origen:", pady=(15, 5))
        self.entrada_valor = ctk.CTkEntry(frame, width=200)
        self.entrada_valor.pack()
        self.entrada_valor.bind("<KeyRelease>", lambda e: self.on_change())

        self._label(frame, "Año origen:", pady=(15, 5))
        self.combo_origen = self._crear_combobox_anio(frame, default=2014)

        self._label(frame, "Año destino:", pady=(15, 5))
        self.combo_destino = self._crear_combobox_anio(frame, default=2025)

        self._label(frame, "Equivalente en USD:", font=("Arial", 15), pady=(20, 5))
        ctk.CTkLabel(frame, textvariable=self.resultado_usd, font=("Arial", 20, "bold")).pack()

        self._label(frame, "Equivalente en pesos del año destino:", font=("Arial", 15), pady=(20, 5))
        ctk.CTkLabel(frame, textvariable=self.resultado_final, font=("Arial", 25, "bold")).pack()

    def on_change(self, *_):
        try:
            texto = self.entrada_valor.get()
            año_origen = int(self.combo_origen.get())
            año_destino = int(self.combo_destino.get())

            usd, valor_destino = compute_conversion(texto, año_origen, año_destino)

            self.resultado_usd.set(format_amount(usd, "USD"))
            self.resultado_final.set(format_amount(valor_destino, "ARS"))

        except (ValueError, KeyError):
            self.resultado_usd.set(PLACEHOLDER)
            self.resultado_final.set(PLACEHOLDER)

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    ArsConverterApp().run()
