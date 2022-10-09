from colorama import Fore
import hashlib

passwordHash = input('Enter MD5 Hash Value: ')

for word in open(input("Enter password file name:")):
    print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
    encodeWord = word.encode('UTF-8')
    md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()

    if md5Hash == passwordHash:
        print(Fore.GREEN + '[+] Password Found: ' + word)
        exit(0)
    else:
        pass

print('[-] Password Not in List')
