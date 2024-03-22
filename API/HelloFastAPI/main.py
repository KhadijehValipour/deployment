import cv2
import numpy as np
import io
from typing import Union
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
 
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/salam")
def test():
    return "علیک سلام"

@app.get("/salam/{firstname}/{lastname}")
def test_2(firstname: str, lastname :str):
    return "علیک سلام"+ " "+ firstname + " "+ lastname +" "+ "عزیز" 


@app.get("/salam/{firstname}")
def test_3(firstname: str, lastname :str = "حسینی"):
    return "علیک سلام"+ " "+ firstname + " "+ lastname +" "+ "عزیز" 


@app.get("/tv_channel/{name}")
def test_4(name: Union[str, int]):
    return {"channel": name}



@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id": item_id,  "q":q}


@app.get("/create_image/{red}/{green}/{blue}")
def create_image(red: int , green: int , blue: int):
    if 0 <= red <= 255  and   0 <= green <= 255  and  0 <= blue <= 255 :
        image = np.zeros((300, 200, 3), dtype=np.uint8)                    # یه عکس خالی ساختم
        image[:, :] = (red, green, blue)                                   # پیکسل هاشو رنگ آمیزی کردم
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)                     # بخاطر جابهجا بودن کانال قرمز و آبی 
        #cv2.imwrite("test.jpg", image)                                    # تست کردم ببینم عکس درست ساخته شده
        _, encoded_image = cv2.imencode(".png", image)                     # آندرلاین اولی که مقدار بولین رو نشون میده اینجا به این معنی هست که من متغیری برای این مقدار نمیخوام اختصاص بدم تا حافظه کمتری اشغال بشه
                                                                           # عکس در این حالت میخواد به کاربر نمایش داده شه ولی نوعش نامپای هست و در تبدیل به جیسون مشکل داره من انکد میکنم عکس رو
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")  # توسط تابع بایت هاشو دارم ارسال میکنم
    

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Numbers must be between 0 to 255")