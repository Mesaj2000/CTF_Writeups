import crypt


'''
put the hashed password you want to guess as "theirHash"
you must run in terminal, not IDLE
it may take a bit
'''

theirHash = "$6$HRMJoyGA$26FIgg6CU0bGUOfqFB0Qo9AE2LRZxG8N3H.3BK8t49wGlYbkFbxVFtGOZqVIq3qQ6k0oetDbn2aVzdhuVQ6US."


def rockYou():
    with open('rockyou.txt','r') as f:
        for guess in f:
            guess = guess.rstrip("\n")
            myHash = crypt.crypt(guess, '$6$HRMJoyGA')
            if myHash == theirHash:
                print(guess)
                return

    print("NOPE!!!")
    return

rockYou()
