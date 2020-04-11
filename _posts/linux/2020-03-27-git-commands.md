---
title: Linux - Git commands
date: 2020-03-27 09:22:00 +0530
categories: [Linux, Commands]
tags: [linux, git, utilities, commands]
summary: Few git commands.
---

Few git commands.

| Description                                                          | Command                                               |
| -------------------------------------------------------------------- | ----------------------------------------------------- |
| Delete all branches locally except for ones having the word "master" | `git branch | grep -v "master" | xargs git branch -D` |
