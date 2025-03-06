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
    4: (255, 255, 0),    # Nerve (major) - Yellow
    5: (0, 255, 0),      # Small intestine - Green
    6: (0, 200, 100),    # Colon/rectum - Dark Green
    7: (200, 150, 100),  # Abdominal wall - Beige
    8: (250, 150, 100),  # Diaphragm - light Beige
    9: (255, 200, 100),  # Omentum - Light Orange
    10: (180, 0, 0),      # Aorta - Dark Red
    11: (0, 0, 180),     # Vena cava - Dark Blue
    12: (150, 100, 50),  # Liver - Brown
    13: (0, 255, 255),   # Cystic duct - Cyan
    14: (0, 200, 255),   # Gallbladder - Teal
    15: (0, 100, 255),   # Hepatic vein - Light Blue
    16: (255, 150, 50),  # Hepatic ligament - Orange
    17: (255, 220, 200), # Cystic plate - Light Pink
    18: (200, 100, 200), # Stomach - Light Purple
    19: (144, 238, 144), # Ductus choledochus - Light Green
    20: (247, 255, 0),               # Mesenterium
    21: (200, 0, 200),   # Spleen - Purple
    22: (255, 0, 150),   # Uterus - Pink
    23: (255, 100, 200), # Ovary - Light Pink
    24: (200, 100, 255), # Oviduct - Lavender
    25: (150, 0, 100),   # Prostate - Dark Purple
    26: (255, 200, 255), # Urethra - Light Pink
    27: (150, 100, 50),  # Ligated plexus - Brown
    28: (200, 0, 150),   # Seminal vesicles - Magenta
    29: (100, 100, 100), # Catheter - Gray
    30: (255, 150, 255), # Bladder - Light Purple
    31: (100, 200, 255), # Kidney - Light Blue

    # Thorax IDs
    32: (150, 200, 255), # Lung - Light Blue
    33: (0, 150, 255),   # Airway (bronchus/trachea) - Sky Blue
    34: (255, 100, 100), # Esophagus - Salmon
    35: (200, 200, 255), # Pericardium - Pale Blue
    36: (100, 100, 255), # V azygos - Blue
    37: (0, 255, 150),   # Thoracic duct - Green Cyan
    38: (255, 255, 100), # Nerves - Yellow

    # Non-anatomical structures
    39: (150, 150, 150),  # Firefly - Gray
    40: (50, 50, 50),     # Non anatomical structures - Dark Gray
    41: (0, 0, 0),       # Excluded frames - Black
}

custom_names = {
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
    21: "Spleen",
    22: "Uterus",
    23: "Ovary",
    24: "Oviduct",
    25: "Prostate",
    26: "Urethra",
    27: "Ligated plexus",
    28: "Seminal vesicles",
    29: "Catheter",
    30: "Bladder",
    31: "Kidney",
    32: "Lung",
    33: "Airway (bronchus/trachea)",
    34: "Esophagus",
    35: "Pericardium",
    36: "V azygos",
    37: "Thoracic duct",
    38: "Nerves",
    39: "Firefly",
    40: "Non anatomical structures",
    41: "Excluded frames"
}

custom_palette_np = np.array([color_palette.get(i, (0, 0, 0)) for i in range(101)])

custom_palette = custom_palette_np.astype(np.uint8).tobytes()


