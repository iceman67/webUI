### How to run webUI 

#### 1. make environment 

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```


#### 2. run server
> it will be raplaced with $Server$
* it receives the configuration message from webUI and sends the result which is commited by $Server$ via $Logger$
* it is running on 8700 port 
```
python3 webUI_server.py
```

#### 3. run flask
* it is used for delivering a new configureation to a server
```
$ flask --app hello run --host=0.0.0.0
```


