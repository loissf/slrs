## WIP

Dynamically typed, garbage-collected language.

Runs on a stack-based VM with a very simple tracing mark-and-sweep GC.

Very much unfinished — expect bugs.

## Examples

Example scripts can be found in the `scripts/` folder alongside Python equivalents for comparison.

## Usage

```bash
cargo run --bin sl --release <path>
```

## Benchmarks

Comparison of results from (`bench.sl`) and its Python equivalent.
Percentages are relative to a fixed baseline from previous results.

| Test    | Time (ms)    | Base %    | Python Time (ms) | Python %   |
|---------|--------------|-----------|------------------|------------|
| calls   | 370          | 98.9305%  | 754              | 201.6042%  |
| pi      | 296          | 108.4249% | 317              | 116.1172%  |
| fib     | 409          | 103.8071% | 707              | 179.4416%  |
| concat  | 290          | 80.3324%  | 233              | 64.5429%   |
| total   | 1365         | 97.3609%  | 2011             | 143.4379%  |
