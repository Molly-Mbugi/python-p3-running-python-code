
import os

def test_app_py_exists():
    assert os.path.exists("lib/app.py"), "app.py does not exist in the lib directory"
