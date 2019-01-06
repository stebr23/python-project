"""
Car Hire App entry point
"""
from carhire.database import create_db
import carhire.views.root_view
import carhire.constants as app_const
from carhire.services.view_controller import ViewController


env = "DEBUG"

if env == "DEBUG":
    LOG_LEVEL = app_const.LOG_LEVEL_DEV
elif env == "PROD":
    LOG_LEVEL = app_const.LOG_LEVEL_PROD
else:
    LOG_LEVEL = app_const.LOG_LEVEL_NONE


if __name__ == "__main__":
    print("APP START")
    # noinspection PyStatementEffect
    create_db
    view_controller = ViewController()
    app = carhire.views.root_view.RootView()
    app.add_view_controller(view_controller)
    view_controller.add_root_frame(app)
    view_controller.set_frame()
    app.mainloop()
    print("APP END")
