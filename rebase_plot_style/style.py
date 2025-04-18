import matplotlib.pyplot as plt
from matplotlib import style as mplstyle
from cycler import cycler
import importlib.resources
from IPython.core.magic import register_line_magic

# Rebase brand color cycle
BRAND_COLORS = ["#2cbc99", "#457cf6"]

def set_plot_style():
    """
    Apply Rebase matplotlib style and color cycle.
    """
    # Load .mplstyle from package resources
    with importlib.resources.path("rebase_plot_style", "rebase.mplstyle") as path:
        mplstyle.use(str(path))

    # Set global color cycle
    plt.rcParams["axes.prop_cycle"] = cycler(color=BRAND_COLORS)

@register_line_magic
def rebase_style(line):
    """
    IPython magic: %rebase_style
    Applies Rebase plot style (ignores any arguments).
    """
    set_plot_style()
    print("✅ Rebase style applied.")
