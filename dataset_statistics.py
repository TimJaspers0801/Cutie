import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from collections import defaultdict
from glob import glob
import tqdm
import concurrent.futures
import multiprocessing


def get_clip_and_frame_statistics(main_folder):
    """Calculates the number of clips, annotated frames, and surgical procedures in the dataset."""
    total_clips = 0
    total_annotated_frames = 0
    total_surgical_procedures = 0
    total_videos = 0

    # Traverse all surgical procedures in the main folder
    for surgical_procedure in tqdm.tqdm(os.listdir(main_folder), desc="Processing surgical procedures"):
        surgical_procedure_path = os.path.join(main_folder, surgical_procedure)

        # Ensure we're working with directories
        if not os.path.isdir(surgical_procedure_path):
            continue

        total_surgical_procedures += 1  # Increment surgical procedure count

        total_videos += len(os.listdir(surgical_procedure_path))
        # Traverse all video folders within the surgical procedure
        for video_folder in os.listdir(surgical_procedure_path):
            video_folder_path = os.path.join(surgical_procedure_path, video_folder)

            # Ensure we're working with directories
            if not os.path.isdir(video_folder_path):
                continue

            # Traverse all clip folders within the video folder
            for clip_folder in os.listdir(video_folder_path):
                clip_folder_path = os.path.join(video_folder_path, clip_folder)

                # Ensure it's a clip folder containing images and masks
                if os.path.isdir(clip_folder_path):
                    images_folder = os.path.join(clip_folder_path, "images")
                    masks_folder = os.path.join(clip_folder_path, "masks")

                    # Check if both images and masks subfolders exist
                    if os.path.isdir(images_folder) and os.path.isdir(masks_folder):
                        # Count the number of masks (annotated frames) in the clip
                        mask_files = glob(os.path.join(masks_folder, "frame_*.png"))
                        total_annotated_frames += len(mask_files)

                        # Increment the total number of clips
                        total_clips += 1

    return total_surgical_procedures, total_videos, total_clips, total_annotated_frames





# Function to calculate the length of each clip
def get_clip_lengths(main_folder):
    clip_lengths = []

    # Loop through all surgical procedures
    for procedure_folder in os.listdir(main_folder):
        procedure_path = os.path.join(main_folder, procedure_folder)

        # Only consider folders
        if os.path.isdir(procedure_path):
            # Loop through each video folder in the procedure folder
            for video_folder in os.listdir(procedure_path):
                video_path = os.path.join(procedure_path, video_folder)

                if os.path.isdir(video_path):
                    # Loop through each clip folder in the video folder
                    for clip_folder in os.listdir(video_path):
                        clip_path = os.path.join(video_path, clip_folder)

                        if os.path.isdir(clip_path):
                            # Count the number of frames in the "images" folder
                            image_folder = os.path.join(clip_path, 'images')
                            num_frames = len(os.listdir(image_folder))  # Count the number of image files (frames)
                            clip_lengths.append(num_frames)

    return clip_lengths


# Function to create a plot of clip durations
def plot_clip_durations(clip_lengths):
    # Define bins for the clip lengths
    bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

    # Create the histogram
    n, bins, patches = plt.hist(clip_lengths, bins=bins, edgecolor='black', alpha=0.7)

    # Add labels and title
    plt.xlabel("Clip Length (Frames)")
    plt.ylabel("Number of Clips")
    plt.title("Distribution of Clip Durations")

    # Add the counts on top of each bin
    for count, bin_edge in zip(n, bins[:-1]):
        # Position the count at the center of each bin
        plt.text(bin_edge + (bins[1] - bins[0]) / 2, count + 0.05,
                 str(int(count)), ha='center', va='bottom', fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


# Define the color palette for classes
color_palette = {
    1: (255, 255, 255),  # Tools/camera - White
    2: (0, 0, 255),  # Vein (major) - Blue
    3: (255, 0, 0),  # Artery (major) - Red
    4: (255, 255, 0),  # Nerve (major) - Yellow
    5: (0, 255, 0),  # Small intestine - Green
    6: (0, 200, 100),  # Colon/rectum - Dark Green
    7: (200, 150, 100),  # Abdominal wall - Beige
    8: (250, 150, 100),  # Diaphragm - light Beige
    9: (255, 200, 100),  # Omentum - Light Orange
    10: (180, 0, 0),  # Aorta - Dark Red
    11: (0, 0, 180),  # Vena cava - Dark Blue
    12: (150, 100, 50),  # Liver - Brown
    13: (0, 255, 255),  # Cystic duct - Cyan
    14: (0, 200, 255),  # Gallbladder - Teal
    15: (0, 100, 255),  # Hepatic vein - Light Blue
    16: (255, 150, 50),  # Hepatic ligament - Orange
    17: (255, 220, 200),  # Cystic plate - Light Pink
    18: (200, 100, 200),  # Stomach - Light Purple
    19: (144, 238, 144),  # Ductus choledochus - Light Green
    20: (247, 255, 0),  # Mesenterium
    21: (255, 206, 27),  # Ductus hepaticus - Red
    22: (200, 0, 200),  # Spleen - Purple
    23: (255, 0, 150),  # Uterus - Pink
    24: (255, 100, 200),  # Ovary - Light Pink
    25: (200, 100, 255),  # Oviduct - Lavender
    26: (150, 0, 100),  # Prostate - Dark Purple
    27: (255, 200, 255),  # Urethra - Light Pink
    # 28: (150, 100, 75),  # Ligated plexus - Brown
    # 29: (200, 0, 150),  # Seminal vesicles - Magenta
    # 30: (100, 100, 100),  # Catheter - Gray
    # 31: (255, 150, 255),  # Bladder - Light Purple
    # 32: (100, 200, 255),  # Kidney - Light Blue
    # # Thorax IDs
    # 33: (150, 200, 255),  # Lung - Light Blue
    # 34: (0, 150, 255),  # Airway (bronchus/trachea) - Sky Blue
    # 35: (255, 100, 100),  # Esophagus - Salmon
    # 36: (200, 200, 255),  # Pericardium - Pale Blue
    # 37: (100, 100, 255),  # V azygos - Blue
    # 38: (0, 255, 150),  # Thoracic duct - Green Cyan
    # 39: (255, 255, 100),  # Nerves - Yellow
    # Non-anatomical structures
    # 40: (150, 150, 150),  # Firefly - Gray
    # 41: (50, 50, 50),  # Non anatomical structures - Dark Gray
    # 42: (0, 0, 0),  # Excluded frames - Black
}

class_names = {
    1: "Tools/camera",
    2: "Vein (major)",
    3: "Artery (major)",
    4: "Nerve (major)",
    5: "Small intestine",
    6: "Colon/rectum",
    7: "Abdominal wall",
    8: "Diaphragm",
    9: "Omentum",
    10: "Aorta",
    11: "Vena cava",
    12: "Liver",
    13: "Cystic duct",
    14: "Gallbladder",
    15: "Hepatic vein",
    16: "Hepatic ligament",
    17: "Cystic plate",
    18: "Stomach",
    19: "Ductus choledochus",
    20: "Mesenterium",
    21: "Ductus hepaticus",
    22: "Spleen",
    23: "Uterus",
    24: "Ovary",
    25: "Oviduct",
    26: "Prostate",
    27: "Urethra",
    28: "Ligated plexus",
    29: "Seminal vesicles",
    # 30: "Catheter",
    # 31: "Bladder",
    # 32: "Kidney",
    # 33: "Lung",
    # 34: "Airway (bronchus/trachea)",
    # 35: "Esophagus",
    # 36: "Pericardium",
    # 37: "V azygos",
    # 38: "Thoracic duct",
    # 39: "Nerves",
}

# Remove non-anatomical classes (41, 42)
# del color_palette[41]
# del color_palette[42]


def process_mask_file(mask_file):
    """Process a single mask file using NumPy vectorized operations."""
    mask = Image.open(mask_file)
    if mask.mode != 'RGB':
        mask = mask.convert('RGB')
    mask_array = np.array(mask)

    pixel_counts = {class_id: np.sum(np.all(mask_array == color, axis=-1)) for class_id, color in color_palette.items()}
    classes_in_image = {class_id for class_id, count in pixel_counts.items() if count > 0}

    return pixel_counts, classes_in_image

def process_mask_wrapper(mask_file):
    """Wrapper function to process a mask file in parallel."""
    return process_mask_file(mask_file)

def count_class_occurrences(main_folder):
    """Count class occurrences in the dataset using multiprocessing."""
    class_pixel_counts = defaultdict(int)
    class_image_counts = defaultdict(int)
    class_clip_counts = defaultdict(int)
    class_video_counts = defaultdict(int)

    surgical_procedures = [surgical_procedure for surgical_procedure in os.listdir(main_folder)
                           if os.path.isdir(os.path.join(main_folder, surgical_procedure))]

    for surgical_procedure in tqdm.tqdm(surgical_procedures, desc="Processing procedures"):
        surgical_procedure_path = os.path.join(main_folder, surgical_procedure)
        video_folders = [video_folder for video_folder in os.listdir(surgical_procedure_path)
                         if os.path.isdir(os.path.join(surgical_procedure_path, video_folder))]

        for video_folder in tqdm.tqdm(video_folders, desc="Processing videos", leave=False):
            video_folder_path = os.path.join(surgical_procedure_path, video_folder)
            clip_folders = [clip_folder for clip_folder in os.listdir(video_folder_path)
                            if os.path.isdir(os.path.join(video_folder_path, clip_folder))]

            video_classes = set()
            for clip_folder in tqdm.tqdm(clip_folders, desc="Processing clips", leave=False):
                clip_folder_path = os.path.join(video_folder_path, clip_folder)
                masks_folder = os.path.join(clip_folder_path, "masks")

                if os.path.isdir(masks_folder):
                    mask_files = glob(os.path.join(masks_folder, "frame_*.png"))

                    # Use multiprocessing to process mask files
                    with multiprocessing.Pool() as pool:
                        results = list(pool.imap(process_mask_wrapper, mask_files))

                    clip_classes = set()
                    for pixel_counts, classes_in_image in results:
                        for class_id, count in pixel_counts.items():
                            class_pixel_counts[class_id] += count
                        for class_id in classes_in_image:
                            class_image_counts[class_id] += 1
                            clip_classes.add(class_id)

                    for class_id in clip_classes:
                        class_clip_counts[class_id] += 1
                        video_classes.add(class_id)

            for class_id in video_classes:
                class_video_counts[class_id] += 1

    return class_pixel_counts, class_image_counts, class_clip_counts, class_video_counts


def plot_class_occurrences(class_pixel_counts, class_image_counts, class_clip_counts, class_video_counts):
    """Plots occurrences per pixels, frames, clips, and videos."""
    data = {
        "Pixel Count": class_pixel_counts,
        "Frame Count": class_image_counts,
        "Clip Count": class_clip_counts,
        "Video Count": class_video_counts
    }

    for title, counts in data.items():
        plt.figure(figsize=(12, 6))
        class_ids = list(counts.keys())
        values = [counts[class_id] for class_id in class_ids]
        labels = [class_names[class_id] for class_id in class_ids]
        bars = plt.barh(labels, values, color='skyblue')
        plt.xlabel(title)
        plt.ylabel("Anatomical Structure")
        plt.title(f"Class Occurrences by {title}")

        for bar in bars:
            plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height() / 2,
                     str(bar.get_width()), va='center', ha='left', fontsize=10)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Basic statistics
    main_folder = "E:\SurgeSAM_processed"  # Replace with your dataset path
    total_surgical_procedures, total_videos, total_clips, total_annotated_frames = get_clip_and_frame_statistics(
        main_folder)

    print(f"Total number of surgical procedures: {total_surgical_procedures}")
    print(f"Total number of videos: {total_videos}")
    print(f"Total number of clips: {total_clips}")
    print(f"Total number of annotated frames: {total_annotated_frames}")

    clip_lengths = get_clip_lengths("E:\SurgeSAM_processed")
    plot_clip_durations(clip_lengths)


    # Per class statistics
    # main_folder = "E:\SurgeSAM_processed"  # Replace with your dataset path
    # class_pixel_counts, class_image_counts, class_clip_counts, class_video_counts = count_class_occurrences(main_folder)
    # plot_class_occurrences(class_pixel_counts, class_image_counts, class_clip_counts, class_video_counts)
