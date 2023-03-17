import torch
import cv2
import numpy as np

# Load the pre-trained model
model = torch.load('faster_rcnn_pytorch.pth')
model.eval()

# Load the input image
image = cv2.imread('input.jpg')

# Resize the input image
image = cv2.resize(image, (800, 600))

# Normalize the input image
image = (image / 255.0 - 0.5) / 0.5

# Convert the input image to a PyTorch tensor
tensor = torch.tensor(image.transpose(2, 0, 1), dtype=torch.float32)

# Feed the input tensor to the model and get the predicted bounding boxes
with torch.no_grad():
    boxes = model([tensor])

# Draw the predicted bounding boxes on the input image
for box in boxes[0]['boxes']:
    x1, y1, x2, y2 = box.tolist()
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

# Display the output image
cv2.imshow('Output', image)
cv2.waitKey(0)
