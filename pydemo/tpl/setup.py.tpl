import setuptools

setuptools.setup(
	name = "{{name}}",
	version = "{{version}}",
	author = "{{author}}",
	author_email = "{{email}}",
	description = "",
	long_description = open('README.md').read(),
	long_description_content_type = "text/markdown",
	url = "{{github}}",
	packages = setuptools.find_packages(),
	package_data = {},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
