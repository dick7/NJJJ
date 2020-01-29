from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # return 'Hello World! Another time!'
    user = {'nickname': 'Master'}  # fake user
    # return '''
    # <html>
    #   <head>
    #     <title>Home Page</title>
    #   </head>
    #   <body>
    #     <h1>Hello, ''' + user['nickname'] + '''</h1>
    #   </body>
    # </html>
    # '''

    # return render_template("index.html",title='front page',
    #                        user=user)

    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Zhang San'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Li Si'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                            # title='Home',
                            user=user,
                            posts=posts)