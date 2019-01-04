""" Car Hire App entry point

"""
from carhire.database import create_db
from carhire.views.root_view import RootView

if __name__ == "__main__":
    print("APP START")
    # noinspection PyStatementEffect
    create_db
    app = RootView()
    app.mainloop()
    print("APP END")
