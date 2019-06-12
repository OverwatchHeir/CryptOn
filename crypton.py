from termcolor import colored
import errors
from modes import command_line as command_line, interactive_mode as interactive_mode
from cli.cli import Cli
from crypt_algorithms.asymmetric.dsa import DSA
from crypt_algorithms.asymmetric.ecdsa import ECDSA
from crypt_algorithms.asymmetric.rsa import RSA


# ProPass Run
#

# Interactive mode

def interactive():
    cli = Cli()
    cli.display_menu()
    option = cli.get_option(prompt=cli.crypton_cli)

    while True:
        if option == 0:
            quit()

        if option == 1:
            pass_length, pass_number = cli.display_password_generator()
            command_line.show_passwords(pass_length, pass_number)

        if option == 2:
            password = cli.display_password_checker()
            command_line.check_password(args=password)

        if option == 3:
            interactive_mode.symmetric()

        if option == 4:
            interactive_mode.asymmetric()

        if option == 5:
            interactive_mode.hashing()

        option = cli.get_option(prompt=cli.crypton_cli)


# Command line mode

def command(parser, args):
    if args.version is not None:
        Cli().display_banner()

    if args.generate_password is not None:
        command_line.generate_password(parser=parser, args=args.generate_password)

    if args.check_password is not None:
        command_line.check_password(args=args.check_password)


# Main entry point

def main():
    parser, args = command_line.create_parser()

    if args.interactive:
        interactive()

    else:
        command(parser, args)


if __name__ == '__main__':
    main()
