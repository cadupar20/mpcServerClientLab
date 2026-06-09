# Welcome to FastMCP — Servidor MCP Demo

Este es un servidor MCP de ejemplo construido con **FastMCP** que demuestra los tres componentes principales del protocolo MCP: **tools**, **resources** y **prompts**.

## Estructura del proyecto

```
welcome_mcp_server/
│
├── fastmcp_quickstart.py    # Servidor MCP Demo con tool, resource y prompt
├── main.py                  # Script simple de prueba (NO es el servidor MCP)
├── pyproject.toml            # Configuración del proyecto y dependencias
├── uv.lock                   # Lock file de dependencias
├── .python-version           # Versión de Python (3.12)
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Este archivo
```

## ¿Qué hace este servidor MCP?

El servidor `Demo` expone **1 tool**, **1 resource** y **1 prompt** para demostrar las capacidades de FastMCP:

| Componente | Nombre | Descripción |
|-----------|--------|-------------|
| **Tool** | `add(a: int, b: int)` | Suma dos números enteros y devuelve el resultado |
| **Resource** | `greeting://{name}` | Devuelve un saludo personalizado "Hello, {name}!" |
| **Prompt** | `greet_user(name, style)` | Genera una plantilla de saludo en 3 estilos: friendly, formal, casual |

## Archivo `fastmcp_quickstart.py` en detalle

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

# Tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }
    return f"{styles.get(style, styles['friendly'])} for someone named {name}."
```

### Componentes explicados

- **`add(a, b)`** — Decorada con `@mcp.tool()`. Es una herramienta invocable por el agente de IA para sumar dos números.
- **`greeting://{name}`** — Decorada con `@mcp.resource()`. Es un recurso dinámico accesible mediante una URI con parámetro `{name}`.
- **`greet_user(name, style)`** — Decorada con `@mcp.prompt()`. Es una plantilla de prompt que el agente de IA puede usar para generar saludos en diferentes estilos (friendly, formal, casual).

### Nota sobre `main.py`

El archivo `main.py` no está relacionado con el servidor MCP. Es solo un script simple de prueba que imprime "Hello from welcome-mcp-server!". El servidor MCP real está en `fastmcp_quickstart.py`.

## Configuración del entorno

### 1. Instalar dependencias

```bash
cd welcome_mcp_server && uv sync
```

Esto instalará todas las dependencias definidas en `pyproject.toml` (mcp[cli]) usando el lock file `uv.lock`.

### 2. Ejecutar el servidor

```bash
cd welcome_mcp_server && uv run fastmcp_quickstart.py
```

O en Windows:

```cmd
cmd /c "cd welcome_mcp_server && uv run fastmcp_quickstart.py"
```

El servidor se ejecuta usando transporte **stdio** (por defecto). También se puede usar HTTP descomentando la línea:

```python
# mcp.run(transport="streamable-http")  # Para usar http
```

## Configurar el MCP Client (agente de IA)

Para que tu agente de IA (Kiro o Cline) pueda usar este servidor, agrega la siguiente configuración en la sección `mcpServers` de tu archivo de configuración:

```json
{
  "mcpServers": {
    "fastmcp_quickstart": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\welcome_mcp_server",
        "run",
        "fastmcp_quickstart.py"
      ]
    }
  }
}
```

> **Importante:** Reemplaza `C:\\ABSOLUTE\\PATH\\TO\\welcome_mcp_server` con la ruta completa real a tu carpeta `welcome_mcp_server` en tu sistema.

## Ejemplos de uso

Una vez configurado, puedes probar el servidor con comandos como:

### Tool — Suma de números
- "Add 5 and 3."
- "What is 1234 + 5678?"
- "Suma 10 y 20."

### Resource — Saludo personalizado
- Accede al recurso `greeting://Mundo` → "Hello, Mundo!"
- Accede al recurso `greeting://Alice` → "Hello, Alice!"

### Prompt — Plantilla de saludo
- "Greet user Juan with a friendly style."
- "Generate a formal greeting for someone named Dr. Smith."
- "Saluda a María de forma casual."