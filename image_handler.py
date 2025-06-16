from mcp.server.fastmcp import FastMCP, Image
import os
from datetime import datetime
import json
from PIL import Image as PILImage
import numpy as np
from typing import List
import base64
import io
from pdf2image import convert_from_path
import fitz

mcp = FastMCP("Image Processing Server")

    

@mcp.tool()
def save_image_text_json(image_format: str, extracted_text: str) -> str:
    """
    Read text from an image file and save it in a json file on the desktop 
    There are 2 input arguments
    image_format: the format of the image, like png, jpeg
    extracted_text: the text extracted from the image
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

    

@mcp.tool()
def file_enumerator() -> List[str]:
    """
    Go through the names of all files in a folder and return the names.
    """

    folder_path = "C:/Users/Umair/Documents/Coding/MCP/Images"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    return files

@mcp.tool()
def get_image_data(image_name: str, file_type: str) -> Image:
    """
    Receives an image name and returns the image data.
    There is 1 input argument
    image_name: the name of the image/file, including its extension like .png, .jpg, .pdf
    file_type: the type of the file, if it is png, jpg, pdf etc. if it is a pdf, it gets converted to an image type file and returned
    """
    folder_path = "C:/Users/Umair/Documents/Coding/MCP/Images"
    image_path = os.path.join(folder_path, image_name)
    if file_type == "pdf":
        try:
            pdf_document = fitz.open(image_path)
        
            # Convert first page to image
            page = pdf_document.load_page(0)
            pixmap = page.get_pixmap()
            image_path = f"{folder_path}/page_{1}.png"
            pixmap.save(image_path)
            
            # pdf_document.close()
            
            # # Encode as base64 for JSON serialization
            # encoded_content = base64.b64encode(img_data).decode('utf-8')
            
            #return Image(pixmap)
        except Exception as e:
            return None
    return Image(path=image_path)



    

# Run the MCP server
if __name__ == '__main__':
    mcp.run()