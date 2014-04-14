import sublime, sublime_plugin
import subprocess, os

def launch_process(arglist):
	''' launch detached process '''
	DETACHED_PROCESS = 0x00000008
	print "opening proccess %s" % arglist[0]
	subprocess.Popen(arglist, close_fds=True, creationflags=DETACHED_PROCESS)

def arg_expand(in_str):
	''' TODO:: Expanding settings
	 '''
	out_str = in_str
	return our_str

class GotoFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit, mode='e'):
		if len(self.view.file_name()) > 0:
			fn = os.path.dirname(self.view.file_name())
			if mode == 'e':
				launch_process(["explorer", fn])
			elif mode == 'c':
				launch_process(["conemu64", "/Dir", fn, "/Single" ])
			#sublime.set_clipboard(self.view.file_name())
			#sublime.status_message("Copied file path")

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0