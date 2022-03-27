from app import app, db
from flask import redirect, url_for, request, flash, render_template
from form import CarsForm
from models import Cars



@app.route('/', methods=['POST', 'GET'])
def index():
    form = CarsForm()
    # добавление транпортного средства
    if request.method == 'POST' and not request.args.get('id'):
        car_brand = form.car_brand.data
        car_model = form.car_model.data
        category = form.category.data
        car_license_plate = form.car_license_plate.data
        car_type = form.car_type.data
        release_year = form.release_year.data
        trailer = form.trailer.data
        try:
            cars = Cars(car_brand=car_brand,
                        car_model=car_model,
                        category=category,
                        car_license_plate=car_license_plate,
                        car_type=car_type,
                        release_year=release_year,
                        trailer=trailer)
            db.session.add(cars)
            db.session.commit()
            flash(message=f"Транспортное средство успешно добавлено", category='success')
        except:
            print("ошибка")
            flash(message=f"Транспортное средство с государственным номером: {car_license_plate} уже существует", category='danger')
            db.session.rollback()
        return redirect(url_for('index'))


    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    search = request.args.get('search')
    if search:
        cars = Cars.query.filter(Cars.car_brand.contains(search) | Cars.category.contains(search)).order_by(Cars.car_brand.desc())
    else:
        cars = Cars.query.order_by(Cars.car_brand.desc())
    pages = cars.paginate(page=page, per_page=5)

    car_id = request.args.get('id')
    if car_id:
        car_edit = Cars.query.filter_by(id=car_id).first_or_404()
        if request.method == 'POST' and car_id:
            form_edit = CarsForm(formdata=request.form, obj=car_edit)
            form_edit.populate_obj(car_edit)
            db.session.commit()
            return redirect(url_for('index', page = request.args.get('page'), search = request.args.get('search')))
        form_edit = CarsForm(obj=car_edit)
        return render_template('modal.html', car_edit=car_edit, form_edit=form_edit, form=form, pages=pages, search=search)

    return render_template('index.html', form=form, pages=pages, search=search)

@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    Cars.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))
