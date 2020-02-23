from setuptools import setup

from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pysympla",
    version="0.1",
    description=" plataforma online de eventos líder no Brasil. Venda de ingressos, promoção e administração de eventos. Simples e segura. Organiza eventos? Sympla!",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/hudsonbrendon/pysympla",
    author="Hudson Brendon",
    author_email="contato.hudsonbrendon@gmail.com",
    license="MIT",
    packages=["pysympla"],
    install_requires=["requests",],
    zip_safe=False,
)