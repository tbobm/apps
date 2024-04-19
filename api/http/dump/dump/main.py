from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.api_route("/{full_path:path}", methods=["HEAD", "GET", "POST", "DELETE", "PUT"])
async def read_root(request: Request, full_path: str):
    response = {
        "path": full_path,
        "method": request.method,
    }
    response['headers'] = request.headers
    _json = await request.json()
    if _json is not None:
        response['json'] = _json
    _form = await request.form()
    if _form is not None:
        response['form'] = _form
    return response
