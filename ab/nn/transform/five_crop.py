import torch
import torchvision.transforms as transforms

def transform(norm):
    return transforms.Compose([
    transforms.FiveCrop(size=34),
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize(*norm)
])
