import matplotlib.pyplot as plt

def apply_flexDirection(figure: plt.Figure, flexDirection: str):
    if flexDirection == "row":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()
    
        # calculate the width of each plot
        width = total_width / len(figure.axes)
        height = total_height
        for i, ax in enumerate(figure.axes):
            ax.set_position([i * width / total_width, 0, width / total_width, height / total_height])
    elif flexDirection == "column":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()
    
        # calculate the height of each plot
        width = total_width
        height = total_height / len(figure.axes)
        for i, ax in enumerate(figure.axes):
            ax.set_position([0, i * height / total_height, width / total_width, height / total_height])
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
        width = width - 2 * margin
        height = height - 2 * margin
        ax.set_position([x, y, width, height])

    return figure