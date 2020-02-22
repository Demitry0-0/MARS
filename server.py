from flask import Flask, url_for

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
           'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <heh1><h1>Жди нас, Марс!</h1></heh1>
                        <img src="https://ic.pics.livejournal.com/serzigzagser/74708980/1647453/1647453_original.jpg" alt="Сдесь должен быть сладенький марс">
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return image_mars() + bootstrap()


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <div class="alert alert-primary" role="alert">
                      <h2>На марсе не хватает налогоплательщиков.
                      </br>Больше налогов, больше счастья.</br>
                      Налог не платил, жизни не видал.</h2>
                      </br>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
