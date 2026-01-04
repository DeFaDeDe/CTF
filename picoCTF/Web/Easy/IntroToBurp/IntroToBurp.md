# IntroToBurp

![image.png](images/image.png)

Within the web instance, there is an HTML registration form that we can fill out. Here I type everything as ‘test’

![image.png](images/image%201.png)

However, after that, we have no idea how to fill in the OTP

![image.png](images/image%202.png)

If we try to submit ‘test’, it will return ‘**Invalid OTP**’

To solve this challenge, we need to use a tool called Burp Suite. It is a tool capable of capturing web requests and manipulating them.

We can start a new project, and here is the main page

![image.png](images/image%203.png)

Go to the proxy tab first, then open the browser

![image.png](images/image%204.png)

A chromium page should show up, and access the web instance in that page, then go back to Burp Suite to open up the intercept, this will intercept the requests and responses. 

![image.png](images/image%205.png)

After filling the form, we can click submit, and we can see Burp Suite capture a request, click the Forward button to send the request

![image.png](images/image%206.png)

Keep forwarding until we reach the 2FA authentication again

![image.png](images/image%207.png)

If we submit the ‘test’ OTP, we can see the request will look like this

![image.png](images/image%208.png)

What if we remove the entire line `otp=test`, and send the request?

![image.png](images/image%209.png)

<aside>
💡

I did need a few attempts to get the flag, so try few more times if you are doing the same but failed

</aside>

Turns out that if you don’t include the OTP, you can bypass it successfully

Flag: `picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}`
