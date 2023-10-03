from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Main.py', base=base, target_name = 'MyAnimePut', icon = 'Resources/icon.ico')
]

setup(name='MyAnimePut',
      version = '23',
      description = 'MyAnimePut',
      options = {'build_exe': build_options},
      executables = executables)
