# Spookifier

![image.png](images/image.png)

## Source Code analysis

After we unzip the source code, we will see the following files

```bash
.
├── build-docker.sh
├── challenge
│   ├── application
│   │   ├── blueprints
│   │   │   └── routes.py
│   │   ├── main.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   ├── index.css
│   │   │   │   └── nes.css
│   │   │   └── images
│   │   │       └── vamp.png
│   │   ├── templates
│   │   │   └── index.html
│   │   └── util.py
│   └── run.py
├── config
│   └── supervisord.conf
├── Dockerfile
└── flag.txt
```

We can inspect the `Dockerfile` first

```docker
# Create the basefile based on the python:3.8-alpine image
FROM python:3.8-alpine
# Update gcc
RUN apk add --no-cache --update supervisor gcc
# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask==2.0.0 mako flask_mako Werkzeug==2.0.0

# Copy flag to root!
COPY flag.txt /flag.txt

# Setup app(-p flag will create parent directories if needed)
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# start supervisord
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
```

We can see that the `flag.txt` is moved to root(`/`) and there are some dependencies updated or upgraded

After that, we navigate to the `main.py`, which review little info

```python
from flask import Flask, jsonify
from application.blueprints.routes import web
from flask_mako import MakoTemplates
# Create a Flask Object
app = Flask(__name__)
# Use the Mako template
MakoTemplates(app)

def response(message):
    return jsonify({'message': message})
# Register blueprint(basically actions that will be taken)
app.register_blueprint(web, url_prefix='/')
# Error Handling
@app.errorhandler(404)
def not_found(error):
    return response('404 Not Found'), 404

@app.errorhandler(403)
def forbidden(error):
    return response('403 Forbidden'), 403

@app.errorhandler(400)
def bad_request(error):
    return response('400 Bad Request'), 400
```

We can observe that:

1. Uses Mako 
2. Returns JSON responses for error pages

According to [Mako](https://www.makotemplates.org/)

> Mako is a template library written in Python. It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance. Mako's syntax and API borrows from the best ideas of many others, including **Django and Jinja2** templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded Python (i.e. Python Server Page) language, which refines the familiar ideas of componentized layout and inheritance to produce one of the most straightforward and flexible models available, while also maintaining close ties to Python calling and scoping semantics.
> 

To know what the [blueprint looks](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) like, we can read the `route.py`

```python
from flask import Blueprint, request
from flask_mako import render_template
from application.util import spookify
# Define the blueprint
web = Blueprint('web', __name__)

@web.route('/')
def index():
    # Get the text value
    text = request.args.get('text')
    if(text):
        # Covert the test using the spookify function
        converted = spookify(text)
        # Reder the output to the index page
        return render_template('index.html',output=converted)
    
    return render_template('index.html',output='')
```

We can see that this code will:

- Get the text argument
    - If it is not empty, convert the text and render using [render_template](https://flask-mako.readthedocs.io/en/latest/#rendering) with the converted output
        
        > Rendering Mako templates sends the same template_rendered signal as **Jinja2** templates. Additionally, Mako templates receive the same context as **Jinja2** templates.
        > 
    - Else, render the index page with an empty output

And Scanning the `util.py` will do us no good, it is just changing the fonts.

```python
# Fonts here
.
.
.
def generate_render(converted_fonts):
	result = '''
		<tr>
			<td>{0}</td>
        </tr>
        
		<tr>
        	<td>{1}</td>
        </tr>
        
		<tr>
        	<td>{2}</td>
        </tr>
        
		<tr>
        	<td>{3}</td>
        </tr>

	'''.format(*converted_fonts)
	
	return Template(result).render()

def change_font(text_list):
	text_list = [*text_list]
	current_font = []
	all_fonts = []
	
	add_font_to_list = lambda text,font_type : (
		[current_font.append(globals()[font_type].get(i, ' ')) for i in text], all_fonts.append(''.join(current_font)), current_font.clear()
		) and None

	add_font_to_list(text_list, 'font1')
	add_font_to_list(text_list, 'font2')
	add_font_to_list(text_list, 'font3')
	add_font_to_list(text_list, 'font4')

	return all_fonts

def spookify(text):
	converted_fonts = change_font(text_list=text)

	return generate_render(converted_fonts=converted_fonts)
```

## Webpage Exploitation

Inputting the ‘test’ word will return us ‘test’ in different spooky fonts.

![image.png](images/image%201.png)

So after we submit the word ‘test’, it will send a post request to the root(`/`).

```html
<form action="/">
            <input id="input" name="text" type="text" value="">
            <button id="go" type="submit">Spookify</button>
</form>
```

But can we manipulate the input and make the output show us the flag in `/root.txt`?

If you notice the quotes I included from the documents, you will see that templates like ‘Jinja’ and ‘Django’ appear frequently and are vulnerable to an attack called Server-Side Template Injection (SSTI). In fact, you should be able to find this type of attack if we search for ‘python template exploit’. According to [PortSwigger](https://portswigger.net/web-security/server-side-template-injection),

> Server-side template injection is when an attacker is able to use **native template syntax** to inject a malicious payload into a template, which is then **executed server-side**.
> 
> 
> Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is **concatenated directly** into a template, rather than passed in as data. This allows attackers to inject arbitrary template directives in order to manipulate the template engine, often enabling them to take complete control of the server. As the name suggests, server-side template injection payloads are delivered and evaluated server-side, potentially making them much more dangerous than a typical client-side template injection.
> 

We can find the payloads and the attacker techniques in [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md#mako), We can see all the payloads are wrapped in `${<payload>}`, so to test whether if it is vulnerable to SSTI, we should try to use `${3*3}` to see its result

![image.png](images/image%202.png)

We can find that the result is `9`, instead of return `{3*3}` directly, which means that it is vulnerable to SSTI

<aside>
📢

I urge you to read the Identify session in the [PortSwigger](https://portswigger.net/web-security/server-side-template-injection#Identify) article. That section explains how different templates will respond to the payload

</aside>

Refer to [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md#mako), we can see that the first payload is the following:

`${self.module.cache.util.os.system("id")}`

However, we do want to see the value(the flag), so we should use `popen`. Here is a great [article]([https://www.tutorialspoint.com/python/os_popen.htm](https://www.tutorialspoint.com/python/os_popen.htm)) about it

To implement, simply include the command inside `popen` and add `.read()` so that we can read the result. With this, the full command will be `${self.module.cache.util.os.popen('cat /flag.txt').read()}`

![image.png](images/image%203.png)

Flag: `HTB{t3mpl4t3_1nj3ct10n_C4n_3x1st5_4nywh343!!}`
