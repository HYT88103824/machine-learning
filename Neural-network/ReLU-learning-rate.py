import numpy as np
import matplotlib.pyplot as plt

# 活性化関数
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # ガウス分布に基づく乱数で初期化
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, x):
        self.hidden_input = np.dot(x, self.weights_input_hidden)
        self.hidden_output = relu(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output)
        self.output = relu(self.output_input)
        return self.output
    
    def backward(self, x, y, output, learning_rate):
        output_error = y - output
        output_delta = output_error * relu_derivative(output)
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * relu_derivative(self.hidden_output)
        
        # 重みを更新
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += x.T.dot(hidden_delta) * learning_rate

    def train(self, x, y, iterations, learning_rate):
        for i in range(iterations):
            output = self.forward(x)
            self.backward(x, y, output, learning_rate)

x_values = np.linspace(-np.pi, np.pi, 50)
y_values = np.sin(x_values)

# バイアス追加
x_train = np.c_[x_values, np.ones(50)]
y_train = ((y_values + 1) / 2).reshape(-1, 1)

input_neurons = 2
hidden_neurons = 10
output_neurons = 1
iterations = 100000

loss = []
min_error = float('inf')
best_learning_rate = 0
learning_rates = []

# 学習率を探索（0を除外）
for learning_rate in range(1, 100):
    current_rate = learning_rate / 10000
    nn = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
    nn.train(x_train, y_train, iterations, current_rate)
    
    predictions = 2 * nn.forward(x_train) - 1  # スケーリングを元に戻す
    error = np.mean((predictions - y_values) ** 2)  # 平均二乗誤差
    
    if error < min_error:
        min_error = error
        best_learning_rate = current_rate
    
    loss.append(error)
    learning_rates.append(current_rate)

# 最良の学習率を表示
print("Best learning rate:", best_learning_rate)

# グラフ描画
plt.plot(learning_rates, loss, label='Learning Rate vs Loss')
plt.xlabel('Learning Rate')
plt.ylabel('Loss')
plt.title('Learning Rate vs Loss')
plt.legend()
plt.show()
