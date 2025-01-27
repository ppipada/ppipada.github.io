#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from pprint import pprint
import shutil
import subprocess

import frontmatter

TAG_DIR = 'all-tags'

MAX_LEVEL = 2  # Tree level for current script file.
SCAN_PATH = "."

EXCLUDED_DIRECTORIES = ["pycode", "images", "algorithms", "system-design-primer"]
# EXCLUDED_DIRECTORIES_FROM_SIDEBAR = ["problems"]
EXCLUDED_DIRECTORIES_FROM_SIDEBAR = []
INCLUDED_FILE_TYPES = ["*.md"]

EXCLUDED_FILE_PREFIXES = [
    '_',
    '.',
]

EXCLUDED_FILES = [
    'algorithms.md',
    'coding.md',
    'introduction.md',
    'CHANGELOG.md',
    'external.md',
    'coverpage.md',
    'all.md',
    'data-structures.md',
    'system-design.md',
    'README.md',
]

# Define a section that is always going to be at the top of the sidebar. The
# format is regular Markdown. Example:
# DEFAULT_HEADER = '''
# * [Home](./home.md)
# * [Summary](./summary.md)
# '''
DEFAULT_HEADER = '''
* [Introduction](/)
* [Data structures](data-structures.md)
* [Algorithms](algorithms/)
  * [Bitmasks](algorithms/bitmasks.md)
  * [Graph](algorithms/graph.md)
  * [Greedy](algorithms/greedy.md)
  * [Sorting](algorithms/sorting.md)
* [Coding](coding.md)
* [System Design](https://github.com/donnemartin/system-design-primer)
'''

# Define section that is always going to be at bottom of sidebar
DEFAULT_BOTTOM = '''
* [External references](external.md)
* [Changelog](CHANGELOG.md)

* [![Github](https://icongram.jgog.in/simple/github.svg?color=808080&size=16)Github](https://github.com/ppipada/ppipada.github.io/tree/master/tech-interview-prep)
* [<img src="/favicon.ico" width="16" height="16" style="vertical-align:middle;" /> Blog](https://pankajpipada.com)
* [![Linkedin](https://icongr.am/simple/linkedin.svg?color=808080&size=16)Linkedin](https://www.linkedin.com/in/ppipada)
'''


def make_display_name_from_path(path):
    parts = path.split('/')
    name = parts[-1]
    name = name.split(".md")[0]  # Remove .md extension
    name = name.replace('-', ' ')  # Add space instead of -
    name = name.replace('_i_', '')  # Always remove _i_ index flag
    name = name.lower().capitalize()  # Capitalize first word
    return name


def create_dir_index_file(dir_tree, dir_path):
    # Create index file name
    dir_name = dir_path.split('/')[-1]
    # dir_index_file_path = dir_path.replace(dir_name, '_i_' + dir_name) + '.md'
    dir_index_file_path = os.path.join(dir_path, "README.md")

    if (os.path.isfile(dir_index_file_path)):
        # Clear existing file
        open(dir_index_file_path, 'w').close()

    # Compose the index file
    index_file = open(dir_index_file_path, 'w')

    # Write a title
    dir_display_name = make_display_name_from_path(dir_path)
    index_file.write(f"# {dir_display_name}\n\n")

    # Write a link for each entry in this directory
    dir_entries, file_entries = get_dir_entries_from_tree(dir_tree, dir_path)
    entries = dir_entries + file_entries
    for entry_file_name in entries:
        entry_path = dir_path + '/' + entry_file_name
        # entry_path = entry_file_name
        entry_display_name = make_display_name_from_path(entry_path)
        # if os.path.isdir(entry_path):
        #     entry_path = dir_path + '/_i_' + entry_file_name
        if entry_path.startswith("./"):
            entry_path = entry_path[2:]
        index_file.write(f"* [{entry_display_name}]({entry_path})\n\n")

    index_file.close()


def write_entry_in_sidebar(entry_path, level, index=False):
    """
    Write the sidebar entry, on the right level
    """
    # Add prefix for index files
    if index:
        # entry_file_name = entry_path.split('/')[-1]
        # entry_path = entry_path.replace(entry_file_name,
        #                                 '_i_' + entry_file_name) + '.md'
        entry_path = entry_path + '.md'
    # Write entry in the sidebar file
    entry_display_name = make_display_name_from_path(entry_path)
    if entry_path.startswith("./"):
        entry_path = entry_path[2:]
    append_static_section(
        f"{'  ' * level}* [{entry_display_name}]({entry_path})\n")

def write_direntry_in_sidebar(entry_path, level):
    """
    Write the sidebar entry, on the right level
    """
    # Add prefix for index files
    # if index:
    #     # entry_file_name = entry_path.split('/')[-1]
    #     # entry_path = entry_path.replace(entry_file_name,
    #     #                                 '_i_' + entry_file_name) + '.md'
    #     entry_path = entry_path + '.md'
    # Write entry in the sidebar file
    entry_display_name = make_display_name_from_path(entry_path)
    if entry_path.startswith("./"):
        entry_path = entry_path[2:]
    entry_path = entry_path + '/'
    append_static_section(
        f"{'  ' * level}* [{entry_display_name}]({entry_path})\n")

def get_dir_entries_from_tree(dir_tree, dir_path):
    dnode = dir_tree.get(dir_path)
    if not dnode:
        print("Did not find directory entry in tree for", dir_path)
        return [], []
    return dnode[0], dnode[1]


def check_directory_index_file(dir_path, filename):
    filename = filename.split(".md")[0]
    entry_path = dir_path + '/' + filename
    return os.path.isdir(entry_path)

def generate_readme_pages(dir_tree,
    dir_path='.',
    level=0):

    """
    Look inside each directory in the project to see if there's anything good to
    add to the sidebar
    """
    dir_entries, file_entries = get_dir_entries_from_tree(dir_tree, dir_path)
    sublevel = level + 1

    if level > 0:
        # Create folder index (skip root directory)
        create_dir_index_file(dir_tree, dir_path)

    for entry_dir_name in dir_entries:
        # Compose full path for this entry
        entry_path = dir_path + '/' + entry_dir_name
        if os.path.isdir(entry_path):
            # Scan this directory to add the entries it contains
            generate_readme_pages(dir_tree, entry_path, sublevel)


def scan_dir(
    dir_tree,
    dir_path='.',
    level=0,
    exclude_from_sidebar=False,
):
    """
    Look inside each directory in the project to see if there's anything good to
    add to the sidebar
    """
    dir_entries, file_entries = get_dir_entries_from_tree(dir_tree, dir_path)
    sublevel = level + 1

    if not exclude_from_sidebar:
        for entry_file_name in file_entries:
            # Compose full path for this entry
            # print("processing", entry_file_name)
            isdir = check_directory_index_file(dir_path, entry_file_name)
            if isdir:
                print("Skipping index file: {} for directory {}".format(entry_file_name, dir_path))
                continue
            entry_path = dir_path + '/' + entry_file_name
            if os.path.isfile(entry_path):
                # Found suitable sidebar item, write it down
                # print("writing in sidebar", entry_path)
                write_entry_in_sidebar(entry_path, level)

    for entry_dir_name in dir_entries:
        current_exclude_from_sidebar = exclude_from_sidebar
        if entry_dir_name in EXCLUDED_DIRECTORIES_FROM_SIDEBAR:
            current_exclude_from_sidebar = True
        # Compose full path for this entry
        entry_path = dir_path + '/' + entry_dir_name
        if os.path.isdir(entry_path):
            if not current_exclude_from_sidebar:
                # Create a higher lever entry for this directory
                write_direntry_in_sidebar(entry_path, level)
                # write_entry_in_sidebar(entry_path, level, index=True)
            # Scan this directory to add the entries it contains
            # Skipping this and adding just the directory in sidebar
            scan_dir(dir_tree, entry_path, sublevel, exclude_from_sidebar=current_exclude_from_sidebar)


def get_direntries(path='.',
                   exclude_dirs=None,
                   exclude_files=None,
                   include_file_types=None,
                   exclude_prefixes=None):

    if not exclude_dirs:
        exclude_dirs = []
    if not exclude_files:
        exclude_files = []
    if not include_file_types:
        include_file_types = [".md"]
    if not exclude_prefixes:
        exclude_prefixes = []

    dents = [d for d in os.scandir(path)]
    # print(dents)
    dlist = []
    flist = []
    for d in dents:
        if d.is_dir():
            if d.name in exclude_dirs:
                print("excluded:", d.name)
                continue
            # print(d.path)
            dlist.append(d.path)
            continue
        if d.is_file():
            if d.name in exclude_files:
                print("excluded:", d.name)
                continue
            if (any(i for i in exclude_prefixes if d.name.startswith(i))):
                print("excluded:", d.name)
                continue
            # print("included:", d.name)
            _, ext = os.path.splitext(d.path)
            if ext in include_file_types:
                flist.append(d.path)

    return sorted(dlist), sorted(flist)


def get_dir_heirarchy(path='.',
                      exclude_dirs=None,
                      exclude_files=None,
                      include_file_types=None,
                      exclude_prefixes=None,
                      nlevels=2):
    if not exclude_dirs:
        exclude_dirs = []
    if not exclude_files:
        exclude_files = []
    if not exclude_prefixes:
        exclude_prefixes = []

    level = 0
    res = {}
    plist = [path]
    while len(plist) > 0 and level <= nlevels:
        clist = []
        iterlist = plist[:]
        for pent in iterlist:
            dlist, flist = get_direntries(pent,
                                          exclude_dirs=exclude_dirs,
                                          exclude_files=exclude_files,
                                          exclude_prefixes=exclude_prefixes)
            # print(dlist, flist)
            res[pent] = ([os.path.basename(d) for d in dlist],
                         [os.path.basename(f) for f in flist])
            clist.extend(dlist)
            # print("removing", pent)
            plist.remove(pent)
        if clist:
            plist.extend(clist)
        # print(plist)
        level += 1

    return res


def append_static_section(section, sidebar_file="_sidebar.md"):
    if section:
        f = open(sidebar_file, 'a')
        f.write(section)
        f.close()


def get_frontmatter_for_file(fpath):
    post = frontmatter.load(fpath)
    tags = []
    title = ""
    if "tags" in post:
        tags = post["tags"]
    if "title" in post:
        title = post["title"]
    # print(fpath, tags, title)
    return tags, title


def get_all_tags(dir_tree, dir_path=".", tag_dict=None):
    if not tag_dict:
        tag_dict = {}

    dir_entries, file_entries = get_dir_entries_from_tree(dir_tree, dir_path)
    for entry_file_name in file_entries:
        # Compose full path for this entry
        entry_path = dir_path + '/' + entry_file_name
        if os.path.isfile(entry_path):
            # Found suitable sidebar item, get tags for it
            ftags, ftitle = get_frontmatter_for_file(entry_path)
            if not ftitle:
                ftitle = make_display_name_from_path(entry_path)
            if entry_path.startswith("./"):
                entry_path = entry_path[2:]
            for t in ftags:
                if t not in tag_dict:
                    tag_dict[t] = []
                # print("appending")
                tag_dict[t].append((entry_path, ftitle))
    # print(tag_dict)
    for entry_dir_name in dir_entries:
        # Compose full path for this entry
        entry_path = dir_path + '/' + entry_dir_name
        if os.path.isdir(entry_path):
            # Scan this directory to add the entries it contains
            tag_dict = get_all_tags(dir_tree, dir_path=entry_path, tag_dict=tag_dict)

    return tag_dict


def generate_tag_pages(dir_tree, dir_path="."):
    all_tags = get_all_tags(dir_tree, dir_path=".")
    print("Got tags:")
    pprint(all_tags)
    if not all_tags:
        print("Didnt get any tags")
        return
    tag_path = os.path.join(dir_path, TAG_DIR)
    if os.path.exists(tag_path):
        print("removing current tag tree")
        shutil.rmtree(tag_path)

    os.makedirs(tag_path)

    for tag, files in all_tags.items():
        tag_page = tag_path + '/' + tag.replace(' ', '-').lower() + '.md'
        with open(tag_page, 'w+', encoding='utf-8') as md:
            # Write entry in the sidebar file
            entry_display_name = make_display_name_from_path(tag_page)
            md.write("# {}\n\n".format(entry_display_name))
            if not files:
                print("Did not get any files for tag {}".format(tag))
                continue
            for entry_path, ftitle in sorted(files):
                md.write("* [{}]({})\n\n".format(ftitle, entry_path))

    change = subprocess.getoutput("git status {} -s".format(TAG_DIR))
    if change:
        print("[INFO] Succeed! {} tag-pages created.".format(len(all_tags)))


def process_page_generation(gen_tags, gen_sidebar, gen_readme):
    # Start process
    # First get the eligible directory structure
    print("Generating tags: {}. Generating sidebar: {}. Generating readme files: {}".format(
        gen_tags, gen_sidebar, gen_readme))
    if (not gen_tags) and (not gen_sidebar) and (not gen_readme):
        print("Not generating anything.")
        return

    result = get_dir_heirarchy(path=SCAN_PATH,
                               exclude_dirs=EXCLUDED_DIRECTORIES,
                               exclude_files=EXCLUDED_FILES,
                               include_file_types=INCLUDED_FILE_TYPES,
                               exclude_prefixes=EXCLUDED_FILE_PREFIXES,
                               nlevels=MAX_LEVEL)

    print("Got tree to process:")
    pprint(result)
    if gen_tags:
        generate_tag_pages(result, dir_path=SCAN_PATH)

    if gen_readme:
        generate_readme_pages(result, dir_path=SCAN_PATH)

    if gen_sidebar:
        # Erase sidebar's content
        open('_sidebar.md', 'w').close()
        if DEFAULT_HEADER:
            append_static_section(DEFAULT_HEADER)

        scan_dir(result, dir_path=SCAN_PATH)

        if DEFAULT_BOTTOM:
            append_static_section(DEFAULT_BOTTOM)


    # Time for a cold one
    print('✅ All done, cheers!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate pages for docsify")
    parser.add_argument("-t",
                        "--tags",
                        action="store_true",
                        help="Generate tags pages from frontmatter")
    parser.add_argument("-r",
                        "--readme",
                        action="store_true",
                        help="Generate readme files for directories")
    parser.add_argument("-s",
                        "--sidebar",
                        action="store_true",
                        help="Generate sidebar pages using dir structure")
    args = parser.parse_args()
    process_page_generation(args.tags, args.sidebar, args.readme)
