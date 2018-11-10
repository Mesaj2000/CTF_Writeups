The problem gives us two files: "[passwd](passwd.txt)" and "[shadow](shadow.txt)". These should look familiar to linux users.

Password:
```
root:x:0:0:root:/root:/bin/bash
```

Shadow:
```
root:$6$HRMJoyGA$26FIgg6CU0bGUOfqFB0Qo9AE2LRZxG8N3H.3BK8t49wGlYbkFbxVFtGOZqVIq3qQ6k0oetDbn2aVzdhuVQ6US.:17770:0:99999:7:::
```

The passwd file contains all of the user accounts on a system and various pieces of information about them. The shadow file contains all of the password hashes for those users. It appears that the only account on this system is root.


Under normal situations, it is practically impossible to crack a hash of this nature, however, the problem's hint gives us some insight:
```
If at first you don't succeed, try, try again. And again. And again.
If you're not careful these kind of problems can really "rockyou".
```

The first hint suggests a brute force attack. The second, after a quick bout of googling, suggests to guess common passwords. You see, RockYou was a company that engaged in *terrible* security practices and ultimately got hacked. However, their leaked data revealed a much more intersting thing: a LOT of people use very, very weak passwords, and by chance often end up using the same ones as other people. This lead to the creation of the infamous ["RockYou.txt"](rockyouabridged.txt), a file that contains all 14 million of the most common weak passwords that people actually use. Here, I have included a (very) abridged version of the file, because the [real one](rockyou.zip) is too big to upload to GitHub.


The problem's title, "Here's Johnny", hints at using a tool called "John the Ripper", a free password cracker that comes with many features, including rockyou attacks. However, for the purposes of this challenge you could just write a quick [python script](JohnnySolution.py) instead:
```
from crypt import crypt

theirHash = "$6$HRMJoyGA$26FIgg6CU0bGUOfqFB0Qo9AE2LRZxG8N3H.3BK8t49wGlYbkFbxVFtGOZqVIq3qQ6k0oetDbn2aVzdhuVQ6US."

def rockYou():
    with open('rockyouabridged.txt','r') as f:
        for guess in f:
            guess = guess.rstrip("\n")
            myHash = crypt(guess, '$6$HRMJoyGA')
            if myHash == theirHash:
				return guess

    return "NOPE!!!"

print(rockYou())
```

Either way, the password is `hellokitty`. Use that to login as root through the netcat, and voila:
```
picoCTF{J0hn_1$_R1pp3d_99c35524}
```
