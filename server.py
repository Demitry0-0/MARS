from flask import Flask, url_for, request, render_template, redirect, json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import random
import os


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class DostupForm(FlaskForm):
    id_astronaft = IntegerField('id астронавта')
    password_astronaft = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = IntegerField('id капитана')
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if sex == 'male':
        color = random.choice(['man1.jpg', 'man2.jpg', 'man3.jpg'])
    else:
        color = random.choice(['girl1.jpg', 'girl2.jpg', 'girl3.jpg'])
    if age < 21:
        mars = 'marsianin1.jpg'
    else:
        mars = 'marsianin2.jpg'
    return render_template('table.html', color=color, mars=mars)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DostupForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
def hack():
    return 'Миссия Колонизация Марса'


@app.route('/distribution')
def distribution():
    lst = ['Vorobei', 'John', 'Boroda', 'Terner', 'VIll']
    return render_template('distribution.html', lst=lst)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.',
           'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.',
           'И начнем с Марса!',
           'Присоединяйся! С нами БОГ!!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                      < img
                        src = "https://ic.pics.livejournal.com/serzigzagser/74708980/1647453/1647453_original.jpg"
                        alt = "Сдесь должен быть сладенький марс" >
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name2" placeholder="Введите Фамилию" name="input_name2">
                                    <input type="text" class="form-control" id="name1" placeholder="Введите имя" name="input_name1">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Высшее полное</option>
                                          <option>Высшее неполное</option>
                                          <option>Срднее</option>
                                          <option>НЕТУ</option>
                                          <option>ДИВАННОЕ ОБРАЗОВАНИЕ</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Выбор основной профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="male" value="инженер-исследователь" checked>
                                          <label class="form-check-label" for="male">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="пилот">
                                          <label class="form-check-label" for="female">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="строитель">
                                          <label class="form-check-label" for="female">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="экзобиолог">
                                          <label class="form-check-label" for="female">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="врач">
                                          <label class="form-check-label" for="female">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="инженер по терраформированию">
                                          <label class="form-check-label" for="female">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="климатолог">
                                          <label class="form-check-label" for="female">
                                            климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="sex" id="female" value="специалист">
                                          <label class="form-check-label" for="female">
                                            специалист
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Мотивация</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Варианты выбора</title>
    <link rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
    crossorigin="anonymous">
</head>
<body>
    <h1>Моё предложение: {planet_name.title()}</h1>
    <div class="alert alert-light" role="alert">
    <h3>Эта планета;</h3>
    </div>                             
    <div class="alert alert-success" role="alert">
    <h3>На ней может быть много ресурсов;</h3>
    </div>
    <div class="alert alert-secondary" role="alert">
    <h3>На ней может быть вода и атмосфера;</h3>
    </div>
    <div class="alert alert-warning" role="alert">
    <h3>На ней может быть небольшое магнитное поле;</h3>
    </div>
    <div class="alert alert-danger" role="alert">
    <h3>Наконец, она просто великолепна!</h3>
    </div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}:</h3>
                        <div class="alert alert-success" role="alert">
                        <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                        </div>
                        <h3>составляет {rating}!</h3>
                        <div class="alert alert-warning" role="alert">
                        <h3>Желаем удачи!</h3>
                        </div>
                    </body>
                    </html>"""


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename:
            f.save(f'static/img/galery/mars{len(os.listdir("static/img/galery"))}.jpg')
    s = ''
    for i, file in enumerate(os.listdir('static\\img\\galery')):
        s += f'''
            <div class="carousel-item {'active' if not i else ''}">
                <img class="d-block w-100" src="{url_for('static', filename='img/galery/' + file)}">
            </div>'''
    return """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Пейзажи Марса</title>
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="static/css/style.css">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>
</head>
<body>
<form method="post" class="login_form" enctype="multipart/form-data">

    <center><h1>Пейзажи Марса</h1></center>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
        """ + s + """
            
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls" role="button"
           data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls" role="button"
           data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    <h1>Загрузим файл</h1>
    <div class="form-group">
        <label for="photo">Выберите файл</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>"""


# Возможо отличное решение другой задачи
'''@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename:
            f.save(f'static/img/galery/mars{len(os.listdir("static/img/galery"))}.jpg')
    s = ''
    for file in os.listdir('static\\img\\galery'):
        s += f''' + '''
            <div class="carousel-item active">
                <img class="d-block w-100" src="{url_for('static', filename='img/galery/' + file)}">
            </div>''' + '''
    print(s)
    # return render_template('galery.html')
    return """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Пейзажи Марса</title>
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="static/css/style.css">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>
</head>
<body>
<form method="post" class="login_form" enctype="multipart/form-data">

    <center><h1>Пейзажи Марса</h1></center>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
        """ + s + """
            
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls" role="button"
           data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls" role="button"
           data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    <h1>Загрузим файл</h1>
    <div class="form-group">
        <label for="photo">Выберите файл</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>"""'''


@app.route('/carousel')
def carousel():
    return """<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <title>Пейзажи Марса</title>
                        <link rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
    crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                      </head>
                      <body>
                      <center><h1>Пейзажи Марса</h1></center>
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="static/img/mars.jpg" alt="Первый слайд">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="static/img/mars1.jpg" alt="Второй слайд">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="static/img/mars2.jpg" alt="Третий слайд">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
                      </body>
                    </html>"""


def new():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                            <h1>Загрузим файл</h1>
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('load_photo.html', flag=0)
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename:
            if 'photo1.jpg' in os.listdir('static\\img'):
                f.save('static/img/photo.jpg')
                os.remove('static/img/photo1.jpg')
                return render_template('load_photo.html', flag=1, photo='photo.jpg')
            elif 'photo.jpg' in os.listdir('static\\img'):
                f.save('static/img/photo1.jpg')
                os.remove('static/img/photo.jpg')
                return render_template('load_photo.html', flag=1, photo='photo1.jpg')
            else:
                f.save('static/img/photo.jpg')
                return render_template('load_photo.html', flag=1, photo='photo.jpg')

    return render_template('load_photo.html', flag=0)


"""def new():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                            <h1>Загрузим файл</h1>
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return new()
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename:
            f.save('static/img/photo.jpg')
        else:
            return new()
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                     integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                     crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Пример загрузки файла</title>
                  </head>
                  <body>
                    <form method="post" class="login_form" enctype="multipart/form-data">
                    <h1>Загрузим файл</h1>
                       <div class="form-group">
                            <label for="photo">Выберите файл</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <img src='static/img/photo.jpg' alt=''>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                  </body>
                </html>'''

"""


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', name='Инженерные тренажеры', photo='it.png')
    else:
        return render_template('training.html', name='Научные симуляторы', photo='science.png')


@app.route('/list_prof')
@app.route('/list_prof/<tp>')
def list_prof(tp=False):
    if tp:
        lst = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
               'врач', 'инженер по терраформированию', 'климотолог',
               'специолист по радиационной защите', 'астрогеолог', 'гляцеолог',
               'инженер жизниобеспечиния', 'метеоролог', 'оператор марсохода',
               'киберинженер', 'штурман', 'пилот дронов']
        if tp == 'ol':
            return render_template('list_prof.html', tp='ol', lst=lst)
        elif tp == 'ul':
            return render_template('list_prof.html', tp='ul', lst=lst)
    return 'Неверный параметр.'


@app.route('/answer')
def answer():
    item = {'title': 'Анкета',
            'surname': 'Wathy',
            'name': 'Mark',
            'education': 'выше среднего',
            'profession': 'штурман марсохода',
            'sex': 'male',
            'motivation': 'Всегда мечтал застрять на марсе',
            'ready': 'True'}
    return render_template('auto_answer.html', item=item, title=item['title'])


@app.route('/auto_answer')
def auto_answer():
    item = {'title': 'Анкета',
            'surname': 'Wathy',
            'name': 'Mark',
            'education': 'выше среднего',
            'profession': 'штурман марсохода',
            'sex': 'male',
            'motivation': 'Всегда мечтал застрять на марсе',
            'ready': 'True'}
    return render_template('auto_answer.html', item=item, title=item['title'])


@app.route('/member')
def member():
    with open("templates\\crew.json", "rt", encoding="utf8") as f:
        crew_list = json.loads(f.read())
    item = crew_list['crew'][random.choice([i for i in crew_list['crew'].keys()])]
    print(sorted(crew_list['professsion']))
    return render_template('member.html', item=item,
                           profession=', '.join(sorted(crew_list['professsion'])))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
