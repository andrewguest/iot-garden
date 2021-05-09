from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..models import deviceModel


router = APIRouter()


@router.get("/device/all")
async def get_all_devices():
    # TODO: This should be real data pulled from MongoDB
    fake_devices = [
        {
            "name": "Jalapeno Peppers",
            "location": "greenhouse",
            "model": "Raspberry Pi",
        },
        {
            "name": "Broccoli",
            "location": "livingroom",
            "model": "Arduino Uno",
        },
    ]
    return JSONResponse(
        status_code=200,
        content={"devices": fake_devices},
    )


@router.post("/device")
def add_new_device(device: deviceModel.DeviceModel):
    return_data = {
        "message": "Device successfully created",
        "new device data": {
            "ID": str(device.id),
            "Device name": device.name,
            "Device type": device.type,
            "Device description": device.description,
        },
    }
    # TODO: Add this information to MongoDB
    return JSONResponse(status_code=201, content=return_data)
