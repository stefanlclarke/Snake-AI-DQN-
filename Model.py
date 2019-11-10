import numpy as np
import torch
import torch.nn as nn

hidden_layer_size = 20

class actor(nn.Module):
    def __init__(self, in_size, hidden_layer_size, out_size):
        super(actor, self).__init__()
        self.fc1 = nn.Linear(in_size, hidden_layer_size)
        self.fc2 = nn.Linear(hidden_layer_size, hidden_layer_size)
        self.fc3 = nn.Linear(hidden_layer_size, hidden_layer_size)
        self.fc4 = nn.Linear(hidden_layer_size, out_size)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        l1 = self.relu(self.fc1(x.float()))
        l2 = self.relu(self.fc2(l1))
        l3 = self.relu(self.fc3(l2))
        l4 = self.fc4(l3)
        return l4
        
def get_network_input(player, apple):
    proximity = player.getproximity()
    x = torch.cat([torch.from_numpy(player.pos).double(), torch.from_numpy(apple.pos).double(), 
                   torch.from_numpy(player.dir).double(), torch.tensor(proximity).double()])
    return x
