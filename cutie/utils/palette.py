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
    4: (0, 255, 0),      # Small intestine - Green
    5: (0, 200, 100),    # Colon/rectum - Dark Green
    6: (200, 150, 100),  # Abdominal wall - Beige
    7: (255, 200, 100),  # Omentum - Light Orange
    8: (180, 0, 0),      # Aorta - Dark Red
    9: (0, 0, 180),      # Vena cava - Dark Blue
    10: (150, 100, 50),  # Liver - Brown
    11: (0, 255, 255),   # Cystic duct - Cyan
    12: (0, 200, 255),   # Gallbladder - Teal
    13: (0, 100, 255),   # Hepatic vein - Light Blue
    14: (255, 150, 50),  # Hepatic ligament - Orange
    15: (200, 150, 0),   # Hepatocystic triangle - Mustard
    16: (255, 220, 200), # Cystic plate - Light Pink
    17: (255, 255, 0),   # Nerve (major) - Yellow
    18: (200, 0, 200),   # Spleen - Purple
    19: (255, 0, 150),   # Uterus - Pink
    20: (255, 100, 200), # Ovary - Light Pink
    21: (200, 100, 255), # Oviduct - Lavender
    22: (150, 0, 100),   # Prostate - Dark Purple
    23: (255, 200, 255), # Urethra - Light Pink
    24: (150, 100, 50),  # Ligated plexus - Brown
    25: (200, 0, 150),   # Seminal vesicles - Magenta
    26: (100, 100, 100), # Catheter - Gray
    27: (255, 150, 255), # Bladder - Light Purple
    28: (100, 200, 255), # Kidney - Light Blue

    # Thorax IDs
    29: (150, 200, 255), # Lung - Light Blue
    30: (0, 150, 255),   # Airway (bronchus/trachea) - Sky Blue
    31: (255, 100, 100), # Esophagus - Salmon
    32: (200, 200, 255), # Pericardium - Pale Blue
    33: (100, 100, 255), # V azygos - Blue
    34: (0, 255, 150),   # Thoracic duct - Green Cyan
    35: (255, 255, 100), # Nerves - Yellow

    # Non-anatomical structures
    99: (50, 50, 50),    # Non anatomical structures - Dark Gray
    100: (0, 0, 0),      # Excluded frames - Black
}

custom_names = {
    1: "Tools/camera",
    2: "Vein (major)",
    3: "Artery (major)",
    4: "Small intestine",
    5: "Colon/rectum",
    6: "Abdominal wall",
    7: "Omentum",
    8: "Aorta",
    9: "Vena cava",
    10: "Liver",
    11: "Cystic duct",
    12: "Gallbladder",
    13: "Hepatic vein",
    14: "Hepatic ligament",
    15: "Hepatocystic triangle",
    16: "Cystic plate",
    17: "Nerve (major)",
    18: "Spleen",
    19: "Uterus",
    20: "Ovary",
    21: "Oviduct",
    22: "Prostate",
    23: "Urethra",
    24: "Ligated plexus",
    25: "Seminal vesicles",
    26: "Catheter",
    27: "Bladder",
    28: "Kidney",
    29: "Lung",
    30: "Airway (bronchus/trachea)",
    31: "Esophagus",
    32: "Pericardium",
    33: "V azygos",
    34: "Thoracic duct",
    35: "Nerves",
    99: "Non anatomical structures",
    100: "Excluded frames"
}

custom_palette_np = np.array([color_palette.get(i, (0, 0, 0)) for i in range(101)])

custom_palette = custom_palette_np.astype(np.uint8).tobytes()


