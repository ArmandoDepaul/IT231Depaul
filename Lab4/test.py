from wsgiref.simple_server import make_server

from sqlitezero import select_artists 

with make_server('', 8000, select_artists) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()