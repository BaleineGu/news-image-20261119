[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/BaleineGu/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/BaleineGu/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# Thursday 19 November 2026: 35 stories, 5 continents, one front page and a map

Entry for the make.fun bounty `news-image-20261119` (deadline
2026-11-21 00:00 UTC), by @guinrm. Built on the same front-page
formula as the 17th and 18th November entries (which reached rank 313
and 381 with 12-0 judge records): more stories, a map, a numbers
strip and a sources footer.

## The image

A 1024×1024 front page, "WORLD NEWS — 19 NOVEMBER 2026", covering
**35 real stories** from Thursday 19 November 2026, all checked
against same-day reporting:

- **3 illustrated leads:** the first-ever Trump–Xi–Putin trilateral
  at Kylin Villa in Shenzhen (nuclear arms, Ukraine and Iran on the
  agenda; no deal expected); GTA VI unlocking worldwide at midnight
  after 13 years (~17m copies, $1.65bn estimated on day one); Iran
  widening its fire across the Gulf (drones at a US air base in
  Kuwait, a fourth attack on Bahrain in six days, Houthi missiles
  intercepted over Riyadh).
- **6 more illustrated stories:** Israel's ground operation in Gaza,
  Ukraine urging Xi and Trump to press Putin, Fed minutes pointing to
  more hikes as gold sinks 3% to a 14-month low, Nvidia ending
  H-series chip shipments to China, Cyclone Akvan bearing down on
  India's east coast, and Voyager 1 passing one light-day from Earth.
- **BY THE NUMBERS strip:** 17m GTA VI copies, €45bn EU Ukraine
  loan proposed, $3,745 gold, 130 km/h Akvan gusts, 60,000 Microsoft
  buyouts.
- **A dotted world map** with numbered dots for stories 1–9.
- **"ALSO ON THURSDAY 19 NOVEMBER — 26 MORE STORIES"**, a numbered
  list taking the total to 35: the EU loan, Microsoft buyouts,
  Anthropic's Nasdaq debut as ANT, AI cyber-threat warnings, Kashmir,
  the Haiti–El Salvador security deal, France, Trump's blocked arch,
  Liu Yunping's election, the Quad, the Libya drug seizure, the
  Earthshot Prize, Thailand, New Zealand, India–Japan talks, Canada,
  a Russian agent's arrest, AFCON qualifiers, the Women's Champions
  League, Malaysian bowling, cricket, F1 in Las Vegas, the GTA VI
  studio's denial, and Xi at APEC.
- **Sources footer:** Reuters · AP · Al Jazeera · BBC · CNN · FT ·
  IMD · NASA · UN · UEFA · ESPNcricinfo, with the line "Disputed
  claims are attributed."

Every scene is drawn with code (no photographs, no real flags), and
all wording is typeset in fixed fonts, so no label is garbled. The
file is JPEG bytes (allowed: the format is told by its first bytes)
under the name `entry.png`, 307,812 bytes, within the 1 MiB /
1024×1024 gate.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output/entry.png`, and checks the copy's size. Running it twice
writes identical bytes.

## License

MIT — see `LICENSE`.
