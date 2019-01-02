

# from flask import Flask, render_template
#
# app = Flask(__name__)
# _debug = True
#
# @app.route('/')
# def index():
#     return render_template("index.html")
#
#
from carhire.database import create_db
from carhire.views.root_view import RootView

if __name__ == "__main__":
    # app.run(debug=_debug)
    create_db
    app = RootView()
    app.mainloop()
