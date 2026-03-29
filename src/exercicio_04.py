def format_name(name: str) -> tuple[str, str, str]:
    """
    Retorna o nome em diferentes formatos.

    Args:
        name (str): nome de entrada

    Returns:
        tuple[str, str, str]: (lowercase, uppercase, titlecase)
    """
    lowercase = name.lower()
    uppercase = name.upper()
    titlecase = name.capitalize()
    
    return (lowercase,uppercase,titlecase)
