# mcp-client

Command to run only once time: on inside to mcp-client directory

```uv add mcp[cli]```


## 1.Server Resource Discovery

Run the basic client to discover what resources the flight booking server provides. The server offers multiple resources that clients can access.

🔍 Discovery Task:

    Open a new terminal (keep the server terminal running!)
    Navigate to the mcp-client project directory
    Run the basic client to see all available resources
    Identify the additional resource beyond the airports data

Command to run:

```sh
cd /PATH-PROJECT/mcp-client
uv run python basic_client.py
```

💡 Look for the "Available Resources" section in the output!


## 2.Tool Parameter Analysis

Examine the tools_client.py file to understand how MCP clients call server tools with specific parameters.

📋 Analysis Task:

    Open and examine the file: /PATH-PROJECT/mcp-client/tools_client.py
    Look at the search_flights tool call in Test 1
    Identify the destination airport parameter value
    Optionally run the client to see the tools in action

🔍 Code Location:

```sh
flight_result = await client.call_tool("search_flights", {
    "origin": "LAX",
    "destination": "???"
})
```

Command to test:

```sh
cd /PATH-PROJECT/mcp-client
uv run python tools_client.py
```

💡 Find the destination airport code used in the search_flights tool call!

## 3.MCP Roots Configuration

Examine the roots_client.py file to understand which directories are provided as file system roots to the server.

📋 Analysis Task:

    Open and examine the file: /PATH-PROJECT/mcp-client/roots_client.py
    Look at the project_roots list defined at the top
    Identify which directory path is NOT included in the current roots
    Optionally run the client to see roots functionality

🔍 Code Location:
```sh
project_roots = [
    "file:///PATH-PROJECT/",
    "file:///PATH-PROJECT/flight-booking-server/",
    "file:///PATH-PROJECT/mcp-client/"
]
```
Command to test:
```sh
cd /PATH-PROJECT/mcp-client
uv run python roots_client.py
```
💡 Which directory is missing from the roots list?

## 4.Implementing Sampling Support

Sampling allows servers to request LLM responses from clients. Learn how to handle these requests.

    Examine the sampling_client.py file
    Run it to see the sampling callback in action
    Understand how to handle CreateMessageRequestParams
    See how to return CreateMessageResult responses

Command to run:
```sh
cd /PATH-PROJECT/mcp-client
uv run python sampling_client.py
```
🤖 Sampling scenarios handled:

    Travel explanation requests
    Story creation requests
    General recommendation requests

## 5.Implementing Interactive Elicitation

Elicitation allows servers to request user input from clients. Experience true interactive MCP communication where the server can ask you for information directly.

    Examine the elicitation_client.py file
    Run it to see the interactive elicitation callback
    Understand how real user input is captured
    Experience live server-to-user communication

Command to run:
```sh
cd /PATH-PROJECT/mcp-client
uv run python elicitation_client.py
```
🔔 Interactive features:

    Real-time user input prompts
    Intelligent response parsing (text or JSON)
    User can cancel with Ctrl+C
    Supports various input formats

## 6.Complete MCP Client Implementation

Now let's test a complete client that combines all MCP capabilities in one comprehensive implementation.

    Examine the complete_client.py file
    Run it to see all features working together
    Observe the phased testing approach
    See how all callbacks work in harmony

Command to run:
```sh
cd /PATH-PROJECT/mcp-client
uv run python complete_client.py
```
🌟 Complete client features:

    Server discovery and capability listing
    Tool execution and resource access
    Roots provision for file system access
    Sampling for LLM request handling
    Elicitation for user input handling