#!/usr/bin/env python3
"""MAKER LAB automatic image-folder server. Python 3 only."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json, os

ROOT = Path(__file__).resolve().parent
ALLOWED = {'.png','.jpg','.jpeg','.webp','.gif','.avif'}
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT),**kw)
    def do_GET(self):
        if self.path.split('?')[0] == '/gallery-manifest.json':
            folders=[ROOT/'gallery', ROOT/'galley']
            images=sorted([{'file':p.relative_to(folder).as_posix(),'folder':folder.name} for folder in folders for p in folder.rglob('*') if p.is_file() and p.suffix.lower() in ALLOWED and not p.name.startswith('.')],key=lambda v:(v['folder'],v['file'].casefold()))
            data=json.dumps({'images':images},ensure_ascii=False).encode('utf-8')
            self.send_response(200);self.send_header('Content-Type','application/json; charset=utf-8')
            self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        elif self.path.split('?')[0] == '/music-manifest.json':
            folder=ROOT/'music'
            allowed_music={'.mp3','.wav','.ogg','.m4a','.aac'}
            tracks=sorted([v.relative_to(folder).as_posix() for v in folder.rglob('*') if v.is_file() and v.suffix.lower() in allowed_music and not v.name.startswith('.')],key=str.casefold)
            data=json.dumps({'tracks':tracks},ensure_ascii=False).encode('utf-8')
            self.send_response(200);self.send_header('Content-Type','application/json; charset=utf-8')
            self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        elif self.path.split('?')[0] == '/images-manifest.json':
            folder=ROOT/'images'
            images=sorted([p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and p.suffix.lower() in ALLOWED and not p.name.startswith('.')])
            data=json.dumps({'images':images},ensure_ascii=False).encode('utf-8')
            self.send_response(200);self.send_header('Content-Type','application/json; charset=utf-8')
            self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        else: super().do_GET()

if __name__=='__main__':
    port=int(os.environ.get('PORT','8000'))
    print(f'홈페이지 주소: http://localhost:{port}  (종료: Ctrl+C)',flush=True)
    ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
