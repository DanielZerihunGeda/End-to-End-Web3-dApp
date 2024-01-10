from openai import OpenAI
from dotenv import load_dotenv
import cv2
import os
import numpy as np
from io import BytesIO
from PIL import Image
import base64 

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.images.generate(
    model='dall-e-3',
    prompt="""
    you are professional certificate designer:

must Specify the following for a clean and contemporary look:
   - Layout: Portrait orientation with precise A4 dimensions (8.27 × 11.69 inches or 210 × 297 mm)
   - Background: Clean white with no texture, subtle and professional
   - Text Placement:
      - Certificate Title: Centered at the top, Times New Roman
      - Recipient's Name: Below the certificate title, centered
      - Training Program Title: Centered below the recipient's name
      - Organization Name: Positioned prominently at the top
      - Date of Completion: Near the bottom, right-aligned
      - Issued By: At the bottom, left-aligned, with a clear space for a realistic signature
   - Logo Design: Generate a simple and visible logo for "10 Academy" at the top left without distortion
   - Style and Colors: Modern, professional, and minimalist with precise color representation

Please ensure that the generated a single image strictly adheres to the A4 dimensions and follows modern design aesthetics for a professional appearance. Avoid any framing and background only the certificate, make sure to generate full size image.
""",
    n=1,
    size="1024x1024",
    quality='standard',
    response_format='b64_json'
)

# Extract base64 image data from the b64_json response
img_data = response.data[0].b64_json

# Convert base64 image to OpenCV format
img = Image.open(BytesIO(base64.b64decode(img_data)))
img_np = np.array(img)

# Your OpenCV enhancements here
# For example, resize the image to A4 dimensions (210 × 297 mm)
a4_width, a4_height = 210, 297
resized_image = cv2.resize(img_np, (int(a4_width * 3.78), int(a4_height * 3.78)))  # Conversion factor from mm to pixels

# Save the enhanced image
cv2.imshow('Enhanced Certificate', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()