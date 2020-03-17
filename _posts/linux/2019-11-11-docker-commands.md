---
title: Docker - Commands
date: 2019-11-11 21:55:00 +0530
categories: [Linux, Docker]
tags: [linux, docker, utilities, commands]
summary: Basic docker commands.
seo:
  date_modified: 2020-03-17 15:21:18 +0530
---

Basic docker commands.

## Commands

| Description                                                 | Command                                            |
| ----------------------------------------------------------- | -------------------------------------------------- |
| List all container instances, with their ID and status      | `docker ps -a`                                     |
| Lists all images on the local machine                       | `docker images`                                    |
| Displays the logs from a running container                  | `docker logs [container name or ID]`               |
| Stop all containers                                         | `docker stop $(docker ps -a -q)`                   |
| Delete all containers                                       | `docker rm $(docker ps -a -q)`                     |
| Changes command prompt from the host to a running container | `docker attach [container name or ID]`             |
| Executes a command within a running container               | `docker exec [container name or ID] shell command` |
