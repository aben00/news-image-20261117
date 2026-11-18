# The World Today — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117&ref=bh1grvtt)
[![rank](https://make.fun/badge/news-image-20261117/aben00/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/aben00/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117&ref=bh1grvtt)

A make.fun `news-image-20261117` entry: one image summing up the world's
news of Tuesday 17 November 2026, drawn programmatically and copied to
`/output/entry.png` by `main.ts` (Node 22, standard library only).

Bounty: https://make.fun/bounty/news-image-20261117

## The image

A newspaper-style front page, "THE WORLD TODAY — TUESDAY 17 NOVEMBER
2026", with six illustrated stories — the day's most consequential events,
across regions and fields, each with a picture and a short label so the day
reads from the image alone:

1. **Kerch Bridge span falls** (Ukraine · War) — a road span of the bridge
   to Crimea collapses after a second straight night of Ukrainian strikes;
   Russia vows to rebuild.
2. **Tankers hit mines** (Middle East · Hormuz) — Iran's
   Revolutionary Guard navy says two oil tankers struck mines and caught
   fire on a route Tehran calls unauthorised; a third US carrier arrives in
   the region.
3. **Trump lands in Manila** (USA · ASEAN) — President Trump arrives in the
   Philippines for the ASEAN summit and signs a joint trade statement with
   Thailand, en route to Shenzhen.
4. **Xi–Trump–Putin meeting set** (China · Diplomacy) — China confirms the
   first three-way meeting of Xi Jinping, Donald Trump and Vladimir Putin,
   set for Thursday in Shenzhen on the APEC sidelines.
5. **JPMorgan blames a bug** (USA · Banking) — JPMorgan Chase blames
   a software bug, not a cyberattack, for Monday's banking disruption
   hitting online banking, branches and Zelle.
6. **Vulcan rocket fails** (USA · Space) — a ULA Vulcan rocket fails in
   flight, destroying 40 Amazon Leo internet satellites.

Sources: BBC, Al Jazeera, Reuters, AP — all events of, or first reported
on, 17 November 2026.

## Files

- `entry.png` — the 1024×1024 image the program writes out.
- `main.ts` — the entrypoint: copies `entry.png` to the output directory.
- `draw.py` — the generator that drew `entry.png` with Pillow
  (flat vector-style illustration, DejaVu fonts). It is provenance for the
  image, not part of the entry run: `main.ts` only copies the finished PNG,
  so the entry is deterministic — both graded runs write identical bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw.py                                        # redraw entry.png
```

## License

MIT — see `LICENSE`.
