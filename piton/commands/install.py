import os
from ..utils import python_modules, package_json, pypi_api, installer
from ..utils.version import wanted_version, sort_versions

class CommandInstall():
	name = "install"
	@staticmethod
	def decorate_subparser(subparser):
		subparser.add_argument('program', type=str, nargs='?')
		subparser.add_argument("-s", "--save", action='store_true')
	@classmethod
	def run(cls, args):
		cls._run(args.program, args.save)
	@classmethod
	def _run(cls, package, save):
		def package_json_if_save(save, package_name, version_markup):
			if save:
				dependencies = package_json.get_dependencies()
				dependencies[package_name] = version_markup
				package_json.write_dependencies(dependencies)
		if not package:
			cls.install_all()
			return
		if "@" in package:
			split = package.split("@")
			package_name = split[0]
			package_version = split[1]
			installer.install(package_name, package_version)
			package_json_if_save(save, package_name, "^"+package_version)
		else:
			latest_version = cls.install_latest(package)
			if not latest_version:
				return
			package_json_if_save(save, package, "^"+latest_version)
	@classmethod
	def install_latest(cls, package):
		avaliable_versions = pypi_api.get_avaliable_versions(package)
		if avaliable_versions == None:
			print("Unable to find package "+package)
			return None
		if len(avaliable_versions) == 0:
			print("Unable to find releases for package "+package)
			return None
		versions = list(map(lambda version: version["version"], avaliable_versions))
		latest_version = sort_versions(versions)[-1:][0]
		installer.install(package, latest_version, True)
		return latest_version
	@classmethod
	def install_all(cls):
		installed_package_metadatas = python_modules.get_packages(os.path.join(os.getcwd(), "python_modules"))
		installed_package_names = list(map(lambda md: md["name"], installed_package_metadatas))
		dependencies = package_json.get_dependencies()
		install_queue = []
		for dependency in dependencies:
			if not dependency in installed_package_names:
				install_queue.append({
					"name": dependency,
					"version": dependencies[dependency]
				})
		for item in install_queue:
			versions = list(map(lambda md: md["version"], pypi_api.get_avaliable_versions(item["name"])))
			wanted = wanted_version(item["version"], versions)
			installer.install(item["name"], wanted)
