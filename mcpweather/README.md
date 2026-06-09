# MCP Server para el Servicio Meteorológico Nacional de EE.UU. (weather.gov)

## Estructura del proyecto

```
mcpweather/
├── main.py          # Punto de entrada del servidor MCP
├── weather.py       # Implementación de herramientas y lógica del servicio
├── pyproject.toml   # Configuración del proyecto y dependencias
├── uv.lock          # Lock file de dependencias
├── .gitignore       # Archivos ignorados por Git
├── .python-version  # Versión de Python (3.12)
└── README.md        # Este archivo
```

## Configuración del entorno

### 1. Instalar dependencias

```bash
cd mcpweather && uv sync
```

Esto instalará todas las dependencias definidas en `pyproject.toml` (httpx, mcp[cli], etc.) usando el lock file `uv.lock`.

### 2. Ejecutar el servidor

```bash
cd mcpweather && uv run python main.py
```

## Archivo `weather.py`

El archivo `weather.py` contiene toda la lógica del servidor MCP utilizando **FastMCP**. A continuación se detalla su contenido:

### Herramientas (Tools) — 2 disponibles

Se definen mediante el decorador `@mcp.tool()`:

1. **`get_alerts(state: str)`** — Obtiene alertas meteorológicas activas para un estado de EE.UU. Recibe el código de 2 letras del estado (ej: `CA`, `NY`, `FL`, `TX`) y devuelve eventos, área afectada, severidad, descripción e instrucciones.

2. **`get_forecast(latitude: float, longitude: float)`** — Obtiene el pronóstico del tiempo para una ubicación. Recibe coordenadas de latitud y longitud, consulta el grid de pronóstico de weather.gov y devuelve los próximos 5 períodos (día/noche) con temperatura, viento y pronóstico detallado.

### Resources — 0 disponibles

No se definen recursos (`@mcp.resource()`) en este servidor.

### Prompts — 0 disponibles

No se definen prompts (`@mcp.prompt()`) en este servidor.

### Funciones auxiliares internas

- **`make_nws_request(url: str) -> dict | None`**: Realiza peticiones HTTP asíncronas a la API de weather.gov. Maneja errores de conexión y timeouts.
- **`format_alert(feature: dict) -> str`**: Formatea una alerta meteorológica (feature GeoJSON) en un string legible con evento, área, severidad, descripción e instrucciones.

### Constantes

- **`NWS_API_BASE = "https://api.weather.gov"`**: URL base de la API del Servicio Meteorológico Nacional de EE.UU.
- **`USER_AGENT = "weather-app/1.0"`**: User-Agent para las peticiones HTTP.

## Ejecutar y probar tu servidor MCP desde un agente de IA

Configura el servidor en la configuración de MCP de tu agente:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\mcpweather",
        "run",
        "main.py"
      ]
    }
  }
}
```

El servidor mcp `weather` expone **2 herramientas** que utilizan la API del Servicio Meteorológico Nacional de EE.UU. (weather.gov):

### 1. `get_alerts(state: str)` — Alertas meteorológicas

Obtiene alertas activas para un estado de EE.UU. Pasás el código de 2 letras del estado (ej: `CA`, `NY`, `FL`, `TX`) y devuelve:

- **Evento** (tipo de alerta: tormenta, inundación, etc.)
- **Área** afectada
- **Severidad** (extreme, severe, moderate, minor)
- **Descripción** del evento
- **Instrucciones** de seguridad

### 2. `get_forecast(latitude: float, longitude: float)` — Pronóstico del tiempo

Pasás coordenadas de latitud y longitud, y devuelve el pronóstico para los próximos **5 períodos** (día/noche) con:

- **Nombre del período** (ej: "Today", "Tonight", "Thursday")
- **Temperatura** en °F
- **Viento** (velocidad y dirección)
- **Pronóstico detallado** (descripción en texto)

### Limitaciones

- Solo cubre **EE.UU.** (depende de la API de weather.gov)
- Temperatura devuelta en **Fahrenheit** (no configurable)
- No devuelve humedad, presión barométrica, punto de rocío, etc.

Si el servidor aparece en el menú "Conectores", ahora puede probarlo ejecutando los siguientes comandos:

    ¿Qué tiempo hace en Sacramento?
    ¿Cuáles son las alertas meteorológicas activas en Texas?