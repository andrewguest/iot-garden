from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests


router = APIRouter()


# Check the 'andrewguest/iot-garden' repo for a newer release and alert the
#   user if there is a new version.
@router.get("/system/update")
def check_for_new_version():
    gh_repo = requests.get('https://api.github.com/repos/andrewguest/iot-garden/releases/latest')

    if gh_repo.status_code == 200:
        message = {
            'Newest version': gh_repo.json()['tag_name'],
            'Description': gh_repo.json()['name']
        }
        return JSONResponse(status_code=200, content=message)

    elif gh_repo.status_code == 403:
        message = {
            'Error': gh_repo.json()['message']
        }
        return JSONResponse(status_code=403, content=message)
