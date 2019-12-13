import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F



def save_tensor_to_csv(x, fn):
    np.savetxt(fn, x.squeeze(0).squeeze(0).numpy().astype(int), fmt='%i', delimiter=",")

if __name__ == "__main__":
    # make grid of 12x12
    torch.manual_seed(113)
    x = torch.Tensor(1, 1, 12,12).random_(0, 99)
    print(x)
    np.savetxt("original_grid.csv", x.squeeze(0).squeeze(0).numpy().astype(int), fmt='%i', delimiter=",")

    # # pooling 1x1
    p1 = F.adaptive_avg_pool2d(x, 1)
    print(p1)
    save_tensor_to_csv(p1, "1x1pooling.csv")
    x1 = F.interpolate(input=p1, size=(12, 12), mode='bilinear')
    save_tensor_to_csv(x1, "1x1pooling_upsampling.csv")

    # pooling 2x2
    p2 = F.adaptive_avg_pool2d(x, 2)
    print(p2)
    save_tensor_to_csv(p2, "2x2pooling.csv")
    x2 = F.interpolate(input=p2, size=(12, 12), mode='bilinear')
    save_tensor_to_csv(x2, "2x2pooling_upsampling.csv")

    # pooling 3x3
    p3 = F.adaptive_avg_pool2d(x, 3)
    print(p3)
    save_tensor_to_csv(p3, "3x3pooling.csv")
    x3 = F.interpolate(input=p3, size=(12, 12), mode='bilinear')
    save_tensor_to_csv(x3, "3x3pooling_upsampling.csv")
    x3t = F.upsample(input=p3, size=(12, 12), mode='bilinear')
    save_tensor_to_csv(x3t, "3x3pooling_upsampling_old.csv")

    # pooling 6x6
    p4 = F.adaptive_avg_pool2d(x, 6)
    print(p4)
    save_tensor_to_csv(p4, "4x4pooling.csv")
    x4 = F.interpolate(input=p4, size=(12, 12), mode='bilinear')
    save_tensor_to_csv(x4, "4x4pooling_upsampling.csv")