import os
from PIL import Image
from pathlib import Path

# Path to the directory containing images
directory_path = Path("/home/ckadirt/Desktop/Radient/Epilogo Project/images/style_3")

# Ensure directory exists
if not directory_path.exists():
    print(f"Directory not found: {directory_path}")
    exit(1)

total_original_size = 0
total_new_size = 0

print(f"Processing images in {directory_path}...")

for file_path in directory_path.glob("*.png"):
    try:
        # Open source image
        with Image.open(file_path) as img:
            # Construct new file path with .webp extension
            new_file_path = file_path.with_suffix('.webp')
            
            # Save as WebP
            img.save(new_file_path, 'WEBP', quality=85, method=6)
            
            original_size = file_path.stat().st_size
            new_size = new_file_path.stat().st_size
            
            total_original_size += original_size
            total_new_size += new_size
            
            print(f"Converted {file_path.name}: {original_size/1024/1024:.2f}MB -> {new_size/1024/1024:.2f}MB")
            
    except Exception as e:
        print(f"Failed to convert {file_path.name}: {e}")

print("\nConversion Complete!")
print(f"Total Original Size: {total_original_size/1024/1024:.2f}MB")
print(f"Total New Size: {total_new_size/1024/1024:.2f}MB")
print(f"Space Saved: {(total_original_size - total_new_size)/1024/1024:.2f}MB")
