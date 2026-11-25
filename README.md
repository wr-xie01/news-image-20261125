# The World in One Day — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/wr-xie01/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/wr-xie01/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A newspaper front page that sums up Wednesday 25 November 2026 in a
single 1024×1024 image. Every story on the page happened or was first
reported on 25 November 2026.

## The six stories

1. **HODEIDAH — Coalition strikes Yemen port.** Saudi-led warplanes
   hit Hodeidah port early Wednesday, after an evacuation order. The
   Houthis threaten Saudi Red Sea ports, including Jeddah.
2. **HORMUZ — Iran says tankers hit mines.** Iran says two oil tankers
   struck naval mines and caught fire early Wednesday in the Strait of
   Hormuz, on what it calls an unauthorised route.
3. **JIUQUAN — Shenzhou-24 lifts off.** China launches Shenzhou-24,
   carrying Pakistan's Muhammad Zeeshan Ali, the first foreign
   astronaut to visit the Tiangong space station.
4. **SEOUL — Subway strike called off.** Seoul Metro unions call off a
   strike hours before the morning rush after a last-minute deal: a
   3.5% pay rise, 500 new hires, and job cuts shelved.
5. **GENEVA — Chess crown: Game 2.** Gukesh and Sindarov play Game 2
   of the world title match, level at half a point each after a
   38-move draw in the opener. Gukesh has White.
6. **CALIFORNIA — King tides peak.** Near-record king tides peak
   Wednesday on California's coast, flooding low streets as a storm
   hits Thanksgiving travel. San Francisco airport is on alert.

## How it is built

`generate_image.py` draws the front page with PIL (masthead, date band,
six story cards with simple icons, footer) and writes `entry.png`.
`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default
`/output`), checking the 1 MiB size limit and the 1024×1024 limit first.
Both runs write the same bytes.

Run it:

```sh
python3 generate_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
