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
    prepare a very simple and extremely modern look certificate with white backgroud
    and slight red contour used for framing, style use minimalist. incorporate
    only the following text ["Certificate", "Name of Trainee", "Approved by"]
    AS-IS. put the text in appropriate place
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
cv2.imwrite('raw_generated_4.png', img)
