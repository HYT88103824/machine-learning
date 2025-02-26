import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.hidden_layer = nn.Linear(input_size, hidden_size)
        self.output_layer = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        hidden_output = self.sigmoid(self.hidden_layer(x))
        output = self.sigmoid(self.output_layer(hidden_output))
        return output

x_values = np.linspace(-np.pi, np.pi, 50)
y_values = np.sin(x_values)

# データの前処理
x_train = torch.tensor(np.c_[x_values, np.ones(50)], dtype=torch.float32)  # x_valuesとバイアス結合
y_train = torch.tensor(((y_values + 2) / 4).reshape(-1, 1), dtype=torch.float32)  # 0-1にスケーリング

input_neurons = 2
hidden_neurons = 10
output_neurons = 1
iterations = 100000
initial_learning_rate = 0.1

# 学習スケジューリングなし
model_no_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_no_scheduler = optim.SGD(model_no_scheduler.parameters(), lr=initial_learning_rate)
criterion = nn.MSELoss()
loss_no_scheduler = []

for epoch in range(iterations):
    optimizer_no_scheduler.zero_grad()
    output = model_no_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_no_scheduler.append(loss.item())
    loss.backward()
    optimizer_no_scheduler.step()

# ステップ型減少
model_step_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_step_scheduler = optim.SGD(model_step_scheduler.parameters(), lr=initial_learning_rate)
scheduler_step = lr_scheduler.StepLR(optimizer_step_scheduler, step_size=10000, gamma=0.8)
loss_step_scheduler = []

for epoch in range(iterations):
    optimizer_step_scheduler.zero_grad()
    output = model_step_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_step_scheduler.append(loss.item())
    loss.backward()
    optimizer_step_scheduler.step()
    scheduler_step.step()

# 減衰型
model_exp_decay = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_exp_decay = optim.SGD(model_exp_decay.parameters(), lr=initial_learning_rate)
scheduler_exp_decay = lr_scheduler.ExponentialLR(optimizer_exp_decay, gamma=0.9999)
loss_exp_decay = []

for epoch in range(iterations):
    optimizer_exp_decay.zero_grad()
    output = model_exp_decay(x_train)
    loss = criterion(output, y_train)
    loss_exp_decay.append(loss.item())
    loss.backward()
    optimizer_exp_decay.step()
    scheduler_exp_decay.step()

# 余弦退化型
model_cosine_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_cosine_scheduler = optim.SGD(model_cosine_scheduler.parameters(), lr=initial_learning_rate)
scheduler_cosine = lr_scheduler.CosineAnnealingLR(optimizer_cosine_scheduler, T_max=iterations)
loss_cosine_scheduler = []

for epoch in range(iterations):
    optimizer_cosine_scheduler.zero_grad()
    output = model_cosine_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_cosine_scheduler.append(loss.item())
    loss.backward()
    optimizer_cosine_scheduler.step()
    scheduler_cosine.step()

# 多項式減衰型
model_poly_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_poly_scheduler = optim.SGD(model_poly_scheduler.parameters(), lr=initial_learning_rate)
scheduler_poly = lr_scheduler.PolynomialLR(optimizer_poly_scheduler, total_iters=iterations, power=2)
loss_poly_scheduler = []

for epoch in range(iterations):
    optimizer_poly_scheduler.zero_grad()
    output = model_poly_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_poly_scheduler.append(loss.item())
    loss.backward()
    optimizer_poly_scheduler.step()
    scheduler_poly.step()

# Cyclical Learning Rate
model_cyclic_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_cyclic_scheduler = optim.SGD(model_cyclic_scheduler.parameters(), lr=initial_learning_rate)
scheduler_cyclic = lr_scheduler.CyclicLR(optimizer_cyclic_scheduler, base_lr=0.01, max_lr=0.1, step_size_up=5000, mode='triangular')
loss_cyclic_scheduler = []

for epoch in range(iterations):
    optimizer_cyclic_scheduler.zero_grad()
    output = model_cyclic_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_cyclic_scheduler.append(loss.item())
    loss.backward()
    optimizer_cyclic_scheduler.step()
    scheduler_cyclic.step()

# OneCycleLR
model_one_cycle_scheduler = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
optimizer_one_cycle_scheduler = optim.SGD(model_one_cycle_scheduler.parameters(), lr=initial_learning_rate)
scheduler_one_cycle = lr_scheduler.OneCycleLR(optimizer_one_cycle_scheduler, max_lr=0.1, total_steps=iterations)
loss_one_cycle_scheduler = []

for epoch in range(iterations):
    optimizer_one_cycle_scheduler.zero_grad()
    output = model_one_cycle_scheduler(x_train)
    loss = criterion(output, y_train)
    loss_one_cycle_scheduler.append(loss.item())
    loss.backward()
    optimizer_one_cycle_scheduler.step()
    scheduler_one_cycle.step()

# 損失グラフの比較
plt.figure(figsize=(12, 8))
plt.plot(loss_no_scheduler, label='No Scheduler')
plt.plot(loss_step_scheduler, label='Step Decay Scheduler')
plt.plot(loss_exp_decay, label='Exponential Decay Scheduler')
plt.plot(loss_cosine_scheduler, label='Cosine Annealing Scheduler')
plt.plot(loss_poly_scheduler, label='Polynomial Decay Scheduler',linestyle=':')
plt.plot(loss_cyclic_scheduler, label='CyclicLR',linestyle='--')
plt.plot(loss_one_cycle_scheduler, label='OneCycleLR',linestyle='-.')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.yscale('log')
plt.title('Loss Comparison with Learning Rate Schedulers (PyTorch)')
plt.legend()
plt.show()