# Native_MCP

A Model Context Protocol (MCP) server for React Native development tools and utilities.

<a href="https://glama.ai/mcp/servers/@ArkVex/Native_MCP">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@ArkVex/Native_MCP/badge" alt="Native_MCP MCP server" />
</a>

## 🚀 Overview

Native_MCP is an extensible MCP server that provides tools and utilities for React Native development. It allows AI assistants like Claude to generate React Native components and perform other development tasks through a standardized protocol.

## ✨ Features

- **React Native Component Generator**: Automatically generate React Native components with proper structure
- **Extensible Tool System**: Add custom tools through a simple plugin architecture
- **MCP Protocol Compliance**: Full compatibility with Model Context Protocol 2025-06-18
- **Dynamic Tool Loading**: Tools are loaded dynamically from the `tools/` directory

## 🛠️ Available Tools

### React Native Helper
- **generate_component**: Generate a basic React Native functional component
  - Input: `component_name` (string)
  - Output: Complete React Native component code with View and Text elements

## 📋 Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- VS Code with Claude extension (for MCP integration)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ArkVex/Native_MCP.git
   cd Native_MCP
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Verify installation**:
   ```bash
   uv run mcp_server.py
   ```

## 🚀 Usage

### With Claude in VS Code

1. **Configure the MCP server** in your Claude settings:
   ```json
   {
     "mcpServers": {
       "native-mcp": {
         "command": "uv",
         "args": [
           "--directory",
           "C:\\path\\to\\Native_MCP",
           "run",
           "mcp_server.py"
         ]
       }
     }
   }
   ```

2. **Start using the tools** in Claude:
   - Ask Claude to "generate a React Native component called LoginScreen"
   - Claude will use the `generate_component` tool automatically

### Manual Testing

You can test the server manually using JSON-RPC:

```bash
# Initialize the server
echo '{"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test-client","version":"0.1.0"}},"jsonrpc":"2.0","id":0}' | uv run mcp_server.py

# List available tools
echo '{"method":"tools/list","params":{},"jsonrpc":"2.0","id":1}' | uv run mcp_server.py

# Generate a component
echo '{"method":"tools/call","params":{"name":"generate_component","arguments":{"component_name":"MyButton"}},"jsonrpc":"2.0","id":2}' | uv run mcp_server.py
```

## 📁 Project Structure

```
Native_MCP/
├── mcp_server.py          # Main MCP server implementation
├── pyproject.toml         # Project configuration
├── requirements.txt       # Python dependencies
├── tools/                 # Tool plugins directory
│   └── react-native-helper/
│       ├── main.py        # Tool implementation
│       └── mcp.json       # Tool metadata
├── .venv/                 # Virtual environment
└── README.md             # This file
```

## 🔌 Adding Custom Tools

To add a new tool to the server:

1. **Create a tool directory**:
   ```bash
   mkdir tools/my-custom-tool
   ```

2. **Create the tool implementation** (`tools/my-custom-tool/main.py`):
   ```python
   def my_function(params):
       # Your tool logic here
       result = params.get("input", "default")
       return {"output": f"Processed: {result}"}
   ```

3. **Create the tool metadata** (`tools/my-custom-tool/mcp.json`):
   ```json
   {
     "name": "my-custom-tool",
     "entry_point": "main.py",
     "commands": {
       "my_function": {
         "description": "Description of what this tool does",
         "params": {
           "input": "string"
         }
       }
     }
   }
   ```

4. **Restart the server** - tools are loaded automatically

## 🐛 Troubleshooting

### Server Won't Start
- Ensure Python 3.12+ is installed
- Verify `uv` is installed and in your PATH
- Check that all dependencies are installed with `uv sync`

### Tools Not Loading
- Verify tool directory structure matches the expected format
- Check that `mcp.json` is valid JSON
- Ensure the entry point file exists and functions are named correctly

### Connection Issues
- Verify the MCP server path in your Claude configuration
- Check that the server process isn't already running
- Review the Claude extension logs for detailed error messages

## 📖 API Reference

### MCP Protocol Methods

- `initialize`: Initialize the server connection
- `tools/list`: Get list of available tools
- `tools/call`: Execute a specific tool
- `resources/list`: List available resources (currently empty)
- `prompts/list`: List available prompts (currently empty)

### Tool Response Format

Tools return responses in the MCP standard format:
```json
{
  "content": [
    {
      "type": "text",
      "text": "Tool output here"
    }
  ]
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-tool`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add new tool'`
5. Push to the branch: `git push origin feature/new-tool`
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/) for the specification
- [Anthropic](https://www.anthropic.com/) for Claude and MCP support
- [React Native](https://reactnative.dev/) community for inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/ArkVex/Native_MCP/issues)
3. Create a new issue with detailed information about your problem

---

**Made with ❤️ for the React Native and AI development community**