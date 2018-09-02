# 计算 06_handout.pdf  13  22/37 页  bounding function B(4,3), N=4, k=3
# B(4,3)=11

# 备注: 
# bounding function B(N,k):
# maximum possible m_{H}(N) when break point = k  # 参考 06_handout.pdf  6  15/37

from numpy import array
import itertools

# k = 3
# 列举出 k=3 的所有排列

p3=[]

num = [0, 1]

# 定义p3列表
for i in num:
    for j in num:
        for k in num:
            p3.append([i,j,k])  # len=8

# p3=array(p3)         


# px 输入为一个n行3列的矩阵
# 如果3个元素shatter, 返回True
def check_x(px, p3):
    bl = [False for i in range(len(p3))]

    for i in range(len(px)):
        for j in range(len(p3)):
            if px[i] == p3[j]:
                bl[j] = True   

    # 如果bl全为True, 则代表3个元素shatter, 否则, 没有shatter
    for i in bl:
        if i == False:
            return False  # bl中有元素为False, 3个元素没有shatter, 返回False
    return True  # bl全为True, 3个元素shatter, 返回True
        
        
# p为一个n行4列矩阵
# 检查一个n行4列的矩阵中是否任意3列（个）都没有shatter
def check(p, p3):

    # # 元素 x1, x2, x3
    # p_1=p[:,(0,1,2)]

    # # 元素 x1, x2, x4
    # p_2=p[:,(0,1,3)]

    # # 元素 x2, x3, x4
    # p_3=p[:,(1,2,3)]


    p_1=[[x[0],x[1],x[2]] for x in p]  # 提取矩阵p的0,1,2列
    p_2=[[x[0],x[1],x[3]] for x in p]  # 提取0,1,3列
    p_3=[[x[0],x[2],x[3]] for x in p]  # 提取0,2,3列
    p_4=[[x[1],x[2],x[3]] for x in p]  # 提取1,2,3列

    c1=check_x(p_1,p3)
    c2=check_x(p_2,p3)
    c3=check_x(p_3,p3)
    c4=check_x(p_4,p3)

    # 如果任意三个都没有shatter, 则返回True, 否则返回False
    if c1==False and c2==False and c3==False and c4==False:
        return True
    else:
        return False


p4 = []
for i in num:
    for j in num:
        for k in num:
            for g in num:
                p4.append([i,j,k,g])  # len(p4)=16


# 生成矩阵(p4的元素排列组合)
# num为行数
def generate(num, p4):
    
    # 组合, 从p4中选出行数组合
    list1 = list(itertools.combinations([i for i in range(len(p4))], num))
    matric = []
    for i in list1:
        matric = [p4[j] for j in i]  # matric = p4 里对应的行数  # matric为一个num行4列的矩阵 
        if check(matric, p3) == True:
            print("no shatter, ok!")
            return matric
    return False  # 如果没有匹配的, 则返回False
    




for i in range(len(p4),1,-1):  # 倒序
    
    matric = generate(i, p4)
    if matric!=False:
        print("最大行数为: ",i)
        print(array(p3),"\n\n")
        print(array(matric))
        break



# matric = generate(12, p4)

# if matric!=False:
#     print(array(p3),"\n")
#     print(array(matric),"\n")
#     check(matric,p3)

# else:
#     print("""------------------
#     No match
# ------------------""")






        












