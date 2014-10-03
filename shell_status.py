import sublime
import sublime_plugin
from StatusMessage import status_message
import os
import subprocess

class ShellStatusListener(sublime_plugin.EventListener):
  def on_activated_async(self, view):
    settings = sublime.load_settings('ShellStatus.sublime-settings')
    command = view.settings().get('status_command') or settings.get('command')

    if command == 'DEFAULT':
      command = sublime.packages_path() + '/ShellStatus/sublime-status'

    if view.file_name() == None or command == None:
      return

    path = os.path.dirname(view.file_name())
    process = subprocess.Popen([command, view.file_name()],
      stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)

    status, err = process.communicate()
    status = status.decode('UTF-8').strip()
    # __ is for very first position
    status_message.set(view, '__', status)