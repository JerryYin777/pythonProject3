import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
from matplotlib import pyplot as plt
from IPython import display
import numpy as np
# 未初始化
# x=torch.empty(5,3)
# print(x)
# # 初始化
# x=torch.rand(5,3)
# print(x)
# # # long型全0/1
# x=torch.zeros/ones(5,3,dtype=torch.long)
# print(x)
# 生成数据集
num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = torch.randn(num_examples, num_inputs,
                       dtype=torch.float32)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()),
                       dtype=torch.float32)
print(features[0], labels[0])
def use_svg_display():
    # 用矢量图显示
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize
set_figsize()
plt.scatter(features[:, 1].numpy(), labels.numpy(), 1);
plt.show()




