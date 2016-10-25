# -*- coding: utf-8 -*-

from __future__ import print_function

try:
	import sublime, sublime_plugin
except ImportError:
	print ("GotoFolder: 'import sublime, sublime_plugin' ImportError - (Expected during testing)")
	class Dummy(object):
		TextCommand = object
	sublime_plugin = Dummy()


import subprocess, os, re
from .GotoFolderHelpers import symbol_replacer

class GotoFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit, c=None):
		commandkey = c
		if self.is_enabled():
			self.settings = sublime.load_settings("GotoFolder.sublime-settings")
			launchers = self.settings.get("launchers")
			if not launchers:
				print ("'GotoFolder.sublime-settings' missing key 'launchers', no launchers to run.")
				return
			if commandkey in launchers:
				cmd = self._replace_arguments(launchers[commandkey])
				self._launch_process(cmd)
			else:
				print ("Unregonised command: please set in 'GotoFolder.sublime-settings'")

	def is_enabled(self):
		return bool(self.view.file_name() and len(self.view.file_name()) > 0)

	def _launch_process(self, arglist):
		''' launch detached process '''
		DETACHED_PROCESS = 0x00000008 #is this windows spesific?
		print ("opening proccess %s" % arglist[0])
		subprocess.Popen(arglist, close_fds=True, creationflags=DETACHED_PROCESS)

	def _replace_arguments(self, arglist):
		Path = self.view.file_name()
		Dir = os.path.dirname(Path)
		File = os.path.basename(Path)
		Linenumber = 0

		# Find line number of first cursor else leave as 0
		cursors = self.view.sel()
		if len(cursors) > 0:
			point = cursors[0].begin()
			linenumber = self.view.rowcol(point)

		escape_keys = {
			'P': Path,
			'D': Dir,
			'F': File,
			'L': Linenumber,
		}

		newargs = [symbol_replacer(a, escape_keys) for a in arglist]
		# print (newargs)
		return newargs
