"""
Py-Tree-sitter
"""


import platform
from setuptools import setup, Extension


setup(
    name = "tree_sitter",
    version = "0.0.7",
    maintainer = "Max Brunsfeld",
    maintainer_email = "maxbrunsfeld@gmail.com",
    author = "Max Brunsfeld",
    author_email = "maxbrunsfeld@gmail.com",
    url = "https://github.com/tree-sitter/py-tree-sitter",
    license = "MIT",
    platforms = ["any"],
    python_requires = ">=3.3",
    description = "Python bindings to the Tree-sitter parsing library",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Compilers",
        "Topic :: Text Processing :: Linguistic",
    ],
    packages = ['tree_sitter'],
    ext_modules = [
        Extension(
            "tree_sitter_binding",
            [
                "tree_sitter/core/lib/src/lib.c",
                "tree_sitter/binding.c",
            ],
            include_dirs = [
                "tree_sitter/core/lib/include",
                "tree_sitter/core/lib/utf8proc",
            ],
            extra_compile_args = (
                ['-std=c99'] if platform.system() != 'Windows' else None
            )
        )
    ],
    project_urls = {
        'Source': 'https://github.com/tree-sitter/py-tree-sitter',
        'Documentation': 'http://initd.org/psycopg/docs/',
    }
)
