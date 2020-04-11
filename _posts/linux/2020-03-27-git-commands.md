---
title: Linux - Git commands
date: 2020-03-27 09:22:00 +0530
categories: [Linux, Commands]
tags: [linux, git, utilities, commands]
summary: Few git commands.
seo:
  date_modified: 2020-04-11 17:09:01 +0530
---

Few git commands.

| Description                                                          | Command                                               |
| -------------------------------------------------------------------- | ----------------------------------------------------- |
| Delete all branches locally except for ones having the word "master" | `git branch | grep -v "master" | xargs git branch -D` |
