from colorama import init, Fore, Style

# Initialize colorama with autoreset to ensure colors are reset automatically
init(autoreset=True)

def print_header(message):
    """Prints a header message in bright cyan color."""
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{message}")

def print_error(message):
    """Prints an error message in red color."""
    print(f"{Fore.RED}{message}")

def print_success(message):
    """Prints a success message in green color."""
    print(f"{Fore.GREEN}{message}")

def print_warning(message):
    """Prints a warning message in yellow color."""
    print(f"{Fore.YELLOW}{message}")

def print_info(message):
    """Prints an informational message in blue color."""
    print(f"{Fore.BLUE}{message}")

def print_highlight(message):
    """Prints a highlighted message in bright magenta."""
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{message}")

def print_debug(message):
    """Prints a debug message in white color."""
    print(f"{Fore.WHITE}{message}")


def get_user_input(prompt):
    return input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}").strip()