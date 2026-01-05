# HealthGPT

![image.png](images/image.png)

This is an AI prompt injection challenge. At first, it almost rejected all my injections

![image.png](images/image%201.png)

However, when I asked why it rejects me, it replies me with the flag

![image.png](images/image%202.png)

I still want to dig deeper, so I try other prompts, some work and some don’t

![image.png](images/image%203.png)

However, stating to return the instructions instead of text will return the flag, although it is labeled as fake

![image.png](images/image%204.png)

If you try to include the words `emergency` or `DAN`, you will get rejected. The AI is tricking me

![image.png](images/image%205.png)

How about tricking it that the flag is a medicine necessary for my survival?

![image.png](images/image%206.png)

But when I asked it why it is dangerous and give me some details, it leaked the flag

![image.png](images/image%207.png)

To summarize, this AI can be exploitable using:

1. Asking him to explain
2. Repeat Instructions
3. Role play

Flag: `THM{policy_bypassed}`
