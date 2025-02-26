import numpy as np
import matplotlib.pyplot as plt

# 活性化関数
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):  # 導関数
    return np.where(x > 0, 1, 0)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size) * np.sqrt(2 / self.input_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))

        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size) * np.sqrt(2 / self.hidden_size)
        self.bias_output = np.zeros((1, self.output_size))

    def forward(self, x):
        self.hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = relu(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = relu(self.output_input)
        return self.output

    def backward(self, x, y, output, learning_rate):
        # MSEの勾配計算
        output_error = y - output
        output_delta = output_error * relu_derivative(self.output_input)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * relu_derivative(self.hidden_input)

        # 重みとバイアスを更新
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

        self.weights_input_hidden += x.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, x, y, iterations, learning_rate):
        loss_history = []
        for i in range(iterations):
            output = self.forward(x)
            # MSE損失
            loss = np.mean((y - output) ** 2)
            loss_history.append(loss)
            self.backward(x, y, output, learning_rate)
        return loss_history

# データ準備
x_values = np.linspace(-np.pi, np.pi, 50).reshape(-1, 1)
y_values = np.sin(x_values)

# バイアスを追加
x_train = np.c_[x_values, np.ones(50)]  # x_valuesとバイアス結合
y_train = ((y_values + 1) / 2).reshape(-1, 1)  # 0-1にスケーリング

# ハイパーパラメータ
input_neurons = 2
hidden_neurons = 10
output_neurons = 1
iterations = 100000
learning_rate = 0.001

# モデル構築と学習
nn = NeuralNetwork(input_neurons, hidden_neurons, output_neurons)
loss_history = nn.train(x_train, y_train, iterations, learning_rate)

# 予測
predictions = 2 * nn.forward(x_train) - 1  # スケーリングを元に戻す

# サブプロットで2つのグラフを横並びで表示
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# 元データと予測結果の比較
axs[0].plot(x_values, y_values, label='sin(x)')
axs[0].plot(x_values, predictions, label='Neural Network', linestyle='--')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title('Prediction vs Actual')
axs[0].legend()

# MSE損失の推移グラフ
axs[1].plot(loss_history, label='MSE Loss')
axs[1].set_xlabel('Iterations')
axs[1].set_ylabel('Loss')
axs[1].set_title('Loss over Iterations')
axs[1].set_yscale('log')  # 縦軸を対数スケールに設定
axs[1].legend()

plt.tight_layout()
plt.show()
