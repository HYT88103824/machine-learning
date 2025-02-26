import numpy as np
import matplotlib.pyplot as plt

# 活性化関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):  # 導関数
    return x * (1 - x)

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
        self.hidden_output = sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output)
        self.output = sigmoid(self.output_input)
        return self.output

    def backward(self, x, y, output, learning_rate):
        # MSEの勾配計算
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)

        # 重みを更新
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += x.T.dot(hidden_delta) * learning_rate

    def train(self, x, y, iterations, learning_rate):
        loss_history = []
        for i in range(iterations):
            output = self.forward(x)
            # MSE損失
            loss = np.mean((y - output) ** 2)
            loss_history.append(loss)
            self.backward(x, y, output, learning_rate)
        return loss_history

# 非線形不連続関数
def target_function(x):
    return np.where(x < 0, 0.5 + 0.5 * (x / np.pi), 0.5 + 0.5 * np.cos(x))

x_values = np.linspace(-np.pi, np.pi, 50)
y_values = target_function(x_values)

# バイアス
x_train = np.c_[x_values, np.ones(50)]  # x_valuesとバイアス結合
y_train = y_values.reshape(-1, 1)  # そのまま 0-1 にスケーリング済み

input_neurons = 2
hidden_neurons = 10
output_neurons = 1
iterations = 100000
learning_rate = 0.1

nn = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
loss_history = nn.train(x_train, y_train, iterations, learning_rate)

predictions = nn.forward(x_train)  # 出力は 0-1 スケーリング済み

# サブプロットで2つのグラフを表示
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# 元データと予測結果の比較
axs[0].plot(x_values, y_values, label='Target Function', color='blue')
axs[0].plot(x_values, predictions, label='Neural Network', linestyle='--', color='red')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title('Prediction vs Actual')
axs[0].legend()

# MSE損失の推移グラフ
axs[1].plot(loss_history, label='MSE Loss', color='green')
axs[1].set_xlabel('Epochs')
axs[1].set_ylabel('Loss')
axs[1].set_title('Loss over iterations (Log Scale)')
axs[1].set_yscale('log')  # 縦軸を対数スケールに設定
axs[1].legend()

plt.tight_layout()
plt.show()
