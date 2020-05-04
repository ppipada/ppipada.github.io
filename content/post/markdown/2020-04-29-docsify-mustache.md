---
title: Mustache templates and YAML front-matter with Docsify
date: 2020-04-29 08:30:00 +0530
categories: [Markdown, Docsify]
tags: [markdown, yaml, front-matter, mustache, docsify]
summary:
  Docsify, YAML front-matter, mustache templates & tags and some quirks when
  using them.
seo:
  date_modified: 2020-04-29 11:52:50 +0530
---

Docsify, YAML front-matter, mustache templates & tags and some quirks when using them.

## Docsify

[Docsify](https://docsify.js.org/) is a great documentation site generator.

- It generates your documentation website on the fly using Markdown files directly.
- To start using it, all you need to do is create an index.html and deploy it on GitHub pages or any other static site host.
- It has a great plugin system that enables extensibility and can be used for solving multiple use cases.

## Docsify-Mustache

One such plugin that is greatly useful is [Docsify-Mustache](https://docsify-mustache.github.io/#/).

- It allows preprocessing markdown documents with [Mustache](https://mustache.github.io/) template engine.
- Mustache is a logic-less templating system. It works by expanding tags in a provided template using values provided in a hash or object.
  - E.g: If you use `{{name}}` as template in your markdown and provide the value for `name` either via [YAML front-matter](https://docsify-mustache.github.io/#/?id=front-matter) or any other supported [sources](https://docsify-mustache.github.io/#/?id=sources), that value will get rendered.
- How to use this plugin with docsify is very well explained in the [documentation site](https://docsify-mustache.github.io/) for this plugin.

## Mustache tags

- Mustache supports different types of tags as documented in [mustache manual](https://mustache.github.io/mustache.5.html).
- The basic tags, that were useful to me, when dealing with a documentation site are `Variables`, `Sections with non-empty lists` and `Inverted sections`.
- Below are a few examples on using these mustache tag types. I have considered the source of the "values" as YAML front-matter in markdown but as pointed out before, the source can be any supported input type.

### Variables

Variables are the most basic tag type in mustache. The template for accessing a variable is `{{variable_name}}`.

Example:

- Consider that you declare the following YAML front-matter in your markdown document:

  ```yaml
  ---
  title: My awesome project documentation
  category: Useful
  ---

  ```

- Now, if you want to refer this in the markdown file you can add:

```markdown
{{title}}

This project belongs to category: {{category}}
```

- When rendering the page `title` and `category` will be substituted using the values declared in the front matter.

### Sections with non-empty lists

Sections render blocks of text one or more times, depending on the value of the key in the current context.

A section begins with a pound and ends with a slash. That is, `{{#person}}` begins a `"person"` section while `{{/person}}` ends it.

When the value for a section is a non-empty list, the text in the block will be displayed once for each item in the list. The context of the block will be set to the current item for each iteration. In this way we can loop over collections.

> IMPORTANT NOTE: If the list `values` contain a hyphen `-` in them then the list rendering is incorrect/fails for that value. To avoid this use single quotes ('') around the value as depicted below.

Example:

- Consider that you declare the following YAML front-matter in your markdown document:

  ```yaml
  ---
  tags: [useful, "rocket-science", launch]
  ---

  ```

- Now, if you want to refer the `tags` list in the markdown file you can add:

```markdown
This doc is has the following tags:
{{#tags}}
{{.}}
{{/tags}}
```

- Output will be rendered as:

  ```text
  This doc is has the following tags: useful, rocket-science, launch
  ```

### Inverted sections

Inverted sections may render text once based on the inverse value of the key. That is, they will be rendered if the key doesn't exist, is false, or is an empty list.

An inverted section begins with a caret (hat) and ends with a slash. That is `{{^person}}` begins a "person" inverted section while `{{/person}}` ends it.

Example:

- Consider that you declare the following YAML front-matter in your markdown document:

  ```yaml
  ---
  tags: []
  ---

  ```

- Now, if you want to handle the `tags` list being empty and check for `category` being absent you can add:

```markdown
This doc is has the following tags:
{{^category}}
No category found !!!
{{/category}}

{{^tags}}
No tags found !!!
{{/tags}}
```

- Given that the categories key doesn't exist and the tags list is empty, Output will be rendered as:

  ```text
  No categories found !!!
  No tags found !!!
  ```

### Extended example

An extended example where we add a YAML front-matter to a markdown file, use the variables and handle the absent cases is given below.

Markdown file that adds a constant heading section to the documentation page, where the `title` will be displayed first, then `category` will be displayed and then the `tags` list is provided:

```markdown
---
title: My awesome project documentation
tags: [useful, "rocket-science", launch]
---

# {{title}}

{{category}}
{{^category}}
No category found !!!
{{/category}}

Tag list:
{{#tags}}
{{.}}
{{/tags}}
{{^tags}}
No tags found !!!
{{/tags}}
```

The output rendered will be:

```text
My awesome project documentation

No category found !!!

Tag list: useful, rocket-science, launch
```

## Example project

> Most of the above mentioned concepts and tools are used at my [tech-interview-prep](https://ppipada.github.io/tech-interview-prep/#/) project site. That can act as a good reference.
