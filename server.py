from flask import Flask, url_for, request
from PIL import Image

app = Flask(__name__)


@app.route('/')
def hack():
    return 'Миссия Колонизация Марса'


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


@app.route('/sample_file_upload', methods=['POST', 'GET', 'PATCH'])
def sample_file_upload():
    print(request.files)
    if request.files:
        file = f'<img src={url_for("static", filename="photo.jpg")} alt="Такой фотки нет">'
        # Image.open(request.files['file'].read()).save('photo.jpg')
    else:
        file = ''
    print(request.files.get('file'))

    print(request.method)
    if request.method == 'PATCH':
        return 'dsfdfsfdsdf'
    elif request.method == 'GET':
        print(request.files)
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
                            <h1>Загрузим файл</h1>
                            <form method="put" enctype="multipart/form-data">
                               <div class="form-group" method="put">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" method="put" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                                {file}
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(dir(request.files['file']))
        print(request.files['file'].filename)
        print(request.files)

        # print(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
