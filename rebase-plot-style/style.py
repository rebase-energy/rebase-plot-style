import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import style as mplstyle
from cycler import cycler
import importlib.resources

from IPython.core.magic import register_line_magic
import warnings

# Rebase brand colors
BRAND_COLORS = ["#2cbc99", "#457cf6"]

def set_plot_style(nbins=5):
    """
    Apply Rebase matplotlib style and limit number of x-axis ticks.
    
    Parameters:
    -----------
    nbins : int
        Maximum number of ticks to display on the x-axis.
    """
    # Load .mplstyle file from package
    with importlib.resources.path("rebase_plot_style", "rebase.mplstyle") as style_path:
        mplstyle.use(str(style_path))

    # Apply custom color cycle globally
    plt.rcParams["axes.prop_cycle"] = cycler(color=BRAND_COLORS)

    # Optionally set x-axis tick limit on current axes
    try:
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=nbins))
    except Exception as e:
        warnings.warn(f"Could not set x-tick locator: {e}")

# Register as IPython magic
@register_line_magic
def rebase_style(line):
    """
    Magic command: %rebase_style [nbins]
    Applies the Rebase plotting style and sets optional x-tick limit.
    """
    try:
        nbins = int(line.strip()) if line.strip() else 5
    except ValueError:
        nbins = 5
    set_plot_style(nbins=nbins)
    print(f"✅ Rebase style applied with max {nbins} x-ticks.")
