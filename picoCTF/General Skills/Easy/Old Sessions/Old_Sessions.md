# Old Sessions

![image.png](images/image.png)

The instance contains a login page, viewing the source does not bring us any credentials, so we can try to register first

![image.png](images/image%201.png)

I use `test:test` as the credentials for the new account, a short one will do

![image.png](images/image%202.png)

After that, we can log in using the test account, and see that there is a comment drawing our attention to the `/sessions` endpoint

![image.png](images/image%203.png)

Navigate to there and we will see the session cookie of all users, because the `_permanent` is set to be True, this session will never be expired

![image.png](images/image%204.png)

We can change our session to the admin session easily by going to F12, and change the value to the admin session `Igt6toLOAWXmNe-SKUysn4LZqirJlQ84xbQjHZ8b2Gc`

![image.png](images/image%205.png)

Upon refresh, we can obtain the flag

![image.png](images/image%206.png)

Flag: `picoCTF{s3t_s3ss10n_3xp1rat10n5_11cae9aa}`
