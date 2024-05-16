import sys
import json
import requests

from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("weather_app\Weather.ui")
        self.ui.show()
        self.ui.btn_city.clicked.connect(self.weather)
        self.ui.info.triggered.connect(self.info)
        self.ui.exit.triggered.connect(exit)

        self.label_date = [self.ui.label_date1,self.ui.label_date2,self.ui.label_date3, self.ui.label_date4]
        self.icon = [self.ui.label_Icon1,self.ui.label_Icon2, self.ui.label_Icon3, self.ui.label_Icon4]
        self.temp = [self.ui.label_temp1,self.ui.label_temp2, self.ui.label_temp3, self.ui.label_temp4]


    
    def weather(self):
        
        city = self.ui.city_text.text()
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={city}&key=2effe1f9f06e40cc8ef77eb5be376022"
        response = requests.request("GET", url)
        jsondata = json.loads(response.text)
        date_time = jsondata["data"][0]["datetime"]
        normal_date = datetime.strptime(date_time, '%Y-%m-%d')
        date = normal_date.strftime('%A, %d %B')
        description_weather = jsondata["data"][0]["weather"]["description"]
        self.ui.label_city.setText(str(jsondata["city_name"])+" "+str(jsondata["country_code"]))
        self.ui.label_date.setText(date)
        self.ui.label_temp_icon.setText("°C")
        self.ui.label_icon_high.setText("°C")
        self.ui.label_icon_low.setText("°C")
        self.ui.label_description.setText(description_weather)
        self.ui.label_wind.setText(f"Wind: {jsondata['data'][0]['wind_spd']}km/h")
        self.ui.label_max_temp.setText(str(jsondata["data"][0]["app_max_temp"]))
        self.ui.label_min_temp.setText(str(jsondata["data"][0]["app_min_temp"]))
        self.ui.label_temperature.setText(str(jsondata["data"][0]["temp"]))



        if "Clear" in description_weather:
            img = "img\clear.png"
        elif "Partly cloudy" in description_weather:
            img = "img\partlyـcloudy.png"
        elif "Few clouds" in description_weather:
            img = "img\cloud.png"
        elif "Scattered" in description_weather:
            img = "img\partlyـcloudy.png"
        elif "Light rain" in description_weather:
            img = "img\light_rain.png"
        elif "Sunny" in description_weather:
            img = "img\sunny.png"
        elif "Light rain shower" in description_weather:
            img = "img\Light_rain_shower.png"
        elif "Mist, rain" in description_weather or "Rain, mist" in description_weather:
            img = "img\mist_rain.png"
        elif "snow" in description_weather:
            img = "img\snow.png"
        elif "Mix snow/rain" in description_weather:
            img = "img/rainy.png"
        elif "rain" in description_weather:
            img = "img\Rainwiththunder.png"
        elif "Wind" in description_weather:
            img = "img\wind.png"
        elif "Patchy rain nearby" in description_weather:
            img = "img\windy_rain.png"
        elif "Thunderst" in  description_weather:
            img = "img/thunderst.png"
        elif "Overcast clouds" in  description_weather:
            img = "img\cloud.png"
        else :
            img = "img/fog_night.png"
        pixmap = QPixmap(img)
        self.ui.label_Icon.setPixmap(pixmap)

        

        # forecast weather
        for W in range(4):
            date_time = jsondata["data"][W+1]["datetime"]
            normal_date = datetime.strptime(date_time, '%Y-%m-%d')
            date = normal_date.strftime('%A')
            self.label_date[W].setText(date[:3]) # سه کاراکتر از روز های هفته رو نمایش بده
            description_weather = jsondata["data"][W+1]["weather"]["description"]



            if "Clear" in description_weather:
                img = "resized_photos\clear.png"
            elif "Partly cloudy" in description_weather:
                img = "resized_photos\partlyـcloudy.png"
            elif "Few clouds" in description_weather:
                img = "resized_photos\cloud.png"
            elif "Sunny" in description_weather:
                img = "resized_photos\sunny.png"
            elif "Light rain shower" in description_weather:
                img = "resized_photos\Light_rain_shower.png"
            elif "Mist, rain" in description_weather or "Rain, mist" in description_weather:
                img = "resized_photos\mist_rain.png"
            elif "Scattered" in description_weather:
                img = "resized_photos\partlyـcloudy.png"
            elif "snow" in description_weather:
                img = "resized_photos\snow.png"
            elif "Mix snow/rain" in description_weather:
                img = "resized_photos/rainy.png"
            elif "rain" in description_weather:
                img = "resized_photos\Rainwiththunder.png"
            elif "Wind" in description_weather:
                img = "resized_photos\wind.png"
            elif "Patchy rain nearby" in description_weather:
                img = "resized_photos\windy_rain.png"
            elif "Thunderst" in  description_weather:
                img = "resized_photos/thunderst.png"
            elif "Overcast clouds" in  description_weather:
                img = "resized_photos\cloud.png"
            else :
                img = "resized_photos/fog_night.png"
            pixmap = QPixmap(img)
            self.icon[W].setPixmap(pixmap)
            self.temp[W].setText(str(jsondata["data"][W+1]["temp"])+"°C")


    def info(self):
        msg = QMessageBox()
        msg.setText("Weather App")
        msg.setIcon(QMessageBox.information)
        msg.setWindowTitle("Information")
        msg.setWindowIcon(QIcon("partlyـcloudy.png"))
        msg.exec()



app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()



