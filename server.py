from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greeter")


@mcp.tool()
def greet() -> str:
    """Return this welcome message, when greeted with "Hi", "Hey" or "Hello"."""
    return "Hey Llama, Welcome to the world of MCPs!"


if __name__ == "__main__":

    mcp.run()