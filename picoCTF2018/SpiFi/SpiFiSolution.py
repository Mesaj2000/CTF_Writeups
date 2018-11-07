from pwn import *

# Option to export the flag to a txt file for safe-keeping, if desired
# g=open("flaglog.txt", "a+")

flag = ""

# "Front Padding", lines up our message with the byteblocks
fpad = "0"*11

# "Back Padding", lines up the flag with the byteblocks
bpad = "0"*48

# Our guess for the next flag character 
nextchr = ""

# 15 characters long, because it doesn't include our guess
message = "fying code is: "

for j in range(38):


    for i in range(32, 126):

        r = remote("18.224.157.204", 33893)


        r.sendline(fpad + message + chr(i) + bpad)

        r.recvuntil(": ")
        output = r.recvline()

		# Extract substrings cooresponding to our input and the flag
        myEncoded = output[128:160]
        flagEncoded = output[288:320]

        r.close()

		# If it's a match, our guess is correct!
        if myEncoded == flagEncoded:
            nextchr = chr(i)
            break

    # Update our message to include the next character, making sure to keep it 15 characters long
    message = message[1:] + nextchr
	
    # Shift the flag one character back to line up with our new message
    bpad = bpad[1:]
    
    # Print the flag as we go, in case of a disconnection
    flag = flag + nextchr
    print(flag)
    # g.write(flag + "\n")

# g.close()

