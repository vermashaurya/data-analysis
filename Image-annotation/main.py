import os
import time
from PIL import Image
import numpy as np
import cv2

def get_basic_info(image_path):
    with Image.open(image_path) as img:
        info = {
            "Format": img.format,
            "Mode": img.mode,
            "Size (Width x Height)": img.size,
        }
    return info

def get_file_metadata(image_path):
    file_stats = os.stat(image_path)
    metadata = {
        "File Size (in bytes)": file_stats.st_size,
        "File Size (in KB)": file_stats.st_size / 1024,
        "File Size (in MB)": file_stats.st_size / (1024 * 1024),
        "Created": time.ctime(file_stats.st_ctime),
        "Modified": time.ctime(file_stats.st_mtime),
    }
    return metadata

def get_cv2_info(image_path):
    img = cv2.imread(image_path)
    height, width, channels = img.shape
    info = {
        "Height (pixels)": height,
        "Width (pixels)": width,
        "Channels": channels,
        "Resolution (DPI)": img.shape[:2],
    }
    return info

def extract_image_metadata(image_path):
    metadata = {}
    metadata.update(get_basic_info(image_path))
    metadata.update(get_file_metadata(image_path))
    metadata.update(get_cv2_info(image_path))
    return metadata

image_path = "image1.jpg"
metadata = extract_image_metadata(image_path)

print("Image Metadata:")
for key, value in metadata.items():
    print(f"{key}: {value}")

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

img = cv2.imread(image_path)
height, width, channels = img.shape

blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

boxes = []
confidences = []
class_ids = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

for i in indices:
    if isinstance(i, (list, tuple, np.ndarray)):
        i = i[0]
    box = boxes[i]
    x, y, w, h = box[0], box[1], box[2], box[3]
    label = str(classes[class_ids[i]])
    color = (0, 255, 0)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

output_path = "output_image.jpg"
cv2.imwrite(output_path, img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
