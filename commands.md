# Random commands

- [Docker](#docker)
- [Top](#top)
- [Jekyll](#jekyll)
- [Virtualbox](#virtualbox)

## Docker

| Description                                                 | Command                                            |
| ----------------------------------------------------------- | -------------------------------------------------- |
| List all container instances, with their ID and status      | `docker ps -a`                                     |
| Lists all images on the local machine                       | `docker images`                                    |
| Displays the logs from a running container                  | `docker logs [container name or ID]`               |
| Stop all containers                                         | `docker stop $(docker ps -a -q)`                   |
| Delete all containers                                       | `docker rm $(docker ps -a -q)`                     |
| Changes command prompt from the host to a running container | `docker attach [container name or ID]`             |
| Executes a command within a running container               | `docker exec [container name or ID] shell command` |

## Top

| Description                                                                                                                        | Command                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| display top with threads                                                                                                           | `top -H`                                                   |
| top with output sorted by memory                                                                                                   | `top -o %MEM`                                              |
| run top in batch mode 10 times with 5 seconds delay in command mode with output sorted by memory                                   | `top -b -n 10 -d 5 -c -o %MEM`                             |
| run top in batch mode 10 times with 5 seconds delay in command mode with output sorted by memory and only print 15 lines at a time | `top -b -n 10 -d 5 -c -o %MEM | grep "load average" -A 15` |

## Jekyll

Reference - [Using with bundler](https://jekyllrb.com/tutorials/using-jekyll-with-bundler/)

| Description          | Command                    |
| -------------------- | -------------------------- |
| serve jekyll locally | `bundle exec jekyll serve` |

## Virtualbox

| Description                    | Command                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| create a vmdk using raw device | `VBoxManage internalcommands createrawvmdk -filename "</path/to/file>.vmdk" -rawdisk /dev/sdb` |
