import argparse
import os
from termcolor import colored
from crypt_algorithms.password.check import Checker
from crypt_algorithms.password.generate import Generator

checker = Checker()
generator = Generator()
file_path = os.getcwd()


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-v",
                        "--version",
                        dest="version",
                        action="store_true",
                        help="See script version")

    parser.add_argument("-i",
                        "--interactive",
                        dest="interactive",
                        action="store_true",
                        help="Run script in interactive mode")

    parser.add_argument("-g",
                        "--generator",
                        nargs='*',
                        metavar=('length', 'number'),
                        type=int,
                        help="Secure passwords generation"
                             " // Defaults: length (20) - number of passwords (1)")

    parser.add_argument("-c",
                        "--check",
                        type=str,
                        metavar='password',
                        help="Passwords strength & security checks")

    parser.add_argument("-r",
                        "--rsa",
                        type=int,
                        nargs='*',
                        metavar='key_size',
                        help="RSA key pair // Defaults: bits (2048)")

    parser.add_argument("-s",
                        "--ssh",
                        nargs='*',
                        type=int,
                        metavar='key_size',
                        help="SSH Identity key pair // Defaults: bits (2048)")

    parser.add_argument("-d",
                        "--dsa",
                        nargs='*',
                        type=int,
                        metavar='key_size',
                        help="DSA key pair // Defaults: bits (2048)")

    parser.add_argument("-e",
                        "--ecdsa",
                        nargs='*',
                        type=int,
                        metavar='key_size',
                        help="EDSA key pair // Defaults: bits (256)")

    return parser, parser.parse_args()


def show_passwords(length, number):
    print('\n' + colored('Entropy : ', 'green') + colored(str(checker.entropy(length)) + ' bits', 'white') + '\n')

    for n in range(number):
        print(colored('Password ' + str(n + 1) + ' : ', 'green') + colored(generator.secure_password(length), 'white')
              + '\n')


def show_check(password):
    print('\n' + colored('Entropy : ', 'green') + colored(str(checker.entropy(len(password))) + ' bits', 'white'))
    print(checker.strength(password) + '\n')
