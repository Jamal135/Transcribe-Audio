import os
import sys
import pip


ACTIVATE_PATH = 'venv/Scripts/activate_this.py'


def get_prefix():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix


def import_or_install(package):
    ''' Purpose: Installs package if it does not exist. '''
    try:
        __import__(package)
        print(f'{package} package already installed')
    except ImportError:
        pip.main(['install', package])


def create_venv():
    ''' Purpose: Creates and activates virtual environment. '''
    import_or_install('virtualenv') # https://pypi.org/project/virtualenv/
    os.system('virtualenv venv')
    exec(compile(open(ACTIVATE_PATH, "rb").read(), ACTIVATE_PATH, 'exec'), dict(__file__ = ACTIVATE_PATH))
     

if __name__ == '__main__':
    try:
        if get_prefix() == sys.prefix:
            create_venv()
        print('Installing packages...')
        os.system('pip install -r requirements.txt')
        print('Setup complete! Please activate venv and restart IDE...')
    except Exception as e:
        print(f"Automatic setup failed:\n{e}")