import sys
from cx_Freeze import setup, Executable
import platform

# Detect the current operating system
current_os = platform.system()

# Set the base value based on the current operating system
if current_os == 'Windows':
    base = 'Win32GUI'
else:
    base = None

build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": [],
}

setup(
    name="GptTokenSaver",
    version="0.1",
    description="Reduces the amount of tokens used in GPT-3 result",
    options={"build_exe": build_exe_options},
    executables=[Executable("gpt_token_saver_app.py", base=base)],
)
