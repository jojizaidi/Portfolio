import http.server
import ssl

httpd = http.server.HTTPServer(('127.0.0.1', 443), http.server.SimpleHTTPRequestHandler)
ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ctx.load_cert_chain(certfile='./server.pem')
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()