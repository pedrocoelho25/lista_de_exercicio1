def sum_numbers(n: int) -> int:
    """
    Calcula a soma dos números de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        int: soma total
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

sum_numbers(3)
