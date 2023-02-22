import sys
from cx_Freeze import setup, Executable

# Set the name of the output executable and directory
exe_name = "main.exe"
output_dir = "dist_windows_cxfreeze_exe"

# Build options
build_options = {
    # "include_msvcr": True,
    "packages": ["tkinter"],
    "excludes": [
        "tcl",
        "_bz2",
        "_decimal",
        "_hashlib",
        "_lzma",
        "_socket",
        "_ssl",
        "bz2",
        "concurrent",
        "distribute",
        "distutils",
        "doctest",
        "docutils",
        "easy_install",
        "email",
        "gzip",
        "html",
        "http",
        "http",
        "IPython",
        "lzma",
        "nose",
        "nose2",
        "packaging",
        "pip",
        "pkg_resources",
        "pydoc",
        "pyreadline",
        "pytest",
        "queue",
        "readline",
        "readline",
        "setuptools",
        "setuptools",
        "sqlite3",
        "tarfile",
        "test",
        "tk",
        "unittest",
        "unittest",
        "wheel",
        "xml",
        "xml",
        "zipfile",
        "zlib",
        "tcltk",    
    ],
    "include_files": ["icons/icon_01.ico"],
}
# Executable definition
exe = Executable(
    script="src/main.py",
    base="Win32GUI",  # Hide the console window
    targetName=exe_name,
    icon="icons/icon_01.ico"
)

# Setup
setup(
    name="MyApp",
    version="1.0",
    description="MyApp Description",
    options={
        "build_exe": build_options,
    },
    executables=[exe],
)
