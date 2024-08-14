import matplotlib.pyplot as plt
from matplotlib_autolayout.utils.apply_functions import apply_direction_count, apply_margin
from matplotlib_autolayout.utils.configuration import AutoLayoutConfig

def autolayout(figure: plt.Figure, configuration=None):
    if configuration is None:
        return ValueError("Flexbox config is required")

    configuration = AutoLayoutConfig(configuration).get_dict_config_dict()
    print(configuration)

    figure = apply_direction_count(
        figure, configuration["direction"], configuration["count"])
    figure = apply_margin(figure, configuration["margin"])

    return figure
