import sublime, sublime_plugin
import subprocess, os, re

goto_folder_settings = sublime.load_settings("GotoFolder.sublime-settings")

def launch_process(arglist):
	''' launch detached process '''
	DETACHED_PROCESS = 0x00000008 #is this windows spesific?
	print "opening proccess %s" % arglist[0]
	subprocess.Popen(arglist, close_fds=True, creationflags=DETACHED_PROCESS)

def arg_replacer(arglist):
	""" 
	Generate a new arguments list replacing (RegEx)"@\w" with corresponding var.
	NOTE: Unit tests for prefered implementation are currently failing. 
	      So you get his instead.
	"""
	##TODO proper escape parser
	escapes = {
		'd': os.path.dirname(self.view.file_name()),
		'f': os.path.basename(self.view.file_name()),
		'@': '@',
	}
	newargs = []
	for arg in arglist:
		if arg.startswith(r'@'):
			if len(arg) == 2 and escapes.haskey(arg[1]):
				escaped = escapes[arg[1]]
				newargs.append(escaped)
		else:
			newargs.append(arg)
	return newargs


class GotoFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit, mode=None):
		if self.is_enabled():
			launchers = goto_folder_settings
			cmd = arg_replacer(launchers[mode])
			if launchers.has_key(mode):
				launch_process(cmd)
			else:
				print "Unregonised Mode/Launcher Argument: please set in 'GotoFolder.sublime-settings'"

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0