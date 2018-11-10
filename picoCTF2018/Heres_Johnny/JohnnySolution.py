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
