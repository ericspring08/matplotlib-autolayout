import matplotlib.pyplot as plt
from matplotlib_autolayout.apply_functions import apply_direction_count, apply_margin


def autolayout(figure: plt.Figure, configuration=None):
    if configuration is None:
        return ValueError("Flexbox config is required")

    figure = apply_direction_count(
        figure, configuration["direction"], configuration["count"])
    figure = apply_margin(figure, configuration["margin"])

    return figure
