'''
Next, we play with the pocket algorithm. Modify your PLA in Question 16 to visit 
examples purely randomly, and the add the "pocket" steps to the algorithm. 

Question 18
The sets are of the same format as the previous one. Run the pocket algorithm with
a total of 50 updates on D, and verify the performance of W_{POCKET} using the test
set. Please repeat your experiment for 2000 times, each with a different random seed
Waht is the average error rate on the test set ?

Question 19
Modify your algorithm in Question 18 to return W_50 (THE PLA vector after 50 updates) instead 
of W_{POCKET} after 50 updates.

Run the modified algorithm on D, and verify the performance using the test set.

Please repeat your experiment for 2000 times, each with a different random seed. What is the 
average error rate on your test set ?

Question 20
Modify your algorithm in Question 18 to run for 100 updates instead of 50, and verify the performance
of W_{POCKET} using the test set. Please repeat your experiment for 2000 times, each with a different
random seed. What is the average error rate on the test set ?

'''

import random

from numpy import (array,  # inner - Inner product of two arrays 返回两个向量的内积
                   inner, mean, zeros)

trainfile=r"C:\Users\User\Documents\MOOC\Coursera\机器学习基石上\homework1\hw1_18_train.dat"
testfile=r"C:\Users\User\Documents\MOOC\Coursera\机器学习基石上\homework1\hw1_18_test.dat"

# take sign(0) as -1
def signfun(x):
    if x <= 0:
        return -1
    return 1

def loadfile(path):
    f = open(path,'r')
    lines = f.readlines()
    X = []
    Y = []
    for line in lines:
        items = line.split()  # 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        # Add x_0=1 to each x_n
        x = [1] + [float(i) for i in items[:-1]]  # x[0] = 1, items[-1] 对应 items[0] - 倒数第二个
        X.append(tuple(x))
        Y.append(int(items[-1]))  # 获取最后一个数
    return array(X), array(Y)  # 需要用到array, 不然返回错误  # numpy.array 中的数据类型必须相同, 而list可以不同


def test(X,Y,W):
    n = len(Y)
    ne = sum([1 for i in range(n) if signfun(inner(X[i], W)) != Y[i]])  # 统计不相同的次数
    err = ne/n  # 错误率
    return err

# Run the pocket algorithm with a total of 50 updates on D, and verify the performance of 
# W_{POCKET} using the test set.
def train(X, Y, updates=50, pocket=True):
    n = len(Y)
    d = len(X[0])
    W = zeros(d)  # 返回一个 1*5 的数组
    Wg = W

    err = test(X,Y,Wg)  # 错误率

    for i in range(updates):
        idx = random.sample(range(n), n)   # 乱序
        for i in idx:
            if signfun(inner(X[i], W)) != Y[i]:
                W = W + Y[i] * X[i]  # 更新W系数
                e = test(X, Y, W)  # 获取新的W系数的错误率
                if e < err:  # 如果 e < err, 则更新err, Wg
                    err = e
                    Wg = W
                break
        
    if pocket:
        return Wg
    return W


def main():
    X, Y = loadfile(trainfile)
    TX, TY= loadfile(testfile)
    err = []
    n =2000  # repeat 2000 times
    for i in range(n):

        print("第",i,"次迭代")

        # Question 18          # Output : 0.133233
        # Run the pocket algorithm with a total of 50 updates on D, and verify the performance of
        # W_{POCKET} using the test set.
        # W = train(X,Y)

        # Question 19          # Output : 0.35534
        # Modify your algorithm in Question 18 to return W_50 (THE PLA vector after 50 updates) instead 
        # of W_{POCKET} after 50 updates
        # W = train(X, Y, pocket=False)

        # Question 20          # Output : 0.116229
        # Modify your algorithm in Question 18 to run for 100 updates instead of 50, and verify the performance
        # of W_{POCKET} using the test set. Please repeat your experiment for 2000 times, each with a different
        # random seed.
        W = train(X, Y, 100)

        etest = test(TX, TY, W)
        err.append(etest)

    print(mean(err))



if __name__ == "__main__":
    main()
