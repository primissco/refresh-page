### Usage: `python main.py [url] [seconds]` <br/>
Make sure that you have installed the Chrome or Gecko (Firefox) web driver. It is important to add the web driver to PATH. You can change your desired web driver in the code as described there.<br/>
You'll also need to install Selenium: `pip install selenium`.
<br/>
<br/>
### 'Index Error: list index out of range:'
This is because you aren't giving the script any arguments. Try using the script like shown above.
<br/>
### 'Malformed URL: URL constructor: example.com is not a valid URL:'
You have to use `http://` or `https://` in your URL input. (e.g. `python main.py https://example.com 30`)
