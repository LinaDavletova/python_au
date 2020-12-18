# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = '[ ' + str(current.value) + ''
            while current.next != None:
                current = current.next
                out += ', ' + str(current.value) + ' '
            return out + ']'
        return '[]'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    def push(self, x):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def Del(self, i):
        if (self.first == None):
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    def __getitem__(self, key):  # поддержка обращения по ключу
        length = 0
        current = None
        if self.first != None:
            current = self.first
            while key != length and current.next != None:
                current = current.next
                length += 1
            if key == length: current = current.value
        return current

    def len(self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first


L1 = LinkedList()
L2 = LinkedList()
a = input().upper()
b = input().upper()
for i in a:
    if i != '-':
        L1.add(i)
for i in b:
    if i != '-':
        L2.add(i)

print(L1)
print(L2)

n = []
for i, c in enumerate('0123456789ABCDEF'):
    n.append(c)

ans = LinkedList()
len1 = L1.len()
len2 = L2.len()
k = 0
for i in range(min(len1, len2)):
    num = (n.index(L2[len2 - 1 - i]) + n.index(L1[len1 - 1 - i])) + k
    if num > 15:
        num -= 16
        ans.push(n[num])
        k = 1
    else:
        ans.push(n[num])
        k = 0
if len1 < len2:
    for i in range(len1, len2):
        num = n.index(L2[len2 - 1 - i]) + k
        if num > 15:
            num -= 16
            ans.push(n[num])
            k = 1
        else:
            ans.push(n[num])
            k = 0
else:
    for i in range(len2, len1):
        num = n.index(L1[len1 - 1 - i]) + k
        if num > 15:
            num -= 16
            ans.push(n[num])
            k = 1
        else:
            ans.push(n[num])
            k = 0
print(L1, ' + ', L2, ' = =', ans)
