# import from the init.py within the package
from flaskBlog import app

if __name__ == '__main__':
    app.run(debug=True)