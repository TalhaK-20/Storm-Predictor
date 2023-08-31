import pandas as p
import numpy as n
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def random_data_CSV():
    n.random.seed(42)
    num_samples = 100

    temperature = n.random.randint(20, 35, num_samples)
    humidity = n.random.randint(40, 80, num_samples)
    atmospheric_pressure = n.random.randint(980, 1050, num_samples)

    storm = n.random.choice([0, 1], num_samples, p=[0.7, 0.3])
    data = p.DataFrame({'temperature': temperature, 'humidity': humidity, 'atmospheric_pressure': atmospheric_pressure,
                        'storm': storm})

    data.to_csv('storm_random_data.csv', index=False)


def Prediction():
    data = p.read_csv('storm_random_data.csv')
    X = data[['temperature', 'humidity', 'atmospheric_pressure']]
    y = data['storm']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    temp = int(input("Enter the value of temperature in Celsius = "))
    humid = int(input("Enter the value of humidity = "))
    atmospheric_p = int(input("Enter the value of atmospheric pressure = "))

    new_data = p.DataFrame({'temperature': [temp], 'humidity': [humid], 'atmospheric_pressure': [atmospheric_p]})
    predicted_storm = model.predict(new_data)
    print(
        f'Will there be a storm for temperature = {new_data["temperature"].iloc[0]}, '
        f'humidity = {new_data["humidity"].iloc[0]} and '
        f'atmospheric_pressure = {new_data["atmospheric_pressure"].iloc[0]}'
        f' ?'f'{" Yes" if predicted_storm[0] else " No"}')


def repeat():
    while True:
        print("Welcome to the Simple Storm Prediction Software")
        print("        Developed by Talha Khalid\n")
        print("** Important Note ** \nFor making this software, Talha Khalid has used "
              "random generated data for temperature, humidity and atmospheric pressure"
              " to train the model.")

        Prediction()

        user = input("Do you want to use it again. Press Y/N = ").lower()
        print("\n")
        if user != 'y' and user == "n":
            print("Thanks for using. Have a lovely day :)")
            break

        elif user != 'n' and user != 'y':
            print("You neither press Y nor N so I am Shutting Down the software..."
                  " Thanks for using. Have a lovely day :)")
            break


repeat()
