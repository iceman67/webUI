### How to run webUI 

#### 0. make environment 

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```

#### 1. define message
> check $struct\_test.py$  
* make requst a message  and handle a response (from $Server$)in $hello.py$   
```
value = request.args.get('fps') # get the value of parameter fps
header = bytearray(SND_HESDER_SZ)
fmt_str = "<BBBBi"
struct.pack_into(fmt_str, header, 0, 0x01, 0x12, 0xff,0, 5) # offset, v1, v2, v3, v4(sz of payload)
byteObject = bytes(header)
payload  = b'fps' + value.encode()
```

#### 2. run server
> it will be raplaced with $Server$
* it receives the configuration message from webUI and sends the result which is commited by $Server$ via $Logger$
* it is running on 8700 port 
```
python3 webUI_server.py
```

#### 3. run flask
> check $hello.py$
* it is used for delivering a new configureation to a server
```
$ flask --app hello run --host=0.0.0.0
```
#### 4. update CFG  

* connect the following URL (associated with $index.html$ in $templates$ directory) :
```
http://127.0.0.1:5000/
```

* render HTML $hello.html$  with the CFG (fps)  
