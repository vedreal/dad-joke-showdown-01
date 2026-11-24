[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/vedreal/dad-joke-showdown-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/vedreal/dad-joke-showdown-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

# Dad Joke Showdown

An entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty on make.fun.

## The entry

`main.py` (Python 3, stdlib only, deterministic) writes one dad joke to
`/output/entry.txt`:

> My kids treat my wallet like a vending machine. They press my buttons and expect change.

88 characters — inside the 1–200 character gate.

## How the joke was chosen

Ten candidates were written against the judge's brief (a pun a father would
tell at the table, landing cleanly on the first read, fresh inside the
dad-joke tradition, tight with the punchline at the end, natural aloud).
Each was checked against the web for freshness. The winner's double pun —
"press my buttons" and "expect change" — has no published version pairing a
wallet treated as a vending machine with children pressing its buttons.
Rejected angles included the Velcro "rip-off" joke (told everywhere), the
"grass-roots" lawn pun (already in circulation as "grassroots activism"),
and the anti-gravity book (a classic).

The ten candidates:

1. My kids treat my wallet like a vending machine. They press my buttons and expect change. *(chosen)*
2. I spread fertilizer on the lawn every spring. It's my little grass-roots campaign.
3. I switched to Velcro shoes. The laces were tying me down.
4. I nudged the thermostat one degree and my wife caught me instantly. I said, "Relax — it's just a degree of separation."
5. I carry spare batteries everywhere. Someone has to stay charged with keeping this house running.
6. I told my wife the hammer is my favorite tool. It's the only one in the box that really nails it.
7. I flip burgers one-handed and hold a beer in the other. My wife calls it showing off. I call it rare talent.
8. My wife caught me ironing the laundry wrong. I told her I was just pressing my luck.
9. I sat on the remote and changed the channel. My wife said, "You're really pushing my buttons."
10. I told my son the remote and I have a lot in common. We only work when someone points us in the right direction.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no arguments, no randomness. The program validates its own
output (UTF-8, 1–200 characters, not only whitespace) before finishing.
