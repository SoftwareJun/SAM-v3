import torch
import torch.nn as nn
import torch.nn.functional as F

"""layer1 = nn.Linear(5, 2)
input = torch.randn(3,5)
print(input)
output1 = layer1(input)
print(output1.shape)


layer2 = nn.Linear(2, 1)
output2 = layer2(output1)
print(output2.shape)

output2 = F.relu(output2)

print(output2)"""

"""input = torch.randn(1,3,32,32)
print(input.shape)
layer1 = nn.Conv2d(3, 8 ,3, 1, 1)
output = layer1(input)
print(output.shape)
layer2 = nn.Conv2d(8, 16, 3, 1, 1)
output = layer2(output)
print(output.shape)"""
class LambdaLayer(nn.Module) :

    def __init__(self, lambdaa) :
        super().__init__()
        self.lambdaa = lambdaa

    def forward(self, x) :
        return self.lambdaa(x)

class Block(nn.Module) :
    
    def __init__(self, in_channels, out_channels) :
        super().__init__()
        self.convlayer1 = nn.Conv2d(in_channels, out_channels ,3, 1, 1) 
        self.bnlayer1 = nn.BatchNorm2d(out_channels)
        self.convlayer2 = nn.Conv2d(out_channels, 2*out_channels, 3, 1, 1)
        self.bnlayer2 = nn.BatchNorm2d(2*out_channels)
        self.shortcut = LambdaLayer(lambda x : F.pad(x, (0,0,0,0, out_channels-in_channels//2, out_channels-in_channels//2)))
    def forward(self, x) :
        out = F.relu(self.bnlayer1(self.convlayer1(x)))
        out = self.bnlayer2(self.convlayer2(out))
        out += self.shortcut(x)
        out = F.relu(out)
        return out



class MyModel(nn.Module) :
    
    def __init__(self, in_channels, out_channels) :
        super().__init__()
        self.layer1 = Block(in_channels, out_channels)
        self.layer2 = Block(2*out_channels, 4*out_channels)
        self.layer3 = Block(8*out_channels, 16*out_channels)
    def forward(self, x) :
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        return out
 

myModel = MyModel(4, 8)
input = torch.randn(1,4,32,32)
print(myModel(input).shape)

