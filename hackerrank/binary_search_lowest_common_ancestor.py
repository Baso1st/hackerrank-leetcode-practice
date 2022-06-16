# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem


def lca(root, v1, v2):
    ance_1 = get_ance(root, v1)
    ance_2 = get_ance(root, v2)
    lca = root
    while ance_1 and ance_2:
        front1 = ance_1.pop(0)
        front2 = ance_2.pop(0)
        if front1 == front2:
            lca = front1

    return lca
  
  
def get_ance(root, v):
    ance = []
    current = root
    while current:
        if current.info == v:
            break
        
        ance.append(current)
        if v <= current.info:
            current = current.left
        else:
            current = current.right
            
    ance.append(current)
    
    return ance
