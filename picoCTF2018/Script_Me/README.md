When you run the netcat, you get the following output:

```
Rules:
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

Example:
(()) + () = () + (()) = (()())

Let's start with a warmup.
(()) + ((())()) = ???
```


It seems rather arcane at first, but it can all be broken down into a few simple rules:
1. Each problem will consist of several "units" of parentheses added together, ending with `"= ???"`
2. Each unit has a "depth" corresponding to the maximum number of opened and unclosed parentheses.
	* E.g. `(())` has a depth of 2, as does `(()()()())`, while `((())()())` has a depth of 3
3. Additions are always conducted left-to-right ("left-associative")
4. If two units are of equal depth, they are simply concatenated ("combine")
5. Otherwise, the shallower unit is "absorbed" into the deeper one, by placing it inside the outermost parenthesis
	* E.g. `((())) + () = ((()) () )`		*space added to show where the shallow unit went*
	* Conviently, the depth of the result with always be equal to the depth of the deeper unit; not more, not less
		
		
With all that in mind, all that's left is to, as the problem's name would suggest, write a script.
[Here's mine.](ScriptMeSolution.py)


When all is said and done, the flag reads: `picoCTF{5cr1pt1nG_l1k3_4_pRo_45ca3f85}`
