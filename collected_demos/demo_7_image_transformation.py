from taipy.gui import Gui
import taipy.gui.builder as tp
import torch
from PIL import Image
from io import BytesIO

selector_input = ['version 1 (🔺 stylization, 🔻 robustness)', 'version 2 (🔺 robustness,🔻 stylization)']
selected = selector_input[0]
file_path = ""
result = ""

model2 = torch.hub.load(
    "AK391/animegan2-pytorch:main",
    "generator",
    pretrained=True,
    progress=False
)
model1 = torch.hub.load("AK391/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v1")
face2paint = torch.hub.load(
    'AK391/animegan2-pytorch:main', 'face2paint', 
    size=512,side_by_side=False
)

def inference(state):
    pil_image = Image.open(state.file_path)
    print(state.selected)
    if state.selected == selector_input[1]:
        out = face2paint(model2, pil_image)
    else:
        out = face2paint(model1, pil_image)
    with BytesIO() as buf:
        out.save(buf, 'jpeg')
        image_bytes = buf.getvalue()
        state.result = image_bytes

with tp.Page() as page:
    tp.text(value="AnimeGANv2")
    with tp.layout():
        with tp.part():
            tp.file_selector("{file_path}", label="Upload an image", extensions=".jpg,.jpeg,.png")
            tp.image("{file_path}", label="Uploaded image")
            tp.selector("{selected}", label="Version", lov="{selector_input}")
            tp.button("Submit", on_action="inference")
        with tp.part():
            tp.text("Image Transformation Result")
            tp.image("{result}", label="Result image")
            

Gui(page=page).run(run_browser=False)