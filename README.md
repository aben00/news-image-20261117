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
2026", with three illustrated lead stories and an index of thirty more —
33 verified stories in total, across regions and beats, each with a
headline and a one-line label so the day reads from the image alone.
Every story was checked against reporting dated 17 November 2026
(BBC, Reuters, AP, CNN, NYT, NPR, Al Jazeera and others): each event
either happened or was first reported on that day.

**Lead stories**

1. **Kerch Bridge falls** (Ukraine · War) — a second night of Ukrainian
   strikes brings down a road span of the bridge to Crimea; Russia vows
   to rebuild.
2. **Iran drones hit radar** (Middle East · Iran) — drones fired at a US
   radar base in Bahrain are shot down; US intelligence warns of an
   Iranian "dirty bomb" plot against Trump officials.
3. **Trump lands in Manila** (Asia · Diplomacy) — Trump opens his Asia
   trip at the ASEAN summit, en route to Shenzhen for Thursday's first
   Xi–Trump–Putin three-way meeting.

**More from the day (30)**

- Tankers hit mines off Hormuz · Kyiv's river bridges struck · Japan
  scrambles jets over suspected Russian aircraft · UK sanctions West
  Bank settlement builders · Settler killing in Jericho · Four nations
  urge Israel to open Gaza crossings · Israel election-arrest probe ·
  Houthi advance in Yemen · Estonia shuts its Russia border Dec 1 ·
  128 states meet in Geneva over a killer-robot ban · China–Canada
  tariff cuts worth $280m · Mongolia's president quits over a $25m
  graft claim · US nationwide alert test ("No blackouts") · NYC Mayor
  Mamdani disbands the NYPD protest-response unit · Newsom sued over
  548 commuted death sentences · Supreme Court declines DEI appeals ·
  US loses measles-free status held for 30 years · Nvidia beats on
  $115.8bn as stocks fall · US curbs China chip access via foreign
  data centres · California sues OpenAI · Microsoft blames a defect
  for its 80%-server outage · ULA Vulcan fails, Amazon satellites
  lost · EU charges Temu · COP31 fight over delaying IPCC reports ·
  US data centres emit 25.7m tonnes of CO2 a year · DR Congo Ebola:
  11,200 cases, 5,500 dead · 17 dead in two South Africa shootings ·
  Depardieu pleads guilty in Paris · India beat Pakistan 2–1 for a
  record 10th SAFF title · Alcaraz beats Tiafoe 6–2, 6–2 at the ATP
  Finals in Turin.

Sources: BBC, Reuters, AP, CNN, NYT, NPR, Al Jazeera — all events of,
or first reported on, 17 November 2026.

## Files

- `entry.png` — the 1024×1024 image the program writes out.
- `main.ts` — the entrypoint: copies `entry.png` to the output directory.
- `draw.py` — the generator that drew `entry.png` with Pillow
  (flat vector-style illustration, DejaVu fonts). It is provenance for
  the image, not part of the entry run: `main.ts` only copies the
  finished PNG, so the entry is deterministic — both graded runs write
  identical bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw.py                                        # redraw entry.png
```

## License

MIT — see `LICENSE`.
