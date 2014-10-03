from __future__ import print_function
import sublime, sublime_plugin
import subprocess, os, re

class GotoFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit, c=None):
		commandkey = c
		if self.is_enabled():
			self.settings = sublime.load_settings("GotoFolder")
			commands = self.settings.get("commands")
			if not commands:
				print ("'GotoFolder.sublime-settings' missing key 'commands', no commands to run.")
				return
			if commandkey in commands:
				cmd = self.arg_replacer(commands[commandkey])
				self.launch_process(cmd)
			else:
				print ("Unregonised command: please set in 'GotoFolder.sublime-settings'")

	def is_enabled(self):
		return bool( self.view.file_name() and len(self.view.file_name()) > 0)

	def launch_process(self, arglist):
		''' launch detached process '''
		DETACHED_PROCESS = 0x00000008 #is this windows spesific?
		print ("opening proccess %s" % arglist[0])
		subprocess.Popen(arglist, close_fds=True, creationflags=DETACHED_PROCESS)

	def arg_replacer(self, arglist):
		""" 
		Generate a new arguments list replacing (RegEx)"@\w" with corresponding var.
		NOTE: Unit tests for prefered implementation are currently failing. 
		      So you get his instead.
		"""
		##TODO proper escape parser

		linenumber = 0
		cursors = self.view.sel()
		if len(cursors) == 1:
			point = cursors[0].begin()
			linenumber = self.view.rowcol(point)

		escapes = {
			'd': os.path.dirname(self.view.file_name()),
			'f': os.path.basename(self.view.file_name()),
			'l': linenumber,
			'@': '@',
		}
		newargs = []
		for arg in arglist:
			if arg.startswith(r'@'):
				if len(arg) == 2 and arg[1] in escapes:
					escaped = escapes[arg[1]]
					newargs.append(escaped)
			else:
				newargs.append(arg)
		return newargs
