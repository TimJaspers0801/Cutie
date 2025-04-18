import os
import shutil
import tqdm
import numpy as np
from glob import glob
from PIL import Image


def create_machine_mask(mask_path, output_path, color_palette):
    """Convert an RGB mask to a grayscale machine mask based on the color palette."""
    mask = Image.open(mask_path).convert("RGB")
    mask_array = np.array(mask)

    machine_mask = np.zeros(mask_array.shape[:2], dtype=np.uint8)

    for class_id, color in color_palette.items():
        matches = np.all(mask_array == color, axis=-1)
        machine_mask[matches] = class_id

    Image.fromarray(machine_mask).save(output_path)


def process_video_folder(video_path, new_video_path, color_palette):
    """Process a single video folder, splitting it into clips and creating machine masks."""
    images_path = os.path.join(video_path, "images")
    masks_path = os.path.join(video_path, "masks")

    # Get and sort the mask files
    mask_files = sorted(glob(os.path.join(masks_path, "frame_*.png")),
                        key=lambda x: int(x.split('_')[-1].split('.')[0]))

    if not mask_files:
        print(f"Skipping {video_path}, no mask files found.")
        return

    # Create the main folder for the new video
    os.makedirs(new_video_path, exist_ok=True)

    current_clip = 1
    frames_in_clip = []

    for i in tqdm.tqdm(range(len(mask_files)), total=len(mask_files),
                       desc=f"Processing {os.path.basename(video_path)}"):
        mask_file = mask_files[i]
        frame_number = os.path.basename(mask_file).split('_')[-1].split('.')[0]

        if os.path.exists(mask_file):
            frames_in_clip.append(frame_number)

            if i == len(mask_files) - 1 or int(
                    os.path.basename(mask_files[i + 1]).split('_')[-1].split('.')[0]) != int(frame_number) + 1:
                # Create clip folders
                clip_folder = os.path.join(new_video_path, f"clip_{current_clip:04d}")
                images_clip_folder = os.path.join(clip_folder, "images")
                masks_clip_folder = os.path.join(clip_folder, "masks")
                machine_masks_folder = os.path.join(clip_folder, "machine_masks")
                os.makedirs(images_clip_folder, exist_ok=True)
                os.makedirs(masks_clip_folder, exist_ok=True)
                os.makedirs(machine_masks_folder, exist_ok=True)

                # Copy images, masks, and create machine masks
                for frame in frames_in_clip:
                    # check if frame has 04 or 06 digits
                    img_file = os.path.join(images_path, f"frame_{frame}.jpg")
                    mask_file = os.path.join(masks_path, f"frame_{frame}.png")
                    machine_mask_file = os.path.join(machine_masks_folder, f"frame_{frame}.png")


                    if os.path.exists(img_file):
                        shutil.copy(img_file, os.path.join(images_clip_folder, os.path.basename(img_file)))
                    shutil.copy(mask_file, os.path.join(masks_clip_folder, os.path.basename(mask_file)))
                    create_machine_mask(mask_file, machine_mask_file, color_palette)

                current_clip += 1
                frames_in_clip = []


def process_dataset(main_folder, new_main_folder, color_palette):
    """Processes all video folders in the dataset."""
    os.makedirs(new_main_folder, exist_ok=True)
    video_folders = [f for f in glob(os.path.join(main_folder, "*")) if os.path.isdir(f)]

    for video_folder in tqdm.tqdm(video_folders, desc="Processing dataset"):
        video_name = os.path.basename(video_folder)
        new_video_path = os.path.join(new_main_folder, video_name)
        process_video_folder(video_folder, new_video_path, color_palette)


# Define the color palette
color_palette = {
    1: (255, 255, 255), 2: (0, 0, 255), 3: (255, 0, 0), 4: (255, 255, 0), 5: (0, 255, 0),
    6: (0, 200, 100), 7: (200, 150, 100), 8: (250, 150, 100), 9: (255, 200, 100), 10: (180, 0, 0),
    11: (0, 0, 180), 12: (150, 100, 50), 13: (0, 255, 255), 14: (0, 200, 255), 15: (0, 100, 255),
    16: (255, 150, 50), 17: (255, 220, 200), 18: (200, 100, 200), 19: (144, 238, 144), 20: (247, 255, 0),
    21: (255, 206, 27), 22: (200, 0, 200), 23: (255, 0, 150), 24: (255, 100, 200), 25: (200, 100, 255),
    26: (150, 0, 100), 27: (255, 200, 255), 28: (150, 100, 75), 29: (200, 0, 150), 30: (100, 100, 100),
    31: (255, 150, 255), 32: (100, 200, 255), 33: (150, 200, 255), 34: (0, 150, 255), 35: (255, 100, 100),
    36: (200, 200, 255), 37: (100, 100, 255), 38: (0, 255, 150), 39: (255, 255, 100), 40: (150, 150, 150),
    41: (50, 50, 50), 43: (173, 216, 230), # Mesocolon - Light Blue 2
    255: (0, 0, 0)
}


# Example usage
main_folder = r"E:\SurgeSAM\RARP"
new_main_folder = r"E:\SurgeSAM_processed\RARP"
process_dataset(main_folder, new_main_folder, color_palette)