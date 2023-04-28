import torch
import torch.nn as nn


class PositionEncoding(nn.Module):
    def __init__(self, d_mod, max_seq_long):
        super().__init__()
        self.max_seq_long=max_seq_long
        self.d_mod=d_mod
    
    def create_encode(self):
        par_i= torch.arange(0, self.d_mod,2).float()
        denominator = torch.pow(10000,par_i/self.d_mod)
        position= torch.arange(self.max_seq_long.reshape(self.max_seq_long,1))
        par_PE= torch.sin(position/denominator)
        impar_PE= torch.cos(position/denominator)
        apilar= torch.stack([par_PE,impar_PE], dim=2)
        PE=torch.flatten(apilar,start_dim=1,end_dim=2)
        return PE