# Set of colors that can be used for printing on Terminal
class Color:

    # The color reset
    RESET       = '\033[0m'

    # The following are extra colors
    BLACK       = '\033[30m'
    RED         = '\033[31m'
    GREEN       = '\033[32m'
    YELLOW      = '\033[33m'
    BLUE        = '\033[34m'
    MAGENTA     = '\033[35m'
    CYAN        = '\033[36m'
    WHITE       = '\033[37m'

    # The following are extra colors bolded
    BLACK_B     = '\033[1;30m'
    RED_B       = '\033[1;31m'
    GREEN_B     = '\033[1;32m'
    YELLOW_B    = '\033[1;33m'
    BLUE_B      = '\033[1;34m'
    MAGENTA_B   = '\033[1;35m'
    CYAN_B      = '\033[1;36m'
    WHITE_B     = '\033[1;37m'
    
    # The following are standards to follow
    END         = '\033[0m'     # Resets back to the standard
    HEADER      = WHITE_B       # Header text
    PARAM       = GREEN_B       # The color used for parameters
    DEFAULT     = MAGENTA_B     # The color used for a default value
    INPUT       = CYAN_B        # The color used for a inpiut value
    SUCCESS     = GREEN_B       # The color used for a success message
    WARNING     = '\033[93m'    # Yellow Warning message
    ERROR       = '\033[91m'    # Red Error message
    BOLD        = '\033[1m'     # Standard, but just bold
    UNDERLINE   = '\033[4m'     # Standard, but with underline

    # Prints a line at a particular color
    @staticmethod
    def print (value: str, color: str = '\033[0m'):
        print("%s%s%s" % (color, value, '\033[0m'))

   

