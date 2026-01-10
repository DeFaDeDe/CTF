# Neighbour

![image.png](images/image.png)

There is a login form after we arrive on the page

![image.png](images/image%201.png)

If we read the source code, we can see there are test credentials `guest:guest`, we can use them to log in

![image.png](images/image%202.png)

After we log in, we can see that it references the current user (guest) in the URL. What if we change it to admin?

![image.png](images/image%203.png)

We get the flag!

![image.png](images/image%204.png)

Flag: `flag{66be95c478473d91a5358f2440c7af1f}`
