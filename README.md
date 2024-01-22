Make sure you have xclip installed on the host machine

```
git clone https://github.com/palash-gupta/MobileToDesktopClipboard.git
cd MobileToDesktopClipboard
pip install -r requirements.txt
python app.py --host=0.0.0.0 --port=80
```

- An IP address in the form of 192.168.x.x shows up
- On a different device connected to common network, enter the IP address in a browser.
- Enter any text into the text field and enter the appropriate password 
- On the host GNU/Linux machine (with xclip installed) the clipboard will be populated with the text.
