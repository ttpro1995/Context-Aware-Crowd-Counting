import torch.nn as nn
import torch

if __name__ == "__main__":
    x = torch.randn(1, 3, 224, 224)
    print(x.shape)  # torch.Size([1, 3, 224, 224])
    avg_module = nn.AdaptiveAvgPool2d(output_size=(4, 4))
    y = avg_module(x)
    print(y.shape)  # torch.Size([1, 3, 4, 4])
