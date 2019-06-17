'''
二叉树设计思路
class Node:
    属性:item,左子树,右子树
class Tree:
    属性:根节点
    方法:添加节点方法
    遍历树的方法
'''


# 定义节点
class Node(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

# 定义树
class Tree(object):
    def __init__(self):
        self.root=None      #根节点初始为None
    def add(self,item):
        node=Node(item)
        # 1 判断根节点是否存在   不存在  添加
        if not self.root:
            self.root=node
            return
        # 2 存在   将根节点添加到待访问队列
        temp=[self.root]
        # 6 重复3-5步
        while 1:
            # 3 从待访问队列中取出一个节点
            cur_node=temp.pop(0)
            # 4 判断其左右子树是否为空  为空 添加
            if not cur_node.left:
                cur_node.left=node
                return
            if not cur_node.right:
                cur_node.right=node
                return
            # 5 不为空 将左右子树添加到待访问队列
            temp.append(cur_node.left)
            temp.append(cur_node.right)

    #先序遍历   先访问根节点 再访问左子树  右子树    深度优先
    def xuanxu(self,node):
        if not node:
            return []
        #访问左子树
        left=self.xuanxu(node.left)
        #访问右子树
        right=self.xuanxu(node.right)
        return [node.item]+left+right
    #中序遍历   先访问左子树 再访问根节点 右节点
    def zhongxu(self,node):
        if not node:
            return []
        left=self.zhongxu(node.left)
        right=self.zhongxu(node.right)
        return left+[node.item]+right
    #后续遍历  先访问左子树，右子树 根节点
    def houxu(self,node):
        if not node:
            return []
        left=self.houxu(node.left)
        right=self.houxu(node.right)
        return left+right+[node.item]

    #广度优先
    def guangdu(self,node):
        if not node:
            return []
        temp=[self.root]
        result=[]
        while temp:
            cur_node=temp.pop(0)
            result.append(cur_node)
            if cur_node.left:
                temp.append(cur_node.left)
            if cur_node.right:
                temp.append(cur_node.right)
        return result


if __name__ == '__main__':
    t=Tree()
    for i in range(1,16):
        t.add(i)
    print(t.xuanxu(t.root))
    print(t.zhongxu(t.root))
    print(t.houxu(t.root))
    p=t.guangdu(t.root)
    for j in p:
        print(j.item,end=' ')

