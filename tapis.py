from PIL import Image, ImageDraw

VOWELS = "AEIOU"

def is_vowel(c):
    return c in VOWELS

def generate_tapis_png(top, side):
    cell = 60   # ⬅️ MAI MARE (era 40)
    cols = len(top)
    rows = len(side)

    width = cols * cell
    height = rows * cell

    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)

    # =========================
    # GRID NEGRU COMPLET
    # =========================

    grid_width = 1

    for x in range(cols + 1):
        X = min(x * cell, width - 1)
        d.line((X, 0, X, height - 1), fill="black", width=grid_width)

    for y in range(rows + 1):
        Y = min(y * cell, height - 1)
        d.line((0, Y, width - 1, Y), fill="black", width=grid_width)

    # =========================
    # LINII COLORATE
    # =========================

    color_width = 2

    # verticale (coloane)
    for x, c in enumerate(top):
        start = is_vowel(c)
        for y in range(rows):
            draw = (y % 2 == 0) if start else (y % 2 != 0)
            if draw:
                d.line(
                    (x * cell, y * cell, x * cell, (y + 1) * cell),
                    fill="red" if start else "blue",  # ⬅️ CULORI NOI
                    width=color_width
                )

    # orizontale (rânduri)
    for y, c in enumerate(side):
        start = is_vowel(c)
        for x in range(cols):
            rx = cols - 1 - x
            draw = (rx % 2 == 0) if start else (rx % 2 != 0)
            if draw:
                d.line(
                    (x * cell, y * cell, (x + 1) * cell, y * cell),
                    fill="red" if start else "blue",  # ⬅️ CULORI NOI
                    width=color_width
                )

    return img



