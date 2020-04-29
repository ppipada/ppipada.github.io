---
title: Movies - Organizing a largish movie collection
date: 2020-03-17 16:53:00 +0530
categories: [Movie]
tags: [movie, linux, ubuntu, kodi]
summary: Organizing a local storage based movie collection.
seo:
  date_modified: 2020-04-28 09:50:38 +0530
---

Organizing a local storage based movie collection. At a high level it involves:

- [Prepare movie metadata](#prepare-movie-metadata)
- [Renaming and folder arrangement](#renaming-and-folder-arrangement)
- [Manage movies in Kodi](#manage-movies-in-kodi)

## Prepare movie metadata

- Use [TinyMediaManager i.e tmm](https://www.tinymediamanager.org/) for metadata management

- Step 1: Prepare source folders:

  - Import local movie paths
    - These are called as `sources` in `tmm`.
    - Add these via `settings`
  - Clean duplicates
  - Manage multi file movies
    - Naming convention is important.
    - Files should end with `-cd1, -cd2, etc or -part1, -part2, etc`.
  - Bulk Subtitles find and download is generally a bad idea.
    - Lot of inaccuracies in downloads.
    - Better do this one by one and before any renaming of files.

- Step 2: Scrape metadata
  - Generally prefer [Kodi](https://kodi.tv/) format metadata (nfo) files. `tmm` provides option for this in the setting.
  - [IMDb](https://www.imdb.com/) vs [TMDb](https://www.themoviedb.org/) metadata
    - `IMDb` scrapping generally is slow for bulk operations
    - `TMDb` provides a good source for movie metadata and most of it (including fan art and posters) can be downloaded from here.
    - I prefer rating from `IMDb`. There is an option to select just ratings from `IMDb` in `tmm`
  - I would recommend doing a two pass metadata search
    - In the first pass do a bulk operation using `TMDb` scrapper. This can include `TMDb` ratings.
    - Once all metadata is downloaded a second bulk search can be done just for `ratings` and `top 250` data using `IMDb`.

## Renaming and folder arrangement

- This step move movies to a `Kodi` recommended structure using `tmm`.
- _CAUTION_ Once renaming is complete it cannot be _undone_. Verify each and every thing before doing renaming.
- Recommended folder structure is `movie-name (year)`. Generally prefer a flat structure over sub-directories and deep hierarchies.
- General preference for file names is same as folder name.
  - I personally prefer `movie-name (year) video-resolution imdb-rating part-no`.
- Once folder name and file name preferences are set in `Settings->Movies->Renamer`, do a dry run to see the changes that `tmm` is going to do.
- Verify the dry run result carefully. Adjust settings if something seems weird.
- Execute rename once verified.

## Manage movies in Kodi

- Install [Kodi](https://kodi.tv/) on your laptop/desktop/tv.
- Import the media folder created using `tmm` above in `Kodi` media manager.
- As a general setting enable `Update library on startup`.
- Cleaning DB in `Kodi` is a bit of a pain. Avoid folder/movie path changes.
  - Keep running `clean library` even for smaller changes done to files/folders.
- Periodically i.e once you have watched enough movies you may want to do a `export library`. This writes `watched` status and any extra info in `Kodi` to .nfo files in source.
