import matplotlib.pyplot as plt
from cycler import cycler
from IPython.core.magic import register_line_magic

# Rebase brand colors
BRAND_COLORS = ["#2cbc99", "#457cf6"]

def set_plot_style():
    """
    Apply full Rebase matplotlib style in Python.
    """
    plt.rcParams.update({
        "figure.figsize": (10, 6),
        "axes.titlesize": 18,
        "axes.labelsize": 16,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "legend.fontsize": 14,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#444444",
        "axes.grid": True,
        "grid.color": "#dddddd",
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "xtick.color": "#888888",
        "axes.prop_cycle": cycler(color=BRAND_COLORS),
    })

@register_line_magic
def rebase_style(line):
    """
    IPython magic: %rebase_style
    """
    set_plot_style()
    print("✅ Rebase plot style applied.")
