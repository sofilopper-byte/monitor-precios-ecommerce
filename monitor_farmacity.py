
# MONITOR DE PRECIO - FARMACITY

import requests
from bs4 import BeautifulSoup
import re


# CONFIGURACIÓN


URL = "https://www.farmacity.com/mascara-de-pestanas-maybelline-sensational-sky-high-x-7-2-ml/p"

# Umbral de alerta
UMBRAL_PRECIO = 15000

# Headers para simular un navegador real
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}



def obtener_html(url):
    """
    Realiza la petición HTTP y devuelve el HTML.
    """

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)

        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {e}")
        return None



def extraer_precio(html):
    """
    Busca el precio dentro del HTML y lo convierte a float.
    """

    soup = BeautifulSoup(html, "html.parser")

    precio_texto = None

    
    texto_completo = soup.get_text(" ", strip=True)

    patron_precio = r"\$\s?[\d\.\,]+"

    coincidencias = re.findall(patron_precio, texto_completo)

    if coincidencias:
        # Tomamos el primer precio encontrado
        precio_texto = coincidencias[0]

    # Si no encontró nada
    if not precio_texto:
        print("No se pudo encontrar el precio.")
        return None

    print(f"Precio encontrado (texto): {precio_texto}")


    precio_limpio = precio_texto

    precio_limpio = precio_limpio.replace("$", "")

    precio_limpio = precio_limpio.strip()

    precio_limpio = precio_limpio.replace(".", "")

    precio_limpio = precio_limpio.replace(",", ".")

    try:
        precio_float = float(precio_limpio)
        return precio_float

    except ValueError:
        print("Error al convertir el precio.")
        return None



def verificar_oferta(precio, umbral):
    """
    Compara el precio contra el umbral definido.
    """

    print(f"Precio actual: ${precio:,.2f}")

    if precio < umbral:
        mensaje = (
            f"¡OFERTA! 🎉\n"
            f"El producto bajó a ${precio:,.2f}\n"
            f"Umbral configurado: ${umbral:,.2f}"
        )

        print(mensaje)


    else:
        print("El precio todavía no está en oferta.")


# FUNCIÓN TELEGRAM (

# def enviar_telegram(mensaje):
#     """
#     Envía un mensaje mediante un bot de Telegram.
#     """
#
#     TOKEN = "TU_BOT_TOKEN"
#     CHAT_ID = "TU_CHAT_ID"
#
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#
#     payload = {
#         "chat_id": CHAT_ID,
#         "text": mensaje
#     }
#
#     try:
#         response = requests.post(url, data=payload)
#
#         if response.status_code == 200:
#             print("Mensaje enviado a Telegram.")
#         else:
#             print("Error enviando mensaje a Telegram.")
#
#     except Exception as e:
#         print(f"Error Telegram: {e}")



def main():

    html = obtener_html(URL)

    if not html:
        return

    precio = extraer_precio(html)

    if precio is not None:
        verificar_oferta(precio, UMBRAL_PRECIO)


if __name__ == "__main__":
    main()