import sys
import subprocess

import asyncio

import string
import random
import time

from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse

import yt_dlp

app = FastAPI()


async def get_vid(video):
    return subprocess.check_output(["yt-dlp", "--no-warnings", "-f", "best/bestvideo+bestaudio", "--get-url", video])


@app.get("/watch")
async def main(v: str):
    video_str = "https://www.youtube.com/watch?v=" + v
    url = await get_vid(video_str)
    print(url.decode('ascii'))
    return RedirectResponse(url.decode("ascii"), status_code=302)
