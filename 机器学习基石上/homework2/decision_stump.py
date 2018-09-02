import math
import numpy as np

'''
Question 17
Generate a data set of size 20 by the procedure above and run the one-dimensional decision stump algorithm
on the data set. Record E_{in} and compute E_{out} with the formula above. Repeat the experiment (including 
data generation, running the decision stump algorithm, and computing E_{in} and E_{out}) 5,000 times. What 
is the average E_{in} ? Please choose the closest option.
'''

# 生成数据函数
def generateData():
    x=np.random.uniform(-1, 1, 20)  # 在[-1, 1)之间均匀分布抽取随机数样本
    y=np.sign(x)
    y[y==0] = 1  # y[y==0] = 1 得到误差小于 y[y==0] = 0, -1
    prop = np.random.uniform(0, 1, 20)  # 在[0,1)之间均匀分布抽取20个随机数样本, 返回array
    y[prop >= 0.8] *= -1  # 生成20%的噪音
    return x, y


# 单维度决策树桩算法
def decision_stump(X, Y):
    theta = np.sort(X)  # 从小到大排序
    num = len(theta)  # 长度
    Xtemp = np.tile(X, (num, 1))  # num行X
    ttemp = np.tile(np.reshape(theta, (num, 1)), (1, num))
    ypred = np.sign(Xtemp - ttemp)
    ypred[ypred == 0] = 1
    # 统计误差的个数
    err = np.sum(ypred != Y, axis = 1)    # 矩阵的每一行相加
    # err = array([10, 9, 8, 7, 8,  7,  6,  5,  4,  5,  6,  7,  8,  9,  8,  7,  8,  7,  8,  9])])

    # 判断最小误差hypothesis
    # 如果np.min(err) <= num - np.max(err), 则判断s为1, 错误率为 np.min(err)/num
    # 如果np.min(err) > num-np.max(err), 则判断s为-1, 错误率为 (num-np.max(err))/num
    if np.min(err) <= num - np.max(err):
        return 1, theta[np.argmin(err)], np.min(err)/num    # np.argmin 返回沿axis最小值的索引值
    else:
        return -1, theta[np.argmax(err)], (num-np.max(err))/num


# Q17和Q18
def main():
    totalin = 0; totalout = 0
    for _ in range(5000):
        X,Y = generateData()
        theta = np.sort(X)  # 默认从小到大排列
        s, theta, errin = decision_stump(X, Y)
        errout = 0.5 + 0.3*s*(math.fabs(theta)-1)  # math.fabs 返回数字的绝对值
        totalin += errin
        totalout += errout
    print("训练集平均误差: ", totalin/5000)
    print("测试集平均误差: ", totalout/5000)

# 输出: 0.17186, 0.260232

if __name__=="__main__":
    main()


