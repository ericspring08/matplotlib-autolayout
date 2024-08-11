import matplotlib.pyplot as plt
import math


def apply_direction_count(figure: plt.Figure, direction: str, count: int):
    if direction == "row":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()

        # count is the number in each column for row direction
        columns = math.ceil(len(figure.axes) / count)

        # calculate the width of each plot
        plot_height = total_height / count
        plot_width = total_width / columns

        for i, ax in enumerate(figure.axes):
            x = (i // count) * plot_width
            y = total_height - ((i % count) * plot_height)

            ax.set_position([x, y, plot_width, plot_height])

    elif direction == "column":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()

        # count is the number in each row for column direction
        rows = math.ceil(len(figure.axes) / count)

        # calculate the height of each plot
        plot_height = total_height / rows
        plot_width = total_width / count

        for i, ax in enumerate(figure.axes):
            x = (i % count) * plot_width
            y = total_height - ((i // count) * plot_height)

            ax.set_position([x, y, plot_width, plot_height])
    else:
        return ValueError("Flex direction must be either row or column")

    return figure


def apply_margin(figure: plt.Figure, margin: int):
    for ax in figure.axes:
        # get the position of the plot
        position = ax.get_position()
        x, y, width, height = position.x0, position.y0, position.width, position.height
        # calculate the new position
        x = x + margin
        y = y + margin
        width = width - margin
        height = height - margin
        ax.set_position([x, y, width, height])

    return figure
