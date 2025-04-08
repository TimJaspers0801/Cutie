import os
import re

import os
import re


def rename_mask_files(folder_path):
    pattern = re.compile(r"frame_(\d{4,5})\.png")  # Matches 'frame_XXXX.png'
    offset = 168

    # Get list of matching files and sort in descending order
    files = sorted([f for f in os.listdir(folder_path) if pattern.match(f)], reverse=True)

    for filename in files:
        match = pattern.match(filename)
        if match:
            old_number = int(match.group(1))

            if old_number > 1168:
                new_number = old_number + offset
                new_filename = f"frame_{new_number:04d}.png"

                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)

                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")


# Usage example
folder_path = r"E:\SurgeSAM\cholestectomy\7ApGq0IlR3k.mp4\masks"  # Change this to your actual folder path
rename_mask_files(folder_path)