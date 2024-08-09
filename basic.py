import matplotlib.pyplot as plt
import math
import random

def flexboxify(figure: plt.Figure, flexbox_config=None):
    if flexbox_config is None:
        return ValueError("Flexbox config is required") 

    flexDirection = "row"
    margin = 0
    # traverse the flexbox config
    for key, value in flexbox_config.items():
        if key == "configuration":
           # flexbox configuration 
           for k, v in value.items():
                if k == "flex-direction":
                   flexDirection = v
                elif k == "margin":
                    margin = v

    print(margin)

    if flexDirection == "row":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()
    
        # calculate the width of each plot
        width = total_width / len(figure.axes)
        height = total_height
        for i, ax in enumerate(figure.axes):
            # ax.set_position([i * width / total_width, 0, width / total_width, height / total_height])
            ax.set_position([i * width / total_width + margin, margin, width / total_width - margin, height / total_height - margin])
    elif flexDirection == "column":
        total_width = figure.get_figwidth()
        total_height = figure.get_figheight()
    
        # calculate the height of each plot
        width = total_width
        height = total_height / len(figure.axes)
        for i, ax in enumerate(figure.axes):
            # ax.set_position([0, i * height / total_height, width / total_width, height / total_height])
            ax.set_position([margin, i * height / total_height + margin, width / total_width - margin, height / total_height - margin])
    else:
        return ValueError("Flex direction must be either row or column")