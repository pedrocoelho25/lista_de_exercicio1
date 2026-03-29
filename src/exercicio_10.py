def greet_names(names: list[str]) -> list[str]:
    """
    Retorna uma lista de saudações para cada nome.

    Args:
        names (list[str]): lista de nomes

    Returns:
        list[str]: lista com mensagens "Hello, <name>!"
    """
    list = []
    for name in names:
        list.append( f"Hello, {name}!")

  
    return list
