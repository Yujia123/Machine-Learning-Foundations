
import numpy as np
from decision_stump import decision_stump

trainfile=r"C:\Users\User\Documents\MOOC\Coursera\机器学习基石上\homework2\hw2_train.dat"
testfile=r"C:\Users\User\Documents\MOOC\Coursera\机器学习基石上\homework2\hw2_test.dat"

def loadfile(path):
    f = open(path,'r')
    lines = f.readlines()
    X = []
    Y = []
    for line in lines:
        items = line.split()  # 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        x = [1] + [float(i) for i in items[:-1]]  # x[0] = 1, items[-1] 对应 items[0] - 倒数第二个
        X.append(x)
        Y.append(int(items[-1]))  # 获取最后一个数
    return np.array(X), np.array(Y)  # 需要用到array, 不然返回错误  # numpy.array中的数据类型必须相同, 而list可以不同


# 多维度决策树桩算法
def decision_stump_multi(X, Y):
    _, col = X.shape  # 10维
    err = np.zeros((col, )); s = np.zeros((col, )); theta = np.zeros((col, ))
    # Q19. a) for each dimension i=1,2,...,d, find the best decision stump h_{s,i,theta} using the one-dimensional
    # decision stump algorithm that you have just implemented
    # b) return the "best of best" decision stump in terms of E_{in}. If there is a tie, please randomly
    # choose among the lowerst-E_{in} ones
    for i in range(col):
        s[i], theta[i], err[i] = decision_stump(X[:, i], Y[:])
    pos = np.argmin(err)
    return pos, s[pos], theta[pos], err[pos]


# Q19和Q20
def main():
    X, Y = loadfile(trainfile)
    Xtest, Ytest = loadfile(testfile)
    pos, s, theta, err = decision_stump_multi(X, Y)
    print("训练集误差: ", err)

    ypred = s*np.sign(Xtest[:,pos]-theta)  # pos对应所在的列数，即维度
    ypred[ypred == 0] = 1
    errout = np.sum(ypred != Ytest)/len(ypred)  # 计算平均误差
    print("测试集误差: ", errout)

# 输出: 0.25, 0.36


if __name__=="__main__":
    main()
