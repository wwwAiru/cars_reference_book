from app import db


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_brand = db.Column(db.String(100))   # марка автомобиля
    car_model = db.Column(db.String(100))   # модель
    category = db.Column(db.String(100))    # категория ТС
    car_license_plate = db.Column(db.String(20), unique=True)   # государственный номер
    car_type = db.Column(db.String(100))    # тип ТС
    release_year = db.Column(db.DateTime())    # год выпуска
    trailer = db.Column(db.String(5))    # наличие прицепа

