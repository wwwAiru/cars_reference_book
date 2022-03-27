from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
from wtforms.validators import InputRequired


class CarsForm(FlaskForm):
    car_brand = StringField('Марка автомобиля: ', validators=[InputRequired()])
    car_model = StringField('Модель: ', validators=[InputRequired()])
    category = StringField('Категория транспортного средства: ', validators=[InputRequired()])
    car_license_plate = StringField('Государственный номер: ', validators=[InputRequired()])
    car_type = StringField('Тип транспортного средства: ', validators=[InputRequired()])
    release_year = DateField('Год выпуска: ', validators=[InputRequired()])
    trailer = SelectField('Наличие прицепа: ', choices=[('Нет', 'Нет'), ('Да', 'Да')])
