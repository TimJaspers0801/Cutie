import numpy as np

# davis_palette = b'\x00\x00\x00\x80\x00\x00\x00\x80\x00\x80\x80\x00\x00\x00\x80\x80\x00\x80\x00\x80\x80\x80\x80\x80@\x00\x00\xc0\x00\x00@\x80\x00\xc0\x80\x00@\x00\x80\xc0\x00\x80@\x80\x80\xc0\x80\x80\x00@\x00\x80@\x00\x00\xc0\x00\x80\xc0\x00\x00@\x80\x80@\x80\x00\xc0\x80\x80\xc0\x80@@\x00\xc0@\x00@\xc0\x00\xc0\xc0\x00@@\x80\xc0@\x80@\xc0\x80\xc0\xc0\x80\x00\x00@\x80\x00@\x00\x80@\x80\x80@\x00\x00\xc0\x80\x00\xc0\x00\x80\xc0\x80\x80\xc0@\x00@\xc0\x00@@\x80@\xc0\x80@@\x00\xc0\xc0\x00\xc0@\x80\xc0\xc0\x80\xc0\x00@@\x80@@\x00\xc0@\x80\xc0@\x00@\xc0\x80@\xc0\x00\xc0\xc0\x80\xc0\xc0@@@\xc0@@@\xc0@\xc0\xc0@@@\xc0\xc0@\xc0@\xc0\xc0\xc0\xc0\xc0 \x00\x00\xa0\x00\x00 \x80\x00\xa0\x80\x00 \x00\x80\xa0\x00\x80 \x80\x80\xa0\x80\x80`\x00\x00\xe0\x00\x00`\x80\x00\xe0\x80\x00`\x00\x80\xe0\x00\x80`\x80\x80\xe0\x80\x80 @\x00\xa0@\x00 \xc0\x00\xa0\xc0\x00 @\x80\xa0@\x80 \xc0\x80\xa0\xc0\x80`@\x00\xe0@\x00`\xc0\x00\xe0\xc0\x00`@\x80\xe0@\x80`\xc0\x80\xe0\xc0\x80 \x00@\xa0\x00@ \x80@\xa0\x80@ \x00\xc0\xa0\x00\xc0 \x80\xc0\xa0\x80\xc0`\x00@\xe0\x00@`\x80@\xe0\x80@`\x00\xc0\xe0\x00\xc0`\x80\xc0\xe0\x80\xc0 @@\xa0@@ \xc0@\xa0\xc0@ @\xc0\xa0@\xc0 \xc0\xc0\xa0\xc0\xc0`@@\xe0@@`\xc0@\xe0\xc0@`@\xc0\xe0@\xc0`\xc0\xc0\xe0\xc0\xc0\x00 \x00\x80 \x00\x00\xa0\x00\x80\xa0\x00\x00 \x80\x80 \x80\x00\xa0\x80\x80\xa0\x80@ \x00\xc0 \x00@\xa0\x00\xc0\xa0\x00@ \x80\xc0 \x80@\xa0\x80\xc0\xa0\x80\x00`\x00\x80`\x00\x00\xe0\x00\x80\xe0\x00\x00`\x80\x80`\x80\x00\xe0\x80\x80\xe0\x80@`\x00\xc0`\x00@\xe0\x00\xc0\xe0\x00@`\x80\xc0`\x80@\xe0\x80\xc0\xe0\x80\x00 @\x80 @\x00\xa0@\x80\xa0@\x00 \xc0\x80 \xc0\x00\xa0\xc0\x80\xa0\xc0@ @\xc0 @@\xa0@\xc0\xa0@@ \xc0\xc0 \xc0@\xa0\xc0\xc0\xa0\xc0\x00`@\x80`@\x00\xe0@\x80\xe0@\x00`\xc0\x80`\xc0\x00\xe0\xc0\x80\xe0\xc0@`@\xc0`@@\xe0@\xc0\xe0@@`\xc0\xc0`\xc0@\xe0\xc0\xc0\xe0\xc0  \x00\xa0 \x00 \xa0\x00\xa0\xa0\x00  \x80\xa0 \x80 \xa0\x80\xa0\xa0\x80` \x00\xe0 \x00`\xa0\x00\xe0\xa0\x00` \x80\xe0 \x80`\xa0\x80\xe0\xa0\x80 `\x00\xa0`\x00 \xe0\x00\xa0\xe0\x00 `\x80\xa0`\x80 \xe0\x80\xa0\xe0\x80``\x00\xe0`\x00`\xe0\x00\xe0\xe0\x00``\x80\xe0`\x80`\xe0\x80\xe0\xe0\x80  @\xa0 @ \xa0@\xa0\xa0@  \xc0\xa0 \xc0 \xa0\xc0\xa0\xa0\xc0` @\xe0 @`\xa0@\xe0\xa0@` \xc0\xe0 \xc0`\xa0\xc0\xe0\xa0\xc0 `@\xa0`@ \xe0@\xa0\xe0@ `\xc0\xa0`\xc0 \xe0\xc0\xa0\xe0\xc0``@\xe0`@`\xe0@\xe0\xe0@``\xc0\xe0`\xc0`\xe0\xc0\xe0\xe0\xc0'
# davis_palette_np = np.frombuffer(davis_palette, dtype=np.uint8).reshape(-1, 3)

youtube_palette = b'\x00\x00\x00\xec_g\xf9\x91W\xfa\xc8c\x99\xc7\x94b\xb3\xb2f\x99\xcc\xc5\x94\xc5\xabyg\xff\xff\xffes~\x0b\x0b\x0b\x0c\x0c\x0c\r\r\r\x0e\x0e\x0e\x0f\x0f\x0f'
youtube_palette_np = np.frombuffer(youtube_palette, dtype=np.uint8).reshape(-1, 3)

color_palette = {
    # Abdomen IDs
    1: (255, 255, 255),  # Tools/camera - White
    2: (0, 0, 255),      # Vein (major) - Blue
    3: (255, 0, 0),      # Artery (major) - Red
    4: (255, 255, 0),  # Nerve (major) - Yellow
    5: (0, 255, 0),      # Small intestine - Green
    6: (0, 200, 100),    # Colon/rectum - Dark Green
    7: (200, 150, 100),  # Abdominal wall - Beige
    8: (255, 200, 100),  # Omentum - Light Orange
    9: (180, 0, 0),      # Aorta - Dark Red
    10: (0, 0, 180),      # Vena cava - Dark Blue
    11: (150, 100, 50),  # Liver - Brown
    12: (0, 255, 255),   # Cystic duct - Cyan
    13: (0, 200, 255),   # Gallbladder - Teal
    14: (0, 100, 255),   # Hepatic vein - Light Blue
    15: (255, 150, 50),  # Hepatic ligament - Orange
    16: (255, 220, 200), # Cystic plate - Light Pink
    17: (200, 0, 200),   # Spleen - Purple
    18: (255, 0, 150),   # Uterus - Pink
    19: (255, 100, 200), # Ovary - Light Pink
    20: (200, 100, 255), # Oviduct - Lavender
    21: (150, 0, 100),   # Prostate - Dark Purple
    22: (255, 200, 255), # Urethra - Light Pink
    23: (150, 100, 50),  # Ligated plexus - Brown
    24: (200, 0, 150),   # Seminal vesicles - Magenta
    25: (100, 100, 100), # Catheter - Gray
    26: (255, 150, 255), # Bladder - Light Purple
    27: (100, 200, 255), # Kidney - Light Blue

    # Thorax IDs
    28: (150, 200, 255), # Lung - Light Blue
    29: (0, 150, 255),   # Airway (bronchus/trachea) - Sky Blue
    30: (255, 100, 100), # Esophagus - Salmon
    31: (200, 200, 255), # Pericardium - Pale Blue
    32: (100, 100, 255), # V azygos - Blue
    33: (0, 255, 150),   # Thoracic duct - Green Cyan
    34: (255, 255, 100), # Nerves - Yellow

    # Non-anatomical structures
    35: (150, 150, 150),  # Firefly - Gray
    36: (50, 50, 50),    # Non anatomical structures - Dark Gray
    37: (0, 0, 0),      # Excluded frames - Black
}

custom_names = {
    1: "Tools/camera",
    2: "Vein (major)",
    3: "Artery (major)",
    4: "Nerve (major)",
    5: "Small intestine",
    6: "Colon/rectum",
    7: "Abdominal wall",
    8: "Omentum",
    9: "Aorta",
    10: "Vena cava",
    11: "Liver",
    12: "Cystic duct",
    13: "Gallbladder",
    14: "Hepatic vein",
    15: "Hepatic ligament",
    16: "Cystic plate",
    17: "Spleen",
    18: "Uterus",
    19: "Ovary",
    20: "Oviduct",
    21: "Prostate",
    22: "Urethra",
    23: "Ligated plexus",
    24: "Seminal vesicles",
    25: "Catheter",
    26: "Bladder",
    27: "Kidney",
    28: "Lung",
    29: "Airway (bronchus/trachea)",
    30: "Esophagus",
    31: "Pericardium",
    32: "V azygos",
    33: "Thoracic duct",
    34: "Nerves",
    35: "Firefly",
    36: "Non anatomical structures",
    37: "Excluded frames"
}

custom_palette_np = np.array([color_palette.get(i, (0, 0, 0)) for i in range(101)])

custom_palette = custom_palette_np.astype(np.uint8).tobytes()


