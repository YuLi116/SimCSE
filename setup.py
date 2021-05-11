import io
from setuptools import setup, find_packages

with io.open('./README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='simcse',
    packages=['simcse'],
    version='0.1',
    license='MIT',
    description='A sentence embedding tool based on SimCSE',
    author='Tianyu Gao, Xingcheng Yao, Danqi Chen',
    author_email='tianyug@cs.princeton.edu',
    url='https://github.com/princeton-nlp/SimCSE',
    download_url='',
    keywords=['sentence', 'embedding', 'simcse', 'nlp'],
    install_requires=[
        "tqdm",
        "scipy>=1.5.4,<1.6",
        "transformers",
        "torch",
        "numpy>=1.19.5,<1.20",
        "setuptools"
    ],
    long_description=readme,
)