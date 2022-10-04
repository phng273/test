class BSTNode:
    global sum
    global count
    sum = 0
    count = 0
    def __init__(self, e):
        self.key = e
        self.left = None
        self.right = None
        
#1: insert        
    def insert(self, ele):
        if ele == self.key:
            return
        elif ele < self.key:
            if self.left is None:
                self.left = BSTNode(ele)
            else:
                self.left.insert(ele)
        else:
            if self.right is None:
                self.right = BSTNode(ele)
            else:
                self.right.insert(ele)
          
#2: preorder          
    def preOrder(self):
        print(self.key, end = ' ')
        for child in [self.left, self.right]:
            if child:
                child.preOrder()
#3: inorder      
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.key, end = ' ')
        if self.right:
            self.right.inOrder()
        
#4: min        
    def find_min(self):
        if self.left is None:
            return self.key
        else:
            return self.left.find_min()
 
#5: max 
    def find_max(self):
        if self.right is None:
            return self.key
        else:
            return self.right.find_max()
        
       
#6: delete       
    def delete(self, val):
        if val < self.key:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.key:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            right_min = self.right.find_min()
            self.key = right_min
            self.right = self.right.delete(right_min)
        return self
            
#7: height            
    def get_height(self):
        if self is None:
            return 0
        else:
            left_height = right_height = 1
            if self.left:
                left_height += self.left.get_height()
            if self.right:
                right_height += self.right.get_height()
            return max(left_height, right_height)
          
#8: sum               
    def Sum(self):
        global sum
        sum += int(self.key)
        for child in [self.left, self.right]:
            if child:
                child.Sum()
        return sum
    
#9: count
    def Count(self):
        global count
        count += 1
        for child in [self.left, self.right]:
            if child:
                child.Count()
        return count
    
#10: average
    def Average(self):
        print('Average=', sum/count)
       
       
#11: postorder  
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.key, end=' ')
        
        
        
     
#demo     
if __name__ == '__main__':
    data = [41, 32, 8, 15, 24, 28, 11, 10, 58, 31, 7]
    T = BSTNode(data[0])
    for i in data[1:]:
        T.insert(i)
    print('PreOrder')
    T.preOrder()
    print()
    print('InOrder')
    T.inOrder()
    print()
    print('PostOrder')
    T.postOrder()
    print()
    print('Min =',T.find_min())
    print('Right Min', T.right.find_min())
    print('Left Min', T.left.find_min())
    print('Max =',T.find_max())
    print('Right Max', T.right.find_max())
    print('Left Max', T.left.find_max())
    T.delete(6)
    T.delete(19)
    T.delete(34)
    print('PreOrder')
    T.preOrder()
    print()
    print('InOrder')
    T.inOrder()
    print()
    print('PostOrder')
    T.postOrder()
    print()
    print('Height =', T.get_height())
    print('Sum =',T.Sum())
    print('Count =',T.Count())
    T.Average()
    