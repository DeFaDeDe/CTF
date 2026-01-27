# get aHead

![image.png](images/image.png)

Here is the challenge page

![image.png](images/image%201.png)

We ca change the color by clicking the button

![image.png](images/image%202.png)

We can take a look at the following code, the following code handles the color changing

```html
...
<style>body {background-color: blue;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
...
```

We can see that changing red uses the GET request, while changing to blue uses the POST request.

What if we try other [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) as well?

We can use curl to send different requests type, and I grep the background to keep track of the changes. For some changes, the background-color is `?`, which means that the request method is not accepted. However , the response of `HEAD` seems weird, as it has no background

```bash
└─$ curl http://wily-courier.picoctf.net:xxxxx/index.php|grep background
...
        <style>body {background-color: red;}</style>

└─$ curl -X POST http://wily-courier.picoctf.net:xxxxx/index.php|grep background                                                                                                                                                           
...
        <style>body {background-color: blue;}</style>

└─$ curl -X PUT http://wily-courier.picoctf.net:xxxxx/index.php|grep background                                                                                                                                                           
...
        <style>body {background-color: ?;}</style>

└─$ curl -X DELETE http://wily-courier.picoctf.net:xxxxx/index.php|grep background                                                                                                                                                         
...
        <style>body {background-color: ?;}</style>

└─$ curl -X HEAD http://wily-courier.picoctf.net:xxxxx/index.php|grep background

└─$ curl -X HEAD http://wily-courier.picoctf.net:xxxxx/index.php
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the way you want. Consider using -I/--head instead.                                                                                                                                                    

```

Use `-v` to view the verbose result, and we will see the flag in the response header

```html

└─$ curl -X HEAD http://wily-courier.picoctf.net:xxxxx/index.php -v                                                                                                                                                                        
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the way you want. Consider using -I/--head instead.
* Host wily-courier.picoctf.net:xxxxx was resolved.
* IPv6: (none)
* IPv4: 18.189.99.27
*   Trying 18.189.99.27:xxxxx...
* Connected to wily-courier.picoctf.net (xx.xxx.xx.xx) port xxxxx
* using HTTP/1.x
> HEAD /index.php HTTP/1.1
> Host: wily-courier.picoctf.net:xxxxx
> User-Agent: curl/8.13.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Tue, 27 Jan 2026 09:36:30 GMT
< Server: Apache/2.4.38 (Debian)
< X-Powered-By: PHP/7.2.34
< flag: picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
< Content-Type: text/html; charset=UTF-8
* no chunk, no close, no size. Assume close to signal end
< 
* shutting down connection #0

```

Flag: `picoCTF{r3j3ct_th3_du4l1ty_8b13f07}`
