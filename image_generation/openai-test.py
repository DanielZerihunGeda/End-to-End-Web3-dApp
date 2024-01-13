from openai import OpenAI
from dotenv import load_dotenv
import cv2
import os
import numpy as np
from io import BytesIO
import base64 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.images.generate(
    model='dall-e-3',
    prompt="""
    a simple and highly clear block diagram that illustrates the relationship between the following concepts:
      [Web 3.0 , Blockchain, Wallet and fungible]
    and non-fungible token, use diagram to show relation between them 
    make the design simple but incorporate all the concepts
    and the diagram must be extremely clear 
    """,
    n=1,
    size="1024x1024",
    quality='standard',
    response_format='b64_json'
)

# Extract base64 image data from the b64_json response
img_data = response.data[0].b64_json

# Convert base64 image to OpenCV format
img_np = np.frombuffer(base64.b64decode(img_data), dtype=np.uint8)
img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

# Display the image using OpenCV
cv2.imwrite('diagram.png', img)
