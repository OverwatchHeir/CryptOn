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
    option = cli.get_option(prompt=cli.propass_cli)

    while True:
        if option == 0:
            quit()

        if option == 1:
            pass_length, pass_number = cli.display_password_generator()
            command_line.show_passwords(pass_length, pass_number)

        if option == 2:
            password = cli.display_password_checker()
            command_line.show_check(password)

        if option == 3:
            interactive_mode.symmetric()

        if option == 4:
            interactive_mode.asymmetric()

        if option == 5:
            interactive_mode.hashing()

        option = cli.get_option(prompt=cli.propass_cli)


# Command line mode

def command(parser, args):
    if args.version is not None:
        cli = Cli()
        cli.display_banner()

    # Secure password generator
    if args.generator is not None:
        if len(args.generator) == 0:
            command_line.show_passwords(16, 1)

        elif len(args.generator) == 2:
            length = args.generator[0]
            number = args.generator[1]

            if length < 16 or number < 1:
                print(errors.value)
            else:
                command_line.show_passwords(length, number)

        elif len(args.generator) != 2:
            parser.error('expected 2 arguments')

    # Password security checker
    if args.check is not None:
        command_line.show_check(args.check)

    # RSA Key Pair generator
    if args.rsa is not None:
        if len(args.rsa) == 0:
            RSA().file_key_pair()
            print(colored('\nRSA Key pair generated!\n', 'green'))
        elif len(args.rsa) > 1:
            parser.error('expected 1 argument')
        elif args.rsa[0] not in RSA.options_key:
            print(errors.rsa_key_size)
        else:
            RSA(args.rsa[0]).file_key_pair()
            print(colored('\nRSA Key pair generated!\n', 'green'))

    # SSH Key Pair generator
    if args.ssh is not None:
        if len(args.ssh) == 0:
            RSA().file_key_pair(ssh=True)
            print(colored('\nSSH Identity key pair generated!\n', 'green'))
        elif len(args.ssh) > 1:
            parser.error('expected 1 argument')
        elif args.ssh[0] not in RSA.options_key:
            print(errors.rsa_key_size)
        else:
            RSA(key_size=args.ssh[0]).file_key_pair(ssh=True)
            print(colored('\nSSH Identity key pair generated!\n', 'green'))

    # DSA Key Pair generator
    if args.dsa is not None:
        if len(args.dsa) == 0:
            DSA().file_key_pair()
            print(colored('\n  DSA key pair generated!\n', 'green'))
        elif len(args.dsa) > 1:
            parser.error('expected 1 argument')
        elif args.dsa[0] not in DSA.options_key:
            print(errors.dsa_key_size)
        else:
            DSA(key_size=args.dsa[0]).file_key_pair()
            print(colored('\nDSA key pair generated!\n', 'green'))

    # ECDSA Key Pair generator
    if args.ecdsa is not None:
        if len(args.ecdsa) == 0:
            ECDSA().file_key_pair()
            print(colored('\nECDSA key pair generated!\n', 'green'))
        elif len(args.ecdsa) > 1:
            parser.error('expected 1 argument')
        elif args.ecdsa[0] not in ECDSA.options_key:
            print(errors.ecdsa_key_size)
        else:
            ECDSA(key_size=args.ecdsa[0]).file_key_pair()
            print(colored('\nECDSA key pair generated!\n', 'green'))


# Main entry point

def main():
    parser, args = command_line.create_parser()

    if args.interactive:
        interactive()

    else:
        command(parser, args)


if __name__ == '__main__':
    main()
