from typing import TextIO
import numpy as np
import pyowm
import requests
import tensorflow as tf
import pandas
from keras import layers
import keras
from tensorflow import keras
from keras.layers import LSTM, Dense
import pandas as pd
import csv
from bs4 import BeautifulSoup



file: TextIO = open("../File.csv", "r")


def simpleai():
    # die sequentiellen schichten durch die die erstellten gewichten durchlaufen,werden erstellt

    # 1.input
    model = tf.keras.Sequential(
        [
            keras.Input(shape=(1)),
            layers.Dense(units=50),
            layers.Dense(units=20)
        ]
    )

    feature_extractor = keras.Model(
        inputs=model.inputs,
        outputs=[layer.output for layer in model.layers],
    )

    xs = np.array([1, 2, 3, 4], dtype=float)
    ys = np.array([10, 20, 30, 40], dtype=float)

    # model wir compiliert
    model.compile(
        loss='mean_squared_error',
        optimizer='sgd',
        metrics=["accuracy"],
    )

    history = model.fit(xs, ys, epochs=400, validation_split=0.2, batch_size=64)

    # model bewerten

    # model vorhersage
    # next_day_prediction = model.predict(real_data)
    prediction = model.predict([5])
    prediction_2 = np.average(prediction)
    print("Der Durchschnitt aus den Werten beträgt:", prediction_2)
    print("Werte im Einzelnen", prediction)




# simpleai()

def wettererkennung():
    #Erklärung
    print("Folgende Befehle gibt es: Wetter?___Wetter speichern")


    # Wetterdaten
    owm = pyowm.OWM('370de50eda07f962c4c242a9f3910670')
    manager = owm.weather_manager()
    #place = manager.weather_at_place("Berlin,DE")
    #wetter = place.weather


    #file
    file = open("../File.csv", "r")

    # print("Temperatur:", wetter.temperature('celsius'))
    number = 0


    try:
        if(input() == "Wetter?"):
            print("Von wo willst du das Wetter wissen (Stadt und Land bitte)")
            place_2 = manager.weather_at_place(input())
            wetter_2 = place_2.weather
            print("Temperatur:", wetter_2.temperature('celsius'))
        elif(input()== "Wetter speichern"):
            for i in range(2000):
                number += 1
            print("Von wo willst du das Wetter speichern (Stadt und Land bitte)")
            Stadt = input()
            place_3 = manager.weather_at_place(Stadt)
            wetter_daten = place_3.weather
            temperatur = wetter_daten.temperature('celsius')
            Temperatur_Daten = [temperatur]
            with open("../File.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([Stadt] + Temperatur_Daten)
                data = Stadt,Temperatur_Daten
                #df = pd.DataFrame(data)
                # #print(df)

            print("Die aktuellen Daten:", Temperatur_Daten)
    except:
        print("error: Falsche eingabe")
        return















def wetterai():#funtkioniert noch nicht Prototyp
        # Beginn der Vorhersage mithilfe des Neuronalen Netztes

        # Beispiel-Datensatz (Temperatur über die Zeit)
        #temperature_data = np.array(wetter_3.temperature('celsius'))

        # Skalieren der Daten auf den Bereich (0, 1)
        #temperature_data = temperature_data.reshape(0, 1)

        # Erstellen von Eingabe und Ausgabe für das RNN


        #Daten aus Csv datei aufrufen:

        df = pd.read_csv('../File.csv')
        # erstmal rufe ic nur spezifische daten für eine stadt auf später kann der user sich welche aussuchen
        df.loc[1, 'Temperatur (°C)']#München Daten







        X = []
        y = []

        X.append(temperature_data)
        y.append(temperature_data)

        X = np.array(X)
        y = np.array(y)


        # Modell erstellen
        model = tf.keras.Sequential()
        model.add(50, activation='relu', input_shape=(0, 1))
        model.add(Dense(1))


        model.compile(optimizer='adam', loss='mean_squared_error')

        # Modell trainieren
        X_reshaped = X.reshape((X.shape[0], 1, 1))
        model.fit(X_reshaped, y, epochs=100, batch_size=1)

        # Vorhersagen machen
        predictions = model.predict(X_reshaped)

        # Ausgabe der Vorhersagen und echten Werte
        print(predictions)


def test():
    df = pd.read_csv(file)
    firstline = df.head()
    print(firstline)
    x = df [['Stadt']]
    print(x)
    y  = [df.loc[1,'Temperatur (°C)']]
    print(y)
    xs = np.array([1, 2, 3, 4], dtype=float)
    print(xs.ndim)



def webscraping():
    #https://labs.cognitiveclass.ai/v2/tools/jupyterlab?ulid=ulid-7cb60dcb9baa86aadffe516df2758a67ab9d3cfb
    url = 'https://www.spiegel.de'
    data = requests.get(url).text
    soup = BeautifulSoup(data,"html5lib")
    links = soup.find_all('a')
    print(links)





#webscraping()
wettererkennung()
#test()


