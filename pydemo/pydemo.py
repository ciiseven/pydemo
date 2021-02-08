#!/usr/bin/env python3
import os
import jinja2

def version():
	return '0.0.1'

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path.strip())

def fread(f, encoding='utf-8'):
    if os.path.isfile(f):
        with open(f, 'r', encoding=encoding) as fd:
            return fd.read()

def fwrite(f, d, encoding='utf-8'):
    with open(f, 'w', encoding=encoding) as fd:
        fd.write(d)

def template(tpl, *args, **kwargs):
    return jinja2.Template(tpl).render(*args, **kwargs)

class PyDemo():
    def __init__(self, name, path='.', author='pydemo', email='', github=''):
        self.name = name
        self.path = path
        self.author = author
        self.email = email
        self.github = github
        self.version = '0.0.1'
        self.epath = os.path.dirname(os.path.relpath(__file__))
        self.versionfunc = f"def version():\n\treturn '{self.version}'"

        mkdir(os.path.join(self.path, self.name))
        mkdir(os.path.join(self.path, self.name, self.name))

        self.tpl('.gitignore')
        self.tpl('install.sh')
        self.tpl('README.md', name=self.name)
        self.tpl('LIENSE', author=self.author)
        self.tpl('setup.py', name=self.name, author=self.author, email=self.email, github=self.github, version=self.version)

        fwrite(os.path.join(self.path, self.name, self.name, '__init__.py'), f'from {self.name} import *')
        fwrite(os.path.join(self.path, self.name, self.name, f'{self.name}.py'), self.versionfunc)

    def tpl(self, a, *args, **kwargs):
        d = fread(os.path.join(self.epath, 'tpl', a+'.tpl'))
        d = template(d, *args, **kwargs)
        fwrite(os.path.join(self.path, self.name, a), d)

def demo(name, path='.', author='pydemo', email='', github=''):
    PyDemo(name, path, author, email, github)

if __name__ == '__main__':
    demo('fy', '/Users/admin/GitProjects')
