---
title: "LRC for syncd lyrics"
layout: post
date: 2026-03-22 20:00
---

I just discoverd the LRC file format, and the companion library [LRCLib](https://lrclib.net/), and they are things of beauty. It's a file format for providing time-syncd lyrics. What it enables - the ability to view lyrics that keep pace with a song as it plays on your music player - is close to miraculous, but the structure of the file is a thing of wondrous simplicity.

The LRC format has some variations, but at its core it's quite simple. It's a newline-delimited plain text file; each line is prefixed with a timestamp, and that is followed by the lyrics which go with that timestamp. Here, for example, are the first few lines of the [Stairway to Heaven LRC](https://lrclib.net/search/stairway%20to%20heaven):

> [00:52.87]There's a lady who's sure
>
> [00:56.66]All that glitters is gold
>
> [00:59.38]And she's buying a stairway to Heaven

As you can see, it's delightfully easy to read, edit, and distribute. LRCLib (which has numerous competitors) provides lyrics by UI, but also API and data product, which is exactly as it should be.

My music player of choice [Musicolet](https://play.google.com/store/apps/details?id=in.krosbits.musicolet), which is quite a fine specimen unto itself - if you're on Android you've got to check it out. In any case LRC lyrics fit together with it like a glove. All you have to do is embed an LRC file in your MP3 file - use the `USLT` ID3 tag - and your player will nicely sync up the lyrics with the music. Magic!

Obviously this find begs for a little side project, and one of these days I hope to see how many lyrics I can embed in my MP3 collection. The LRCLib database is a 21 GB SQLite file, which is quite tractable. Should be fun!