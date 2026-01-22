import io
import numpy as np
import matplotlib
matplotlib.use("Agg")  # OBLIGATORIU pe server
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.colors import ListedColormap

VOWELS = "AEIOU"

def is_vowel(letter):
    return letter in VOWELS


def generate_tapis_png(top_letters, side_letters):
    COLS = len(top_letters)
    ROWS = len(side_letters)

    fig, ax = plt.subplots(figsize=(COLS, ROWS))
    ax.imshow(
        np.ones((ROWS, COLS)),
        cmap=ListedColormap(["white"]),
        extent=[0, COLS, ROWS, 0],
    )

    THIN = 0.6
    THICK = 2.0

    # grid negru complet (interior + margini)
    for x in range(COLS + 1):
        ax.plot([x, x], [0, ROWS], color="black", linewidth=THIN)
    for y in range(ROWS + 1):
        ax.plot([0, COLS], [y, y], color="black", linewidth=THIN)

    # linii verticale colorate
    for c in range(COLS):
        vowel = is_vowel(top_letters[c])
        color = "red" if vowel else "blue"
        for r in range(0, ROWS, 2):
            ax.plot([c, c], [r, r + 1], color=color, linewidth=THICK)

    # linii orizontale colorate
    for r in range(ROWS):
        vowel = is_vowel(side_letters[r])
        color = "red" if vowel else "blue"
        for c in range(0, COLS, 2):
            ax.plot([c, c + 1], [r, r], color=color, linewidth=THICK)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, COLS)
    ax.set_ylim(ROWS, 0)
    ax.set_aspect("equal")

    buffer = io.BytesIO()
    FigureCanvas(fig).print_png(buffer)
    plt.close(fig)

    buffer.seek(0)
    return buffer.getvalue()





