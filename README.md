# Basic Server
Basic server to return local JSON with CORS support

### Set up
```
git clone ...
cd basic-server/
python -m venv venv
pip install -r requirements.txt
python serve.py
```

### Serving JSON
Put your json in `data/` and start the server and go to http://127.0.0.1:5000/filename.json and it will return that filename.json
