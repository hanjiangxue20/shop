from django.test import TestCase

# Create your tests here.


# 第一题：给函数传递一个正整数的列表alist和一个正整数T，假装它等于[1,3,6,4,2,7]，给出alist里所有相加等于T的元素的list，
# 每个数只用一次。比如T=7，列表里3+4=7，7=7，1+6=7。你的函数就要返回[[3,4],[7],[1,6]]。
# 之前见过类似的题目，很快就给出了解题思路，我用的回溯法，但是这个代码对我而言有点复杂了，
# 只能写出来整体的框架，递归调用的返回值想不明白。面试结束的时候，面试官说我三道题给出的算法都很优。


alist=[1,3,6,4,2,7,5,6,7,8,9,]
T=12

def fun(li=[],  T=T):
    blist=[]
    for i in range(len(li)):
        for j in range(len(li)):
            if (li[i] +li[j]==T) & (i<j):
                blist.append([li[i],li[j]])
    return blist


print(fun(alist,T=T))