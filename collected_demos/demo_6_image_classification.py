from taipy.gui import Gui
import taipy.gui.builder as tp
import torch
import requests
from torchvision import transforms
from PIL import Image

file_path = ""
result = {"name": [], "value": []}

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(state):
    pil_image = Image.open(state.file_path)
    image = transforms.ToTensor()(pil_image).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(image)[0], dim=0)
        confidences = {labels[i]: f"{float(prediction[i]) * 100:.4f}%" for i in range(1000)}
    state.result = { "name": confidences.keys(), "value": confidences.values() }

with tp.layout() as main_layout:
    with tp.part():
        tp.file_selector("{file_path}", label="Upload an image", extensions=".jpg,.jpeg,.png")
        tp.image("{file_path}", label="Uploaded image")
        tp.button("Submit", on_action="predict")
    with tp.part():
        tp.text("Image Classification Result")
        tp.table("{result}")

Gui(page=tp.Page(main_layout)).run(run_browser=False)