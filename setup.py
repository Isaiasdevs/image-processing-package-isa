# Indicando a biblioteca setuptools para o desenvolvimento do pacote | Documentação: https://setuptools.readthedocs.io/en/latest/setuptools.html
from setuptools import setup, find_packages

with open("README.md", "r") as f:           # Aponta para página com a descrição longa da descrição do pacote
    page_description = f.read()

with open("requirements.txt") as f:         # Aponta para o carregamento automático dos requerimentos para uso do pacote
    requirements = f.read().splitlines()

setup(
    name = "isaias_image_processing",
    version = "0.0.1",
    author = "Isaias Araújo",
    author_email = "araujoisaias.dev@outlook.com",
    description = "Pacote para Processamento de imagens",
    long_description = page_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Isaiasdevs/image-processing-package-isa",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.8',
)