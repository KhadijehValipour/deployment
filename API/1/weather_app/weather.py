import sys
import requests
import json
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("deployment/API/1/weather_app/Weather.ui", None)
        self.ui.btn_city.clicked.connect(self.weather)
        self.ui.info.triggered.connect(self.info)
        self.ui.exit.triggered.connect(exit)

        self.date = [self.ui.label_date2,self.ui.label_date3, self.ui.label_date4, self.ui.label_date5]
        self.icon = [self.ui.label_Icon2, self.ui.label_Icon3, self.ui.label_Icon4, self.ui.label_Icon5]
        self.temp = [self.ui.label_temp2, self.ui.label_temp3, self.ui.label_temp4, self.ui.label_temp5]


    
    def weather(self):
        city = self.ui.city_text.text()
        response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
        data = json.loads(response.text)
        print(data)
        date_time = data["data"][0]["datetime"]
        normal_date = datetime.strptime(date_time, '%Y-%m-%d')
        date = normal_date.strftime('%A, %d %B')
        description_weather = date["data"][0]["weather"]["description"]
        self.ui.label_city.setText(str(data["city_name"])+" "+str(data["country_code"]))
        self.ui.label_date.setText(date)
        self.ui.label_temp_icon.setText("°C")
        self.ui.label_temp.setText(str(date["data"][0]["temp"]))
        self.ui.description_weather.setText(description_weather)
        self.ui.label_wind.setText(f"Wind: {data['data'][0]['wind_spd']}km/h")

        # forecast weather
    


    def info(self):
        msg = QMessageBox()
        msg.setText("Weather App")
        msg.setIcon(QMessageBox.info)
        msg.setWindowTitle("Information")
        msg.setWindowIcon(QIcon("deployment/API/1/Icon_image/cload.png"))
        msg.exec()





app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()