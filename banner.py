# Color Definitions
RED = '\033[1;91m'
WHITE = '\033[46m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
DEFAULT = '\033[3;0m'
YELLOW = '\033[1;33m'
YELLOW2 = '\033[1;93m'
GREEN2 = '\033[1;92m'

def banner():
    kill = '''
{5}██████{0}╗ {5}███████{0}╗{5}██{0}╗   {5}██{0}╗{5}██{0}╗{5}██{0}╗   {5}█{0}╗ {5}███████{0}╗     {5}██████{0}╗ {5}█████{0}╗ {5}██{0}╗     {5}██{0}╗     
{5}██{0}╔══{5}██{0}╗{5}██{0}╔════╝{5}██{0}║   {5}██{0}║{5}██{0}║{5}██{0}║   {0}╚╝ {5}██{0}╔════╝    {5}██{0}╔════╝{5}██{0}╔══{5}██{0}╗{5}██{0}║     {5}██{0}║     
{5}██{0}║  {5}██{0}║{5}█████{0}╗  {5}██{0}║   {5}██{0}║{5}██{0}║{5}██{0}║      {5}███████{0}╗    {5}██{0}║     {5}███████{0}║{5}██{0}║     {5}██{0}║     
{5}██{0}║  {5}██{0}║{5}██{0}╔══╝  ╚{5}██{0}╗ {5}██╔{0}╝{5}██{0}║{5}██{0}║      ╚════{5}██{0}║    {5}██{0}║     {5}██{0}╔══{5}██{0}║{5}██{0}║     {5}██{0}║     
{5}██████{0}╔╝{5}███████{0}╗ ╚{5}████{0}╔╝ {5}██{0}║{5}███████{0}╗ {5}███████{0}║    ╚{5}██████{0}╗{5}██{0}║  {5}██{0}║{5}███████{0}╗{5}███████{0}╗
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝
    '''.format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW)

    # Displaying the banner
    print("\t\t\t{2}YOU ARE GOING TO MAKE A{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW))
    print(kill)
    print("{0} \n\t\t\t\tby hasanfirnas{1}".format(GREEN, DEFAULT))  # Signature

# Call the banner function to display it
banner()
