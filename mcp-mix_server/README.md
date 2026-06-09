# MCP Server basado en FastMCP Python leyendo archivos CSV y Parquet

Este servidor MCP expone herramientas para resumir archivos CSV y Parquet utilizando **FastMCP** con **pandas** y **pyarrow**. Está diseñado para ser utilizado desde agentes de IA (como Kiro o Cline) que soporten el protocolo MCP.

## Estructura del proyecto

```
mcp-mix_server/
│
├── data/                      # Archivos de datos de ejemplo
│   ├── sample.csv             # CSV: 5 registros de usuarios (id, name, email, signup_date)
│   └── sample.parquet         # Parquet: mismo contenido generado desde sample.csv
│
├── tools/                     # Definiciones de herramientas MCP
│   ├── csv_tools.py           # Herramienta: summarize_csv_file()
│   └── parquet_tools.py       # Herramienta: summarize_parquet_file()
│
├── utils/                     # Lógica reutilizable de lectura de archivos
│   └── file_reader.py         # Funciones: read_csv_summary(), read_parquet_summary()
│
├── generate_parquet.py        # Script para generar sample.parquet desde sample.csv
├── server.py                  # Crea la instancia FastMCP e importa las herramientas
├── main.py                    # Punto de entrada que ejecuta el servidor MCP
├── pyproject.toml             # Configuración del proyecto y dependencias
├── uv.lock                    # Lock file de dependencias
├── .python-version            # Versión de Python (3.12)
├── .gitignore                 # Archivos ignorados por Git
└── README.md                  # Este archivo
```

## ¿Qué hace este servidor MCP?

El servidor `MCP-Mix-Server` expone **2 herramientas** que permiten a un agente de IA leer y resumir archivos de datos:

| Herramienta | Descripción |
|------------|-------------|
| `summarize_csv_file(filename)` | Lee un archivo CSV desde `data/` y devuelve cantidad de filas y columnas |
| `summarize_parquet_file(filename)` | Lee un archivo Parquet desde `data/` y devuelve cantidad de filas y columnas |

### Resources — 0 disponibles
No se definen recursos (`@mcp.resource()`) en este servidor.

### Prompts — 0 disponibles
No se definen prompts (`@mcp.prompt()`) en este servidor.

## ¿Cómo funciona? — Flujo de ejecución de los archivos

### Orden de ejecución (de inicio a fin)

1. **`main.py`** (punto de entrada)
   - Importa la instancia `mcp` desde `server.py`
   - Ejecuta `mcp.run()` iniciando el servidor MCP

2. **`server.py`** (configuración del servidor)
   - Crea la instancia `FastMCP("MCP-Mix-Server")`
   - Importa los módulos de herramientas: `tools.csv_tools` y `tools.parquet_tools`
   - Esto ejecuta los decoradores `@mcp.tool()` registrando las herramientas

3. **`tools/csv_tools.py`** y **`tools/parquet_tools.py`** (herramientas)
   - Cada archivo define una función decorada con `@mcp.tool()`
   - Cuando el agente de IA invoca una herramienta, esta llama a la función correspondiente en `utils/file_reader.py`

4. **`utils/file_reader.py`** (lógica de lectura)
   - Contiene `read_csv_summary(filename)` que usa `pandas.read_csv()`
   - Contiene `read_parquet_summary(filename)` que usa `pandas.read_parquet()`
   - Ambas funciones determinan la ruta del archivo dentro de `data/` usando `pathlib`

### Script auxiliar

- **`generate_parquet.py`** — Lee `data/sample.csv` con pandas y lo guarda como `data/sample.parquet`. Se ejecuta manualmente con `uv run generate_parquet.py`.

## Archivo `server.py` en detalle

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP-Mix-Server")

import tools.csv_tools      # Registra summarize_csv_file como tool
import tools.parquet_tools   # Registra summarize_parquet_file como tool
```

## Configuración del entorno

### 1. Instalar dependencias

```bash
cd mcp-mix_server && uv sync
```

Esto instalará todas las dependencias definidas en `pyproject.toml` (mcp[cli], pandas, pyarrow) usando el lock file `uv.lock`.

### 2. Generar archivo Parquet (opcional, solo si falta `data/sample.parquet`)

```bash
cd mcp-mix_server && uv run generate_parquet.py
```

### 3. Ejecutar el servidor

```bash
cd mcp-mix_server && uv run main.py
```

O en Windows:

```cmd
cmd /c "cd mcp-mix_server && uv run main.py"
```

## Configurar el MCP Client (agente de IA)

Para que tu agente de IA (Kiro o Cline) pueda usar este servidor, agrega la siguiente configuración en la sección `mcpServers` de tu archivo de configuración:

```json
{
  "mcpServers": {
    "mix_server": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\mcp-mix_server",
        "run",
        "main.py"
      ]
    }
  }
}
```

> **Importante:** Reemplaza `C:\\ABSOLUTE\\PATH\\TO\\mcp-mix_server` con la ruta completa real a tu carpeta `mcp-mix_server` en tu sistema.

## Probar el servidor

Una vez configurado, puedes probar las herramientas con comandos como:

- "Summarize the CSV file named sample.csv."
- "How many rows are in sample.parquet?"
- "Resume el archivo CSV sample.csv."
- "¿Cuántas filas tiene sample.parquet?"

## Referencia

Basado en el artículo: [Building a Basic MCP Server with Python](https://www.dremio.com/blog/building-a-basic-mcp-server-with-python/)