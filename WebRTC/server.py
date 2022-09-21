import argparse
import logging
import asyncio
import os
import uuid
import json
import platform

from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer, MediaRelay

from pyngrok import ngrok

token = "2EFlxQQDpreqVGMuQVTtTepMzHB_7Px3VmMDjcQxgLoDH7Ync"
logger = logging.getLogger("pc")
pcs = set()
ROOT = os.path.dirname(__file__)
relays = None
webcam = None

class parser:

    args = None

    def set_logging_level(self):

        if args.verbose:
            logging.basicConfig(level = logging.DEBUG)
            print("Debuge MODE")
        else:
            logging.basicConfig(level = logging.INFO)
            print("INFO MODE")

    def set_parser(self):

        global args

        parser = argparse.ArgumentParser(
            description = "Webcam using WebRTC with python-lib aioRTC"
        )

        parser.add_argument(
            "--host", "-IP", default = "127.0.0.1", help = "Host IP for HTTP Connection"
        )

        parser.add_argument(
            "--port", type = int, default = 8080, help = "post number for server"
        )

        parser.add_argument("--verbose", "-v", action = "count")

        args = parser.parse_args()

        self.set_logging_level()

def create_local_tracks():
    global relays, webcam

    options = {"framerate": "30", "video_size": "640x480"}
    if relays is None:
        if platform.system() == "Darwin":
            webcam = MediaPlayer(
                "default:none", format="avfoundation", options=options
            )
        elif platform.system() == "Windows":
            webcam = MediaPlayer(
                "video=USB2.0 HD UVC WebCam", format="dshow", options=options
            )
        else:
            webcam = MediaPlayer("/dev/video0", format="v4l2", options=options)
        relays = MediaRelay()
    return relays.subscribe(webcam.video)

async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()

async def index(request):
    content = open(os.path.join(ROOT, "index.html"), "r").read()
    return web.Response(content_type="text/html", text=content)

async def javascript(request):
    content = open(os.path.join(ROOT, "client.js"), "r").read()
    return web.Response(content_type="application/javascript", text=content)

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])
    
    pc = RTCPeerConnection()
    pc_id = "PeerConnection(%s)" % uuid.uuid4()
    pcs.add(pc)

    def log_info(msg, *args):
        logger.info(pc_id + " " + msg, *args)

    log_info("Created for %s", request.remote)

    video = create_local_tracks()
    pc.addTrack(video)

     # handle offer
    await pc.setRemoteDescription(offer)


    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )

def set_page(app0):

    app0.on_shutdown.append(on_shutdown)
    app0.router.add_get("/", index)
    app0.router.add_get("/client.js", javascript)
    app0.router.add_post("/offer", offer)

    return app0

def get_ngrok_URL():

    ngrok.set_auth_token(token)
    http_tunnel = ngrok.connect(8080)
    print("-------------------->" + http_tunnel.public_url)

    return http_tunnel.public_url

def open_webcam():
    #setting INFO MODE
    parser_setting = parser()
    parser_setting.set_parser()

    #setting website response
    app = web.Application()
    app = set_page(app)

    #input argument
    web.run_app(
        app, access_log=None, host=args.host, port=args.port, ssl_context=None
    )

if __name__ == "__main__":

    open_webcam()




    
