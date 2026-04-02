# Undo

![image.png](images/image.png)

Once we launch the instance we are asked to reverse the flag step by step

```python
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.
```

<aside>
💡

Normally, you need to use these commands with a pipe or I/O redirection (`<<<`) as the commands below accept files as their inputs. For example, the full valid command for this case will be `echo KTZvNHFycnE4LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj|base64 -d`. 

However for this challenge, we only need to answer the core part, which is `base64 -d` in this case

</aside>

The first step is to decode the base64 string

```python
-- Step 1 ---
Current flag: KTZvNHFycnE4LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it:
```

To do this we need to use `base64 -d`

After typing the correct command, we will proceed to the next step, which is to reverse the entire string

```python
Enter the Linux command to reverse it: base64 -d
Correct!

--- Step 2 ---
Current flag: )6o4qrrq8-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it:
```

There is a utility called `rev`, which can reverse the input

Step 3 and 4 are basically the same, we can use `tr` to replace certain characters.

```python
...
Enter the Linux command to reverse it: rev
Correct!

--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-8qrrq4o6)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: tr - _
Correct!

--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_8qrrq4o6)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: tr '()' '{}'
Correct!
```

For Step 5, it is a ROT-13 shifted string, which a will shift 13 letters and become n. To transform correctly, you need to care both uppercase and lowercase characters, while ensuring the shifting are correct

```python
--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_8qrrq4o6}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: tr a-zA-Z n-za-mN-ZA-M
Correct!

Congratulations! You've recovered the original flag:
>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_8deed4b6}
```

After all these steps, you will obtain the flag

Flag: `picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_8deed4b6}`
