import random

#快排
def kuaipai(l):
    if l==[]:
        return []
    else:
        #找基准
        k=l[0]
        left=kuaipai([i for i in l[1:] if i<k])
        right=kuaipai([j for j in l[1:] if j>=k])
    return left+[k]+right


#归并排序
def guibing(l):
    if len(l)<=1:
        return l
    left=guibing(l[:(len(l))//2])   #左边数组
    right=guibing(l[(len(l))//2:])  #右边数组
    return hebing(left,right)
def hebing(l1,l2):
    l1_index=l2_index=0
    r=[]
    while l1_index<len(l1) and l2_index<len(l2):
        if l1[l1_index]<=l2[l2_index]:
            r.append(l1[l1_index])
            l1_index+=1
        else:
            r.append(l2[l2_index])
            l2_index+=1
    return r+l1[l1_index:]+l2[l2_index:]

l=[1,3,2,5,6,9,8,4,7]

# #冒泡排序
# for i in range(1,len(l)):
#     for j in range(len(l)-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#
# # 选择排序
# for i in range(len(l)-1):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


if __name__ == '__main__':
    l=list(range(11))
    random.shuffle(l)
    print(l)
    print(kuaipai(l))
    print(guibing(l))
