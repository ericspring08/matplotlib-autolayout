import matplotlib.pyplot as plt
from src.apply_functions import apply_flexDirection, apply_margin

def flexboxify(figure: plt.Figure, flexbox_config=None):
    if flexbox_config is None:
        return ValueError("Flexbox config is required") 

    flexDirection = "row"
    margin = 0
    # traverse the flexbox config
    for key, value in flexbox_config.items():
        # flexbox configuration 
        if key == "flex-direction":
            flexDirection = value
        elif key == "margin":
            margin = value

    figure = apply_flexDirection(figure, flexDirection) 
    figure = apply_margin(figure, margin)

    return figure