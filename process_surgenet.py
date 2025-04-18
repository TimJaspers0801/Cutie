import os
import cv2
import numpy as np
from tqdm import tqdm


def process_videos(input_root, output_root):
    # Gather all video files
    video_files = []
    for root, dirs, files in os.walk(input_root):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add other formats as needed
                video_files.append(os.path.join(root, file))

    # Display the number of videos found
    total_videos = len(video_files)
    if total_videos == 0:
        print("No videos found in the dataset.")
        return

    print(f"Found {total_videos} videos. Processing...")

    # Process each video with a progress bar
    for video_path in tqdm(video_files, desc="Processing videos"):
        video_name = os.path.splitext(os.path.basename(video_path))[0]

        # Create the new folder structure in the output directory
        relative_path = os.path.relpath(os.path.dirname(video_path), input_root)
        output_video_folder = os.path.join(output_root, relative_path, video_name)
        images_folder = os.path.join(output_video_folder, 'images')
        masks_folder = os.path.join(output_video_folder, 'masks')

        # Check if processing is already done
        if os.path.exists(images_folder) and any(os.scandir(images_folder)):
            print(f"Skipping {video_name}, already processed.")
            continue

        os.makedirs(images_folder, exist_ok=True)
        os.makedirs(masks_folder, exist_ok=True)

        # Process the video
        save_frames(video_path, images_folder, fps=15)

        print(f"Processed {video_name} successfully.")


def save_frames(video_path, output_folder, fps=5):
    # Capture the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video {video_path}")
        return

    # Get the video frame rate
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(video_fps / fps)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:06d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Processed {saved_count} frames from {video_path} into {output_folder}")

def analyze_video_properties(input_root):
    fps_values = []
    resolutions = []
    video_files = []

    for root, dirs, files in os.walk(input_root):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                video_files.append(os.path.join(root, file))

    total_videos = len(video_files)
    if total_videos == 0:
        print("No videos found to analyze.")
        return

    print(f"Analyzing properties for {total_videos} videos...")

    for video_path in tqdm(video_files, desc="Analyzing Videos"):
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            # Analyze FPS
            video_fps = cap.get(cv2.CAP_PROP_FPS)
            fps_values.append(video_fps)

            # Analyze resolution
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            resolutions.append((width, height))
        cap.release()

    if fps_values:
        max_fps = max(fps_values)
        min_fps = min(fps_values)
        median_fps = np.median(fps_values)
        print(f"Maximum FPS: {max_fps}")
        print(f"Minimum FPS: {min_fps}")
        print(f"Median FPS: {median_fps}")
    else:
        print("No valid FPS data found.")

    if resolutions:
        unique_resolutions = set(resolutions)
        resolution_counts = {res: resolutions.count(res) for res in unique_resolutions}
        print("Resolutions and their counts:")
        for res, count in resolution_counts.items():
            print(f"Resolution {res[0]}x{res[1]}: {count} video(s)")
    else:
        print("No valid resolution data found.")

# Specify the root directory of your dataset
input_root = r"E:\SurgeNet_videos_selected\gastrojejunostomy"
output_root = "E:\SurgeSAM\gastrojejunostomy"
os.makedirs(output_root, exist_ok=True)
process_videos(input_root, output_root)

# analyze_video_properties(input_root)
