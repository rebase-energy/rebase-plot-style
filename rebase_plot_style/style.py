import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import style as mplstyle
from cycler import cycler
import importlib.resources
from IPython.core.magic import register_line_magic
import warnings

BRAND_COLORS = ["#2cbc99", "#457cf6"]

def set_plot_style(nbins=5):
    """
    Apply Rebase matplotlib style and limit number of x-axis ticks.
    """
    with importlib.resources.path("rebase_plot_style", "rebase.mplstyle") as path:
        mplstyle.use(str(path))

    plt.rcParams["axes.prop_cycle"] = cycler(color=BRAND_COLORS)

    try:
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=nbins))
    except Exception as e:
        warnings.warn(f"Could not set x-tick locator: {e}")

@register_line_magic
def rebase_style(line):
    """
    IPython magic: %rebase_style [nbins]
    """
    try:
        nbins = int(line.strip()) if line.strip() else 5
    except ValueError:
        nbins = 5
    set_plot_style(nbins)
    print(f"✅ Rebase style applied with max {nbins} x-ticks.")
