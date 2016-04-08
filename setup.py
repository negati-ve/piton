from distutils.core import setup
setup(
	name = 'piton',
	license='LICENSE',
	packages = ['piton', 'piton/utils', 'piton/commands'], # this must be the same as the name above
	version = '0.1.0',
	description = 'A local python package manager',
	url = 'https://github.com/piton-package-manager/piton', # use the URL to the github repo
	keywords = ['package', 'manager', 'local'], # arbitrary keywords
	classifiers = [
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	],
	entry_points = {
		'console_scripts': [
			'piton = piton.main:main'
		]
	}
)
