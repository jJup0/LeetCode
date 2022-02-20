class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __repr__(self): 
        printList = []
        while self:
            printList.append(self.val)
            self = self.next
        return 'LinkedList: ' + str(printList)

    def addNode(self, newVal):
        self.next = ListNode(newVal)
        return self.next

    def removeNode(self, root, val, prev):
        if self.val == val:
            if not(prev):
                root = self.next  # basically delete self
                if not root:
                    root = ListNode(0)
            else:
                prev.next = self.next
        elif self.next:
            root = self.next.removeNode(root, val, self)
        return root

class slowLLFirstUnique:
    def __init__(self, nums: [int]):
        self.end = self.root = ListNode(None)
        self.delDict = dict()  # val : del_boolean
        for num in nums:
            self.add(num)
        if not(self.root.val) and self.root.next:
            self.root = self.root.next
        # print('Finished Init \ndeldict:', self.delDict, '\nroot:', self.root, '\nend:', self.end, '\n')
        
    def showFirstUnique(self) -> int:
        if self.root.val:
            return self.root.val
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.delDict:
            if not(self.delDict[value]):
                self.root=self.root.removeNode(self.root, value, None)
                self.delDict[value] = True
        else:
            self.end = self.end.addNode(value)
            self.delDict[value] = False
            if not self.root.val:
                self.root = self.root.next
            
        if not self.root:
            pass
        elif not self.root.val and not self.root.next:
            self.end= self.root


class faileOrderedDictFirstUnique:
    def __init__(self, nums: [int]):
        self.cache = OrderedDict()
        for num in nums:
            if num in self.cache:
                self.cache[num] = -1  # so that new item is automatically at end
                self.cache.move_to_end(num)
            else:
                self.cache[num] = num

    def showFirstUnique(self) -> int:
        return list(self.cache)[0]

    def add(self, value: int) -> None:
        if value in self.cache:
            self.cache[value] = -1  # so that new item is automatically at end
            self.cache.move_to_end(value)
        else:
            self.cache[value] = value


class slowFirstUnique:

    def __init__(self, nums: [int]):
        self.seen = set()
        self.unique = []
        for x in nums:
            if x in self.seen:
                try:
                    self.unique.remove(x)
                except:
                    pass
            else:
                self.seen.add(x)
                self.unique.append(x)

    def showFirstUnique(self) -> int:
        if self.unique:
            return self.unique[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.seen:
            try:
                self.unique.remove(value)
            except:
                pass
        else:
            self.seen.add(value)
            self.unique.append(value)
