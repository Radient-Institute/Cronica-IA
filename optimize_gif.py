from PIL import Image
from pathlib import Path
import sys

source_path = Path("/home/ckadirt/Desktop/Radient/Epilogo Project/images/style_3/l_video.gif")

if not source_path.exists():
    print(f"Error: {source_path} does not exist.")
    sys.exit(1)

dest_path = source_path.with_suffix('.webp')

print(f"Opening {source_path}...")
try:
    with Image.open(source_path) as im:
        original_size = source_path.stat().st_size
        print(f"Original size: {original_size / 1024 / 1024:.2f} MB")
        
        # Get duration from the first frame, default to 100ms if not present
        duration = im.info.get('duration', 100)
        
        print("Converting to animated WebP...")
        # save_all=True is required to save all frames of an animation
        # method=6 is the slowest compression method but produces best compression
        # quality=80 is a good tradeoff
        im.save(dest_path, 'webp', save_all=True, optimize=True, duration=duration, loop=0, quality=50, method=6)
        
        new_size = dest_path.stat().st_size
        print(f"New size: {new_size / 1024 / 1024:.2f} MB")
        print(f"Reduction: {100 * (original_size - new_size) / original_size:.1f}%")

except Exception as e:
    print(f"An error occurred: {e}")
