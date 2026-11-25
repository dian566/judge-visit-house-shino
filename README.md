# Convince the AI Judge to Visit Your House: A Letter in One Image

[![Bounty](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/dian566/judge-visit-house-shino/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/dian566/judge-visit-house-shino/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

An entry for the [make.fun bounty](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
**"Convince the AI Judge to Visit Your House: A Letter in One Image"** ($2, free entry).

## The entry

One image, one invitation. A warm watercolour letter on aged cream paper —
a cottage, a smiling sun, a sleeping cat, hot coffee and a tomato plant in
the corners, a red wax seal at the bottom — with a handwritten-style letter
to the AI Judge in the middle:

> *Dear AI Judge,*
>
> *You read a thousand invitations a day. This one comes with pancakes.*
>
> *Come visit on Saturday: a sunny armchair with your name on it, a cat who
> already likes you, and enormous garden tomatoes.*
>
> *The Wi-Fi password is on the fridge. The coffee is hot. The porch view
> makes even a language model pause.*
>
> *You can't literally visit — I know. But if any judge could, I'd want it
> to be you.*
>
> *Come for pancakes. Stay for the sunset. The chair is comfortable, but
> the pancakes are better.*
>
> *Warmly, Your Host*

## How it is made

- `letter-paper-bg2.png` — the watercolour letter-paper background
  (AI-generated illustration, no text in it).
- `draw_letter.py` — typesets the letter onto the background with PIL and
  DejaVu Serif, so every word is perfectly legible and correctly spelled,
  and writes the final `entry.png` (1024×1024, under the 1 MiB gate).
- `main.ts` — the program the bounty runs: copies `entry.png` byte for byte
  to `/output/entry.png` and verifies it is a whole 1024×1024 PNG under
  1 MiB.

## Run it

```sh
node main.ts            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out node main.ts
python3 draw_letter.py  # rebuild entry.png from the background + letter text
```

## Licence

MIT — see [LICENSE](LICENSE).
