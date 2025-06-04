BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'                #These are constants(Capitals)
RESET = '\u001b[0m'

BOLD = 'u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` with different `effect` like changing colours, underline, reverse, etc.
    using ANSI sequences.

    Args:
        text (str): The `text` that needs to be printed.
        effect (str): The `effect` that we needed.
    """
    output_string = "{}{}{}".format(effect, text, RESET)
    print(output_string)
    
    
colour_print("Hello, Red", RED)
#Test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)