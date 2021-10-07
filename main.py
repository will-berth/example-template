from fastapi import FastAPI, Request, Form

import json
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")
datos = {'1': 'Python', '2': 'Java', '3': 'PHP', '4': 'JavaScript'}

@app.get('/')
def raiz(request:Request):
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse('inicio.html', {"request": request, "listado": json_datos})

@app.post('/agregar')
async def agregar(request: Request):
    nuevos_datos = {}
    form_data = await request.form()
    i = 1
    for id in datos:
        nuevos_datos[str(id)] = datos[id]
        i = int(id) + 1
    datos[str(i)] = form_data["lenguaje"]
    sin_codificar = json.dumps(datos)
    json.loads(sin_codificar)
    return RedirectResponse('/', 303)

@app.get('/eliminar/{id}')
async def eliminar(request:Request, id:str):
    del datos[id]
    return RedirectResponse('/', 303)

def TestRemote():
    pass

def TestLocal():
    pass

def TestLocal2():
    pass

def TestLocal3():
    pass
def TestRemote2():
    pass

def TestRemote3():
    pass

def RemoteEdit():
    pass

def RemoteEdit2():
    pass

def LocalEdit():
    pass

def LocalEdit2():
    pass

def RE():
    pass

def RE2():
    pass
