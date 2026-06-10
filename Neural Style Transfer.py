# Install libraries
!pip install torch torchvision pillow matplotlib -q

import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# Upload Content Image and Style Image
from google.colab import files

print("Upload Content Image")
content_upload = files.upload()

print("Upload Style Image")
style_upload = files.upload()

content_path = list(content_upload.keys())[0]
style_path = list(style_upload.keys())[0]

# Load images
content = Image.open(content_path).convert("RGB")
style = Image.open(style_path).convert("RGB")

# Resize
content = content.resize((256, 256))
style = style.resize((256, 256))

# Display images
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(content)
plt.title("Content Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(style)
plt.title("Style Image")
plt.axis("off")

# Simple style transfer demo (blend images)
output = Image.blend(content, style, alpha=0.4)

plt.subplot(1,3,3)
plt.imshow(output)
plt.title("Stylized Output")
plt.axis("off")

plt.show()

# Save output
output.save("stylized_output.png")

print("Output saved as stylized_output.png")