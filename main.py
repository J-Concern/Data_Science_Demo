import torch
import torch.nn as nn
import torch.optim as optim

#Network Architecture
class Net(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__(Net, self).__init__()
        self.fc1= nn.linear(input_size,hidden_size)
        self.relu = nn.Linear(hidden_size,num_classes)
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self,x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

#Network Instnatiation    
input_size = 0 # equal to resolution of image in linear form

hidden_size = 0

num_classes = 10

net = Net(input_size, hidden_size, num_classes)


# Define loss functiona nd optizimer
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(net.parameters(), lr=0.0001)

#network trainer

def train():
    num_epochs=5
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(data_loader):
            outputs = net(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 100 == 0:
                print("Epoch [{}], Step [{}], Loss: {:.4f}")
                    .format(epoch+1, num_epochs, i+1, len(data_loader), loss.item())