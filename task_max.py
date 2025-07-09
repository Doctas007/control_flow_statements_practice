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
        return 'a eng katta son'
    if b>a>c:
        return 'b eng katta son'
    if c>b>a:
        return 'c eng katta son'
    if c>a>b:
        return 'c eng katta son'
    if b>a>c:
        return 'b eng katta son'
    if a>c>b:
        return 'a eng katta son'
print(find_max(5,3,6))

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
        return 0
    if b>a>c:
        return 1
    if c>b>a:
        return 2
    if c>a>b:
        return 2
    if b>a>c:
        return 1
    if a>c>b:
        return 0
print(find_max_idx(1,2,3))
# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2