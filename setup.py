import setuptools

setuptools.setup(
	name = "pydemo",
	version = "0.0.1",
	author = "ciiseven",
	author_email = "ciiseven@yeah.net",
	description = "",
	long_description = open('README.md').read(),
	long_description_content_type = "text/markdown",
	url = "https://github.com/ciiseven/pydemo",
	packages = setuptools.find_packages(),
	package_data = {'pydemo':['tpl/*.tpl', 'tpl/.gitignore.tpl'],},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
