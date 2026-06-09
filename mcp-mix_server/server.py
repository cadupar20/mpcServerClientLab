# server.py
from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("MCP-Mix-Server")

# Import tools so they get registered via decorators
import tools.csv_tools
import tools.parquet_tools

# Entry point to run the server
if __name__ == "__main__":
    mcp.run()
