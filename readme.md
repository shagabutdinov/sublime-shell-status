# Sublime ShellStatus plugin

Run shell command and output its result to status bar.


### Demo

![Notebook screenshot](https://raw.github.com/shagabutdinov/sublime-shell-status/master/screenshot.png)
![Notebook screenshot without battery](https://raw.github.com/shagabutdinov/sublime-shell-status/master/screenshot_without_battery.png)


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.

There is "sublime-status" file in this package. Put it in your "bin" folder or
specify full path to it in package settings to start using the plugin with
default settings.


### Features

Run shell command and add its output to status bar to sublime. By default (with
corrent installation) adds following information:

  - branch (git or mercurial if any);

  - time;

  - battery charge if it lower that 50 percent;

  - path of currently edited file (I'm keeping everything in "server"
    directory so everything before it (incling server/[folder]/) will be removed
    from path; probably you'll want to change this behavior).

Time and battery charge are displayed because I work on i3 with disabled status
bar: that allows to focus hardly on current task. It also allows sublime to
employ as much space as possible when I work on laptop.

There is an issue with displaying some icons (when battery icon is displayed all
text go to bottom out of viewable region and underscores becomes invisible). If
you know how to fix this so please please tell me it ASAP; I got really annoyed
of this bug.

Battery charge will be displayed usign "acpi" command. So you'll need to install
it in order to see battery charge. If you are not using Linux you need to fix
sublime-status command (written with ruby) or write your own to display battery
charge.


### Usage

You can use any language to create sublime-status command. First argument to
command will currently opened file name. Status will be updated on focus.
Command will be executed in directory where file is located.

Note that you should use "\t\t" (two tabs) as separator to format status bar
information nicely.

Example comand (php):

  ```  
  #!/usr/bin/env php
  <?php
  
  // don't forget to chmod u+x this file
  echo "Currently editing: " . $argv[1] . "\t\t";
  echo "Time is: " . date("H:i:s") . "\t\t";
  ```

### Settings

Shell command could be specified globally in "command" in
"ShellStatus.sublime-settings" or per-project using "status_command" setting.

Examples:

  ```
  # globally, ShellStatus.sublime-settings in your User-folder
  {
    "command": "my-status-command"
  }

  # per project, "ctrl+u, p" hotkey to open project settings.
  {
    ...,
    "settings": {
      "status_command": "my-status-command",
      ...
    }
  }
  ```


### Dependencies

* [StatusMessage](https://github.com/shagabutdinov/sublime-status-message)
