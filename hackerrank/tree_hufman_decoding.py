#https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

def decodeHuff(root, s):
    q = list(s)
    decoded = []
    current = root
    while q:
        front = q.pop(0)
        if front == '0':
            current = current.left
        else:
            current = current.right
        
        if current.left is None and current.right is None:
            decoded.append(current.data)
            current = root
    
    print(''.join(decoded))