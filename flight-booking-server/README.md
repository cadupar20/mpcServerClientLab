# Flight Booking Server

Before we can test MCP clients, we need to start the flight booking server that our clients will connect to.

    Open a terminal and navigate to the server directory
    Start the MCP server using the MCP CLI with streamable-http transport
    Verify the server is running on port 8000
    Leave this terminal open - the server must keep running


Command to run only once time: on inside to mcp-client directory

```uv add mcp[cli]```

Commands to run:

```sh
cd /PATH-PROJECT/flight-booking-server
uv run mcp run server.py --transport streamable-http
```

⚠️ Important:

    Server runs on 127.0.0.1:8000 (MCP CLI default)
    You should see "Server running on 127.0.0.1:8000" when server starts
    All clients are configured to connect to http://localhost:8000/mcp/
    Keep this terminal open throughout the lab!