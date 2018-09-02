'''
Each line of the data set contains one (xn,yn) with xn ∈ R^4. The first 
4 numbers of the line contains the components of xn orderly, the last number 
is yn.

Please initialize your algorithm with w=0 and take sign(0) as -1. Please always
remember to add x0=1 to each xn.

Question 15
Implement a version of PLA by visiting examples in the naive cycle using the order
of examples in the data set. Run the algorithm on the data set. What is the number 
of updates before the algorithm halts ?

Question 16
Implement a version of PLA by visiting examples in fixed, pre-determined random cycles
throughout the algorithm. Run the algorithm on the data set. Please repeat your experiment
for 2000 times, each with a different random seed. What is the average number of updates
before the algorithm halts ?

Question 17
Implement a version of PLA by visiting examples in fixed, pre-determined random cycles
throughout the algorithm, while changing the update rule to be

                w_{t+1} = w_{t} + alpha * y_{n(t)} * x_{n(t)}

with alpha=0.5. Note that your PLA in the previous Question corresponds to alpha=1. Please 
repeat your experiment for 2000 times, each with a different random seed. What is the average 
number of updates before the algorithm halts ?
'''


import random
from numpy import zeros, array, inner, mean  # inner - Inner product of two arrays 返回两个向量的内积

filepath=r"C:\Users\User\Documents\MOOC\Coursera\机器学习基石上\homework1\hw1_15_train.dat"

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
        x = [1] + [float(i) for i in items[:-1]]  # x[0] = 1, items[-1] 对应 items[0] - 倒数第二个
        X.append(x)
        Y.append(int(items[-1]))  # 获取最后一个数
    return array(X), array(Y)  # 需要用到array, 不然返回错误  # numpy.array中的数据类型必须相同, 而list可以不同


def train(X, Y, rand=False, alpha=1):  # 预定义参数尽量写在右边
    n = len(Y)  # 400
    d = len(X[0])  # 4
    W = zeros(d)  # [0,0,0,0]

    # 顺序
    idx = range(n)
    # 乱序
    if rand:                         
        idx = random.sample(idx, n)  # 从[0, 400)中随机获取400个元素，作为一个list返回
    t = 0  # 记录到达收敛需要的循环更新的次数               # 每次都不同
    k = 0
    flag = True
    while True:
        if k == n:
            if flag:
                break
            k = 0
            flag = True
        
        i = idx[k]
        # print("i ",i, " ,k ",k, " ,sign(inner(X[i], W)) " ,signfun(inner(X[i], W))," ,Y[i] " ,Y[i])
        if signfun(inner(X[i], W)) != Y[i]:
            flag = False
            t += 1
            W = W + alpha * Y[i] * X[i]  # # 参照02_handout.pdf P9 11/37 页
        k += 1

    return t  # 返回总的更新次数


def naive_cycle():
    X, Y = loadfile(filepath)
    t=train(X,Y)
    print(t)

def predefined_random(n, alpha=1):
    X, Y = loadfile(filepath)
    count = []
    for i in range(n):
        print("第",i,"次迭代")
        t = train(X,Y,True,alpha)  # 默认参数, 从左往右传
        count.append(t)
    print(mean(count))
    

def main():
    # Questions 15          # Output : 45
    # naive_cycle()
    # Question 16           # Output : 40.415
    # predefined_random(2000)
    # Question 17           # Output : 39.797
    predefined_random(2000, 0.5)  # 默认参数，从左往右传

if __name__ == '__main__':
    main()


