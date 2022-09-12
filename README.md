### how to run webUI 

####  make environment 

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```


####  run server
*  it is running on 8700 port
```
python3 webUI_server.py
```

####  run flask
* it is used for delivering a new configureation to a server
```
$ flask --app hello run --host=0.0.0.0
```


