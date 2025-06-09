from mcp.server.fastmcp import FastMCP, Image
import os
from datetime import datetime
import json

mcp = FastMCP("Image Processing Server")

@mcp.tool()
def process_image(extracted_text: str) -> str:
    """
    Read text from an image file and return the text from the file 
    """
    return extracted_text

@mcp.tool()
def save_image_text(extracted_text: str) -> str:
    """
    Read text from an image file and save it in a text file on the desktop 
    """
    desktop_path = os.path.expanduser("~/Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(desktop_path, f"claude_chat_{timestamp}.txt")
    try:

        with open(file_path, "w") as f:

            f.write(extracted_text)

        return f"text saved at: {file_path}"

    except Exception as e:

        return f"Error saving text: {str(e)}"
    

@mcp.tool()
def save_image_json(extracted_text: str, image_format: str) -> str:
    """
    Read text from an image file and save it in a text file on the desktop 
    """
    desktop_path = os.path.expanduser("~/Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(desktop_path, f"claude_chat_{timestamp}.json")
    dictionary = {
        "format": image_format,
        "content": extracted_text
    }
    json_object = json.dumps(dictionary, indent=4)
    try:

        with open(file_path, "w") as f:

            f.write(json_object)

        return f"text saved at: {file_path}"

    except Exception as e:

        return f"Error saving text: {str(e)}"
    

@mcp.tool()
def save_adhaar_info_json(Name: str, Address: str, Adhaar_Number) -> str:
    """
    Read text from image of adhaar card and save the info in it onto a json file
    there are 3 things needed to be saved

    Name: the name of the adhaar card holder
    Address: The address mentioned on the adhaar card
    Adhaar_Number: The addhar card number written on the card
    """
    desktop_path = os.path.expanduser("~/Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(desktop_path, f"claude_chat_{timestamp}.json")
    dictionary = {
        "File Type": "Adhaar",
        "Name": Name,
        "Address": Address,
        "Adhaar Number": Adhaar_Number
    }
    json_object = json.dumps(dictionary, indent=4)
    try:

        with open(file_path, "w") as f:

            f.write(json_object)

        return f"information saved at: {file_path}"

    except Exception as e:

        return f"Error saving information: {str(e)}"
    
    

# Run the MCP server
if __name__ == '__main__':
    mcp.run()