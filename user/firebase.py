import pyrebase
import firebase
config = {
  'apiKey': "AIzaSyDZ-bjG_7eeSt6JddoSoJFiuZMilL20ULg",
  'authDomain': "zeonshop-aa50d.firebaseapp.com",
  'databaseURL': "https://zeonshop-aa50d-default-rtdb.firebaseio.com",
  'projectId': "zeonshop-aa50d",
  'storageBucket': "zeonshop-aa50d.appspot.com",
  'messagingSenderId': "463028134742",
  'appId': "1:463028134742:web:4fef352a4d4bac8e89acf7",
  'measurementId': "G-X0T3V668E5"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'anvarashyrbekov147as@mail.ru'
password = ''

res = auth.create_user_with_email_and_password(email, password)

# test = auth.sign_in_with_email_and_password(email, password)

print(res)
# print(test)
