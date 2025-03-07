import numpy as np
import matplotlib.pyplot as plt

# 活性化関数
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):  # 導関数
    return 1 - np.tanh(x)**2

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # ガウス分布に基づく乱数で初期化
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size) #(2,10)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size) #(10,1)

    def forward(self, x):
        
        self.hidden_input = np.dot(x, self.weights_input_hidden) #行列積の計算
        self.hidden_output = tanh(self.hidden_input)

        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output)
        self.output = tanh(self.output_input)     
        
        return self.output
    
    def backward(self, x, y, output, learning_rate):
        output_error = y - output
        output_delta = output_error*tanh_derivative(output)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * tanh_derivative(self.hidden_output)
        
        #重みを更新
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate #(18.11)
        self.weights_input_hidden += x.T.dot(hidden_delta) * learning_rate #xの転置との内積

    def train(self, x, y, iterations, learning_rate):
        for i in range(iterations):
            output = self.forward(x)
            self.backward(x, y, output, learning_rate)

x_values = np.linspace(-np.pi, np.pi, 50)
y_values = np.sin(x_values) #訓練データ

#バイアス
x_train = np.c_[x_values, np.ones(50)] #x_valuesと50個の1配列を結合
y_train = ((y_values+1)/2).reshape(-1, 1)
#縦1列にして0-1にスケーリング
#シグモイド関数では負の領域が表現できないため

input_neurons = 2  # one for x, one for bias
hidden_neurons = 10
output_neurons = 1
iterations = 100000
loss = []
min_error = float('inf')

#クラスインスタンス生成
for learning_rate in range(0,100):
   nn = NeuralNetwork(input_neurons, hidden_neurons, output_neurons) #2,10,1
   nn.train(x_train, y_train, iterations, learning_rate/1000)
   
   predictions = 2*nn.forward(x_train)-1
   
   error = (predictions - y_values)**2
   if min_error > np.mean(error):
       min_error = np.mean(error)
       best_learning_rate = learning_rate/1000
   loss.append(np.mean(error))
   
learning_rate = np.linspace(0,0.1,100)
#スケーリングを元に戻す
print(best_learning_rate)

plt.plot(learning_rate, loss, label='learning-rate')
plt.xlabel('learning rate')
plt.ylabel('loss')
plt.legend()
plt.show()
