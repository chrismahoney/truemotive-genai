# <AppName> command quick reference

Source: `<cli> commands` registry, <N> commands, captured <date>. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected.

Call shape: <how a command is sent in this app's batch path>.

## <Family 1: for example Documents and files>

| Command | Params |
|---|---|
| `<id>` | `<abbreviated params>` |

## <Family 2: the app's main drawing or editing commands>

| Command | Params |
|---|---|

## Other families (use `artcraft-find` for params)

`<family>.*` (<count>), ...

Rules for this file: pick the 6 to 10 families an agent needs first, cite only IDs that exist (`lint.py --app <slug>` checks every backticked ID), write transport methods and CLI subcommands as plain words so they are not mistaken for commands, and keep each table small.
