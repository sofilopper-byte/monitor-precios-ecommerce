                                            Monitor de Precios E-commerce - Farmacity

Este es un proyecto de automatización desarrollado en **Python** que realiza Web Scraping sobre el sitio de Farmacity para monitorear el precio de productos específicos (como máscaras de pestañas Maybelline) y detectar ofertas de manera automática.

Tecnologías y Conceptos Aplicados
*   **Lenguaje:** Python 3.13
*   **Web Scraping:** `BeautifulSoup4` para el parseo del HTML.
*   **Peticiones HTTP:** Librería `requests` con configuración de `Headers` (User-Agent) para emular navegación humana.
*   **Procesamiento de Datos:** Uso de **Expresiones Regulares (Regex)** para extraer y limpiar patrones de precios dentro de bloques de texto.
*   **Lógica de Negocio:** Comparación de precios contra un umbral (threshold) definido por el usuario.

Funcionalidades
1.  Conexión automática a la URL del producto.
2.  Extracción del precio actual ignorando elementos visuales o banners publicitarios.
3.  Limpieza de strings y conversión de formatos monetarios a valores numéricos (`float`).
4.  Alerta visual en consola cuando el precio baja del límite establecido.
5.  *Estructura lista para integración con Bots de Telegram.*

Requisitos e Instalación
Para ejecutar este script, necesitás tener Python instalado y las siguientes dependencias:

```bash
# Instalación de librerías necesarias
pip install requests beautifulsoup4
