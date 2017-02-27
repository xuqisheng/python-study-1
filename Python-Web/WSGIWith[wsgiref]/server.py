# server.py
# import from wsgiref:
from wsgiref.simple_server import make_server
# import our application
from hello import application

# create server
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# start server
httpd.serve_forever()
