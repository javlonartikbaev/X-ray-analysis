import torch
from torchvision import models, transforms
from PIL import Image


def analysis(img_path):
    model = models.resnet50(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, 2)
    checkpoint = torch.load("ai_model/mura_fracture_model_best.pth", map_location="cpu")
    state_dict = checkpoint["model_state_dict"]

    new_state_dict = {k.replace("backbone.", ""): v for k, v in state_dict.items()}
    model.load_state_dict(new_state_dict, strict=False)

    model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    image_path = img_path
    img = Image.open(image_path).convert("RGB")
    img = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)

    labels = ["Нормально", "Перелом"]
    return labels[predicted.item()]
