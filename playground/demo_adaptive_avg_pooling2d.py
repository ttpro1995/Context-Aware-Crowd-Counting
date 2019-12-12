import torch
import numpy as np



def save_tensor_to_csv(x, fn):
    np.savetxt(fn, x.numpy().astype(int), fmt='%i', delimiter=",")

if __name__ == "__main__":
    torch.manual_seed(113)
    x = torch.LongTensor(5,5).random_(0, 10)
    print(x)
    np.savetxt("save.csv", x.numpy().astype(int), fmt='%i', delimiter=",")