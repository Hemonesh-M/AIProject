import os
import shutil
import random

# Set up folders
base_path = "dataset"
img_dir = os.path.join(base_path, "images")
lbl_dir = os.path.join(base_path, "labels")

# Create train/val folders
for split in ['train', 'val']:
    os.makedirs(os.path.join(img_dir, split), exist_ok=True)
    os.makedirs(os.path.join(lbl_dir, split), exist_ok=True)

# Get all image names
images = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png'))]

# Shuffle and split
random.shuffle(images)
split_index = int(0.8 * len(images))
train_imgs = images[:split_index]
val_imgs = images[split_index:]

# Move files
def move_files(img_list, split):
    for img in img_list:
        name = os.path.splitext(img)[0]
        label = name + ".txt"

        shutil.move(os.path.join(img_dir, img), os.path.join(img_dir, split, img))
        shutil.move(os.path.join(lbl_dir, label), os.path.join(lbl_dir, split, label))

move_files(train_imgs, 'train')
move_files(val_imgs, 'val')

print(f"✅ Done! {len(train_imgs)} training, {len(val_imgs)} validation images.")
