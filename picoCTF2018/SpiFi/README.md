The first thing to do is run the netcat and see what happnes.
```
Welcome, Agent 006!
Please enter your situation report:
```
After typing something in (literally "something", in this case), we get:
```
72f8928a2758a3379144f3c01fb298a41527c40d73f78fd78ba96d842e6d9587d2d89cbf39636928ba9b43db8bf5e34891008c11dbc30270b0436cbf4e111293d05ad4aafe3724e6b66c6a624ec63f4273df451990c403ec07705c47b94d1da9b55dc8361873d9fa6b0dffae3351f9325e41e9b770c7d1484eb7b50f1146e9d2ddc9192a866e93e34cce00138d19d704590c1094a68b52f00a543c43b43ea3fb
```
And that's it. The output is over.


To make heads or tails of this, we look at the included [source code](spy_terminal_no_flag.py), and notice a few things.
1. The encryption uses AES.MODE_ECB
2. The output ("72f89...") is always encrypted with the same key
3. The output always follows the same format, specifically,
```
Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
```

Where `{0}` is whatever we type, `{1}` is the flag, and the message is always padded with
'0' characters such that the character count is a multiple of 16 (a requirement of ECB)


This is the part where we need to research what exactly ECB is, and how to exploit it.
1. ECB divides the message into "byteblocks": 16-byte (16 character) chunks, and encrypts them independently
2. Identical byteblocks are encoded identically.
      * e.g. if the string "abcdefghijklmnop" were to appear twice in the same message such that both times it lined up *perfectly* with the byteblocks, the output would encode both occurances the same way
3. One byteblock (16 characters) cooresponds to 32 characters of output


So, the plan of attack is as follows:
1. Manipulate the byteblocks such that we know excatly how the flag lines up
2. Move the first character of the flag to the end of a byteblock of otherwise known characters
3. Guess every possible character until we get a match
4. Repeat for the next flag character

Specifically, we need to input the following line:
`00000000000fying code is: *` 
Where those eleven 0s are finishing out the previous byteblock ("Agent, Gre... as follows"), and
the * represents every possible character for the beginning of the flag (should be "p" for "picoCTF")


We'll know we get a match when the substring of the output cooresponding to our input matches
the section corresponding to where the flag should be.


All we need to do now is write a [script](SpiFiSolution.py), which gives the following output (make sure to run in silent mode):
```
p
pi
pic
pico
picoC
picoCT
picoCTF
picoCTF{
picoCTF{@
picoCTF{@g
picoCTF{@g3
picoCTF{@g3n
picoCTF{@g3nt
picoCTF{@g3nt6
picoCTF{@g3nt6_
picoCTF{@g3nt6_1
picoCTF{@g3nt6_1$
picoCTF{@g3nt6_1$_
picoCTF{@g3nt6_1$_t
picoCTF{@g3nt6_1$_th
picoCTF{@g3nt6_1$_th3
picoCTF{@g3nt6_1$_th3_
picoCTF{@g3nt6_1$_th3_c
picoCTF{@g3nt6_1$_th3_c0
picoCTF{@g3nt6_1$_th3_c00
picoCTF{@g3nt6_1$_th3_c00l
picoCTF{@g3nt6_1$_th3_c00l3
picoCTF{@g3nt6_1$_th3_c00l3$
picoCTF{@g3nt6_1$_th3_c00l3$t
picoCTF{@g3nt6_1$_th3_c00l3$t_
picoCTF{@g3nt6_1$_th3_c00l3$t_7
picoCTF{@g3nt6_1$_th3_c00l3$t_75
picoCTF{@g3nt6_1$_th3_c00l3$t_757
picoCTF{@g3nt6_1$_th3_c00l3$t_7570
picoCTF{@g3nt6_1$_th3_c00l3$t_75707
picoCTF{@g3nt6_1$_th3_c00l3$t_757076
picoCTF{@g3nt6_1$_th3_c00l3$t_7570765
picoCTF{@g3nt6_1$_th3_c00l3$t_7570765}
```
Beautiful.
