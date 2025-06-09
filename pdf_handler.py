from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage
import base64
import io

mcp = FastMCP("PDF Processing Server")

@mcp.tool()
def process_pdf(extracted_text: str) -> str:
    """
    Read a pdf file and return the text from the file 
    """
    return extracted_text
    
    

# Run the MCP server
if __name__ == '__main__':
    mcp.run()