import os
from ..utils import installer, package_json

class CommandRemove():
	name = "remove"
	@staticmethod
	def decorate_subparser(subparser):
		subparser.add_argument('programs', type=str, nargs='*')
		subparser.add_argument("-s", "--save", action='store_true')
	@classmethod
	def run(cls, args):
		if not args.programs:
			return
		for package in args.programs:
			removed = installer.remove(package)
			if not removed:
				print("package "+package+" is not installed")
			if args.save:
				package_json.remove_dependency(package)
