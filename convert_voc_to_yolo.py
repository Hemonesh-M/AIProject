import os
import xml.etree.ElementTree as ET
from PIL import Image

# Class labels as per your dataset
label_map = {
    "with_mask": 0,
    "without_mask": 1,
    "mask_weared_incorrect": 2
}

# Folders
xml_folder = "archive/annotations"         # All your .xml files
images_folder = "dataset/images"           # All images (.png/.jpg)
labels_output = "dataset/labels"           # Output YOLO .txt labels

os.makedirs(labels_output, exist_ok=True)

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[1]) / 2.0 * dw
    y_center = (box[2] + box[3]) / 2.0 * dh
    width = (box[1] - box[0]) * dw
    height = (box[3] - box[2]) * dh
    return (x_center, y_center, width, height)

for xml_file in os.listdir(xml_folder):
    if not xml_file.endswith(".xml"):
        continue

    path = os.path.join(xml_folder, xml_file)
    tree = ET.parse(path)
    root = tree.getroot()

    image_name = root.find("filename").text
    txt_filename = os.path.splitext(image_name)[0] + ".txt"
    txt_path = os.path.join(labels_output, txt_filename)

    try:
        width = int(root.find("size/width").text)
        height = int(root.find("size/height").text)

        with open(txt_path, "w") as f:
            for obj in root.findall("object"):
                cls = obj.find("name").text
                if cls not in label_map:
                    print(f"Skipping unknown class: {cls}")
                    continue

                cls_id = label_map[cls]
                bndbox = obj.find("bndbox")
                xmin = int(bndbox.find("xmin").text)
                ymin = int(bndbox.find("ymin").text)
                xmax = int(bndbox.find("xmax").text)
                ymax = int(bndbox.find("ymax").text)

                bbox = convert((width, height), (xmin, xmax, ymin, ymax))
                f.write(f"{cls_id} {' '.join([f'{a:.6f}' for a in bbox])}\n")

        print(f"✅ Saved: {txt_path}")

    except Exception as e:
        print(f"❌ Error processing {xml_file}: {e}")
