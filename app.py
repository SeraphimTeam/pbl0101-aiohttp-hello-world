import os
from datetime import datetime

from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

NIM = os.getenv("NIM", "")
NAMA = os.getenv("NAMA", "")


async def hello(request):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""
<h1>HELLO WORLD</h1>
<p>#PBW3B1PBL0101</p>
<p>{NIM}</p>
<p>{NAMA}</p>
<p>Framework Pilihan -> Python [12] - AIOHTTP</p>
<p>TIME : {waktu}</p>
"""
    return web.Response(text=html, content_type="text/html")


app = web.Application()
app.add_routes([web.get("/", hello)])

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8080)
