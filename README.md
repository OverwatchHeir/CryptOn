ProPass
----------

ProPass is an open-source tool that allows :

   - Secure passwords generation based on [OWASP criteria].
   - Passwords strength & security checks based on [OWASP Guidelines for enforcing secure passwords].
   - RSA key pair generation.
   - SSH key pair generation (using RSA).
   - ECDSA key pair generation.
   - GPG tools & features ( only in interactive mode)

About
-----------------

**Passwords**

Passwords are a real security threat. Impossible-to-crack passwords are complex with multiple types of 
characters (numbers, letters, and symbols). 
So if you want to safeguard your personal info and assets, creating secure passwords is a big first step and 
ProPass will help you to achieve it.

It is usual in the computer industry to specify password strength in terms of information entropy which is measured 
in bits and is a concept from information theory. Instead of the number of guesses needed to find the password 
with certainty, the base-2 logarithm of that number is given, which is the number of "entropy bits" in a password.

**Asymmetric Cryptography**

We can also use cryptography with authentication. Therefore, we have asymmetric public-private key cryptosystems. Two of the best-known uses of 
public key cryptography are:

   - Public key encryption, in which a message is encrypted with a recipient's public key. The message cannot be 
     decrypted by anyone who does not possess the matching private key, who is thus presumed to be the owner of that 
     key and the person associated with the public key. This is used in an attempt to ensure confidentiality.
     
   - Digital signatures, in which a message is signed with the sender's private key and can be verified by 
     anyone who has access to the sender's public key. This verification proves that the sender had access to the 
     private key, and therefore is likely to be the person associated with the public key. This also ensures that 
     the message has not been tampered with, as a signature is mathematically bound to the message it originally was 
     made with, and verification will fail for practically any other message, no matter how similar to the original 
     message.
     
There are public-private key cryptosystems algorithms such as [RSA] and [ECDSA].

RSA and ECDSA are well-regarded. They are considered quite secure and is commonly used in:

   - SSH Authentication
   - SSL Certficates
   - VPN Tunnel Encryption
   - Email & Messaging Encryption
   - Etc

**GPG or GnuPG**

GPG or GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP). 
It allows you to encrypt and sign your data and communications; it features a versatile key management system, along 
with access modules for all kinds of public key directories. [What is encryption?]

Using encryption helps to protect your privacy and the privacy of the people you communicate with. Encryption makes 
life difficult for bulk surveillance systems. GnuPG is one of the tools that Snowden used to uncover the secrets of 
the NSA. If you want more information you can look up at [GnuPG] or [How GPG encrypt and decrypt works?].

Requirements
----------
  - python 3
  - pip
  - termcolor
  - cryptography
  - ecdsa
  - python-gnupg
  - validate_email
  - py3dns


Installation
-------------

First of all, we would python 3, pip and gnupg installed in our computer.

**Linux**

 ```
 $ apt-get install python3-pip
 $ apt-get install gnupg
 ```
 
**MacOS**
 ```
 $ brew install python3
 $ brew install pip
 $ brew install gnupg
 ```
 **Windows**
 
 Download python 3 and pip from [python webpage] and gnupg from [Gpg4win].
 
 
Secondly, we install the tool using the traditional installation from **pip**

 ```
 $ easy_install3 -U pip # you have to install python3-setuptools , update pip
 $ pip3 install propass
 $ propass # installed successfully
```

Usage
----------

**Run**
```
$ propass
```

**Options**
```
optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     Run script in interactive mode
  -g [length [number ...]], --generator [length [number ...]]
                        Secure passwords generation // Defaults: length (20) -
                        number of passwords (1)
  -c password, --check password
                        Passwords strength & security checks
  -r [key_size [key_size ...]], --rsa [key_size [key_size ...]]
                        RSA key pair // Defaults: bits (2048)
  -s [key_size [key_size ...]], --ssh [key_size [key_size ...]]
                        SSH Identity key pair // Defaults: bits (2048)
  -e [key_size [key_size ...]], --ecdsa [key_size [key_size ...]]
                        ECDSA key pair // Defaults: bits (256)

```

**Notes**

IN SOME CASES, if your password contains the special characters you may have problems when parsing. That's because of 
your shell. You should type ``` \ ``` before each special character in the password.

If you want to use the GPG features from the command line, use your native ```gpg``` command in a terminal.

Contributing
------------
For bug reports or enhancements, please open an [issue] here.

[OWASP criteria]: https://www.owasp.org/index.php/Authentication_Cheat_Sheet#Implement_Proper_Password_Strength_Controls
[issue]: https://github.com/OverwatchHeir/ProPass/issues
[python webpage]: https://www.python.org
[OWASP Guidelines for enforcing secure passwords]: https://www.owasp.org/index.php/Authentication_Cheat_Sheet#Implement_Proper_Password_Strength_Controls
[ECDSA]: https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet
[RSA]: https://www.di-mgt.com.au/rsa_alg.html
[GnuPG]: https://gnupg.org/index.html
[What is encryption?]:https://www.golinuxcloud.com/tutorial-encrypt-decrypt-sign-file-gpg-key-linux/
[How GPG encrypt and decrypt works?]:https://www.golinuxcloud.com/tutorial-encrypt-decrypt-sign-file-gpg-key-linux/
[Gpg4win]: https://www.gpg4win.org/