# GNU Screen helpers

- [References](#references)
- [Basic commands](#basic-commands)
- [RC File](#rc-file)

## References

- [Man Page](https://www.gnu.org/software/screen/manual/screen.html)
- [Quick Reference](http://aperiodic.net/screen/quick_reference)

## Basic commands

| Description                                         | Command                                 |
| --------------------------------------------------- | --------------------------------------- |
| Start a new session with session name               | `screen -S <session_name>`              |
| List running sessions / screens                     | `screen -ls`                            |
| Attach to a running session with name               | `screen -R <session_name>`              |
| Detach a running session                            | `screen -d <session_name>`              |
| Command mode                                        | `Ctrl+a`                                |
| Enable vertical scrolling mode in a running session | `Ctrl-a ESC`                            |
| Create new window                                   | `Ctrl-a c`                              |
| Change to window by number                          | `Ctrl-a <number>`                       |
| Enter screen command                                | `Ctrl-a :`                              |
| Send command to the screen session                  | `screen -X -S <session_name> <command>` |
| Send kill command to the screen session             | `screen -X -S <session_name> kill`      |

## RC File

{% highlight shell %}
{% include_relative screenrc %}
{% endhighlight %}
