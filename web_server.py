# plugins/web_server.py

from aiohttp import web

async def health(request):
    return web.Response(text="OK", status=200)

async def web_server():
    app = web.Application()
    app.router.add_get("/health", health)
    app.router.add_get("/healthz", health)
    app.router.add_get("/_health", health)
    return app
