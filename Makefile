.RECIPEPREFIX := >
UNIT ?=
FORCE ?=
PY := python3 scripts/generate.py
UNITFLAG := $(if $(UNIT),--unit $(UNIT),)
FORCEFLAG := $(if $(FORCE),--force,)

.PHONY: help outline content build freeze unfreeze clean

help:
> @echo "make outline  [UNIT=01-pathfinding] [FORCE=1]   generate / refresh structural outlines"
> @echo "make freeze   UNIT=01-pathfinding                approve an outline so content can be generated"
> @echo "make content  [UNIT=01-pathfinding] [FORCE=1]    generate lecture/lab/claims from FROZEN outlines"
> @echo "make build    [UNIT=...] [FORCE=1]               outline + content in one go"
> @echo "make unfreeze UNIT=01-pathfinding                re-open an outline for editing"
> @echo "make clean                                       drop the input-hash cache (keeps build/)"

outline:
> $(PY) --stage outline $(UNITFLAG) $(FORCEFLAG)

content:
> $(PY) --stage content $(UNITFLAG) $(FORCEFLAG)

build:
> $(PY) --stage all $(UNITFLAG) $(FORCEFLAG)

freeze:
> @test -n "$(UNIT)" || { echo "UNIT=<id> required, e.g. make freeze UNIT=01-pathfinding"; exit 1; }
> @mkdir -p build/units/$(UNIT) && touch build/units/$(UNIT)/.frozen
> @echo "Frozen: $(UNIT). Now run: make content UNIT=$(UNIT)"

unfreeze:
> @test -n "$(UNIT)" || { echo "UNIT=<id> required"; exit 1; }
> @rm -f build/units/$(UNIT)/.frozen
> @echo "Unfrozen: $(UNIT)"

clean:
> rm -rf .build-cache
