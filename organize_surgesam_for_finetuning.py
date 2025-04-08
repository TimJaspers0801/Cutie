import os
import shutil

# # Define the root directory where the dataset is currently located
# root_dir = "E:\SurgeSAM_processed"
# # Define the new root directory where you want to reorganize the data
# new_root_dir = "E:\SurgeSAM_finetuning"
#
# # Create 'images' and 'masks' directories in the new structure
# os.makedirs(os.path.join(new_root_dir, 'images'), exist_ok=True)
# os.makedirs(os.path.join(new_root_dir, 'masks'), exist_ok=True)
#
#
# # reorginize for cutie
#
# # Loop through all the surgical-procedure folders
# for surgical_procedure in os.listdir(root_dir):
#     surgical_procedure_path = os.path.join(root_dir, surgical_procedure)
#     if os.path.isdir(surgical_procedure_path):
#
#         # Loop through all the videos in the current surgical-procedure folder
#         for video in os.listdir(surgical_procedure_path):
#             video_path = os.path.join(surgical_procedure_path, video)
#             if os.path.isdir(video_path):
#
#                 # Loop through all the clips in the current video folder
#                 for clip in os.listdir(video_path):
#                     clip_path = os.path.join(video_path, clip)
#                     if os.path.isdir(clip_path):
#
#                         # Define new folder name (videoname_clipname)
#                         new_folder_name = f"{video}_{clip}"
#
#                         # Create new subfolders in images and masks
#                         new_images_dir = os.path.join(new_root_dir, 'images', new_folder_name)
#                         new_masks_dir = os.path.join(new_root_dir, 'masks', new_folder_name)
#                         os.makedirs(new_images_dir, exist_ok=True)
#                         os.makedirs(new_masks_dir, exist_ok=True)
#
#                         # Move images and masks from the clip folder to the new directories
#                         images_dir = os.path.join(clip_path, 'images')
#                         masks_dir = os.path.join(clip_path, 'machine_masks')
#
#                         # Move all image files
#                         if os.path.exists(images_dir):
#                             for img_file in os.listdir(images_dir):
#                                 shutil.copy(os.path.join(images_dir, img_file), os.path.join(new_images_dir, img_file))
#
#                         # Move all mask files
#                         if os.path.exists(masks_dir):
#                             for mask_file in os.listdir(masks_dir):
#                                 shutil.copy(os.path.join(masks_dir, mask_file), os.path.join(new_masks_dir, mask_file))
#
# print("Reorganization completed!")


# # reorganize for ritm
#
# # Define the root directory where the dataset is currently located
# root_dir = r"E:\SurgeSAM_processed"
# # Define the new root directory where you want to reorganize the data
# new_root_dir = r"E:\SurgeSAM_finetuning_ritm"
#
# # Create 'images' and 'masks' directories in the new structure
# images_flat_dir = os.path.join(new_root_dir, 'images')
# masks_flat_dir = os.path.join(new_root_dir, 'masks')
# os.makedirs(images_flat_dir, exist_ok=True)
# os.makedirs(masks_flat_dir, exist_ok=True)
#
# # Loop through all the surgical-procedure folders
# for surgical_procedure in os.listdir(root_dir):
#     surgical_procedure_path = os.path.join(root_dir, surgical_procedure)
#     if os.path.isdir(surgical_procedure_path):
#
#         # Loop through all the videos in the current surgical-procedure folder
#         for video in os.listdir(surgical_procedure_path):
#             video_path = os.path.join(surgical_procedure_path, video)
#             if os.path.isdir(video_path):
#
#                 # Loop through all the clips in the current video folder
#                 for clip in os.listdir(video_path):
#                     clip_path = os.path.join(video_path, clip)
#                     if os.path.isdir(clip_path):
#
#                         # Create prefix for filenames
#                         prefix = f"{video}_{clip}_"
#
#                         # Move and rename image files
#                         images_dir = os.path.join(clip_path, 'images')
#                         if os.path.exists(images_dir):
#                             for img_file in os.listdir(images_dir):
#                                 src_path = os.path.join(images_dir, img_file)
#                                 dst_filename = prefix + img_file
#                                 dst_path = os.path.join(images_flat_dir, dst_filename)
#                                 shutil.copy(src_path, dst_path)
#
#                         # Move and rename mask files
#                         masks_dir = os.path.join(clip_path, 'machine_masks')
#                         if os.path.exists(masks_dir):
#                             for mask_file in os.listdir(masks_dir):
#                                 src_path = os.path.join(masks_dir, mask_file)
#                                 dst_filename = prefix + mask_file
#                                 dst_path = os.path.join(masks_flat_dir, dst_filename)
#                                 shutil.copy(src_path, dst_path)
#
# print("Flattened reorganization completed!")



#### Train val split
import random
from collections import defaultdict

# Set paths
base_dir = r"E:\SurgeSAM_finetuning_ritm"
images_dir = os.path.join(base_dir, 'images')
masks_dir = os.path.join(base_dir, 'masks')
pickle_dir = os.path.join(base_dir, 'masks_pickle')

# Set up output dirs
train_img_dir = os.path.join(base_dir, 'train', 'images')
train_mask_dir = os.path.join(base_dir, 'train', 'masks')
train_pickle_dir = os.path.join(base_dir, 'train', 'pickles')
val_img_dir = os.path.join(base_dir, 'val', 'images')
val_mask_dir = os.path.join(base_dir, 'val', 'masks')
val_pickle_dir = os.path.join(base_dir, 'val', 'pickles')


# Create directories
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_mask_dir, exist_ok=True)
os.makedirs(train_pickle_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_mask_dir, exist_ok=True)
os.makedirs(val_pickle_dir, exist_ok=True)

# Group files by video prefix (video_clip)
video_groups = defaultdict(list)
for filename in os.listdir(images_dir):
    if filename.endswith(('.jpg', '.png')):  # add more extensions if needed
        prefix = "_".join(filename.split("_")[:2])  # video_clip
        video_groups[prefix].append(filename)

# Shuffle and split
all_videos = list(video_groups.keys())
random.shuffle(all_videos)
split_idx = int(0.9 * len(all_videos))
train_videos = set(all_videos[:split_idx])
val_videos = set(all_videos[split_idx:])


# Move files to their respective folders
def move_files(video_set, img_dest, mask_dest, pickle_dest):
    for video in video_set:
        for filename in video_groups[video]:
            img_src = os.path.join(images_dir, filename)
            mask_src = os.path.join(masks_dir, filename.replace('.jpg', '.png'))
            pickle_src = os.path.join(pickle_dir, filename.replace('.jpg', '.pickle'))

            img_dst = os.path.join(img_dest, filename)
            mask_dst = os.path.join(mask_dest, filename.replace('.jpg', '.png'))
            pickle_dst = os.path.join(pickle_dest, filename.replace('.jpg', '.pickle'))

            shutil.copy(img_src, img_dst)
            if os.path.exists(mask_src):
                shutil.copy(mask_src, mask_dst)
            if os.path.exists(pickle_src):
                shutil.copy(pickle_src, pickle_dst)

# Execute moving
move_files(train_videos, train_img_dir, train_mask_dir, train_pickle_dir)
move_files(val_videos, val_img_dir, val_mask_dir, val_pickle_dir)

print(f"Dataset split complete. {len(train_videos)} videos in training, {len(val_videos)} videos in validation.")
