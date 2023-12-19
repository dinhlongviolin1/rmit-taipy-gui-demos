from taipy.gui import Gui
from PIL import Image
import numpy as np
from io import BytesIO

image_file = ""
rotation = d_r = d_g = d_b = 0
image_bytes = None
previous_rotation = 0
original_image = None
image_data = None

page = """
# Image processing

<|{image_file}|file_selector|label=Select an image file|extensions=.png,.jpg,.jpeg|drop_message=Drop your image|>

<|part|render={image_bytes is None}|
No image
|>
<|part|render={image_bytes}|
<|layout|id=image-part|columns=1 3
<|
Rotation <|{rotation}|slider|min=-30|max=30|labels=0:none|>

<|layout|id=rgb-columns|columns=1 1 1
<|{d_r}|slider|min=-100|max=100|orientation=v|>

<|{d_g}|slider|min=-100|max=100|orientation=v|>

<|{d_b}|slider|min=-100|max=100|orientation=v|>

&nbsp;&nbsp;&nbsp;&nbsp;R

&nbsp;&nbsp;&nbsp;&nbsp;G

&nbsp;&nbsp;&nbsp;&nbsp;B

<|
|>

<|Reset RGB|button|on_action=reset_rgb|>

<|
|>
|>

<|{image_bytes}|file_download|label=Save processed image|don't bypass_preview|>

|>

<|{image_bytes}|image|width=500px|height=500px|>
|>
|>
<|part|render=false|
<|{original_image}|>
|>
"""


def impact_image(state):
    if state.original_image is None:
        return None
    if state.image_data is None or (state.rotation != state.previous_rotation):
        state.previous_rotation = state.rotation
        state.image_data = np.array(
            state.original_image.rotate(-state.rotation, resample=Image.BILINEAR)
            if state.rotation
            else state.original_image
        )
    if state.d_r or state.d_g or state.d_b:
        data = state.image_data.copy()
        for comp, d in enumerate((state.d_r, state.d_g, state.d_b)):
            band = state.image_data[:, :, comp].copy()
            if d < 0:

                def decrease(v):
                    new_v = v * (100 + d) / 100
                    return 0 if new_v < 0 else int(new_v)

                f = np.vectorize(decrease)
            elif d > 0:

                def increase(v):
                    new_v = v * (1 + (d / 100))
                    return 255 if new_v > 255 else int(new_v)

                f = np.vectorize(increase)
            else:
                f = None
            if f:
                data[:, :, comp] = f(band)
            else:
                data[:, :, comp] = band
    else:
        data = state.image_data
    buffered = BytesIO()
    image = Image.fromarray(data)
    image.save(buffered, format="JPEG")
    return buffered.getvalue()


def on_change(state, name, value):
    if name == "image_file":
        try:
            state.original_image = Image.open(value).convert("RGB")
            state.image_data = None
            state.image_bytes = impact_image(state)
        except Exception:
            state.original_image = None
            state.image_data = None
            state.image_bytes = None
            state.show_notification("error", "Not a valid image file")
    elif name == "rotation" or name == "d_r" or name == "d_g" or name == "d_b":
        state.image_bytes = impact_image(state)


def reset_rgb(state):
    state.d_r = state.d_g = state.d_b = 0


Gui(page).run()
