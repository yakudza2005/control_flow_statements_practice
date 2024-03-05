def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    if a>b>c:
        return a
    if a<b<c:
        return c
    if b>c>a:
        return b
print(find_max(2,6,4))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    if a>b>c:
        return 1
    if a<b<c:
        return 3
    if a<c<b:
        return(2)
print(find_max_idx(3,7,6))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2