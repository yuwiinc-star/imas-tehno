import http.server, base64, os, urllib.parse
OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'src','assets'); os.makedirs(OUT,exist_ok=True)
class H(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self): self.send_response(204); self.send_header('Access-Control-Allow-Origin','*'); self.send_header('Access-Control-Allow-Headers','*'); self.end_headers()
    def do_POST(self):
        q=urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query); name=q.get('name',['x'])[0]
        n=int(self.headers['Content-Length']); data=self.rfile.read(n).decode()
        open(os.path.join(OUT,name),'wb').write(base64.b64decode(data.split(',',1)[1]))
        self.send_response(200); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self,*a): pass
http.server.HTTPServer(('127.0.0.1',8766),H).serve_forever()
