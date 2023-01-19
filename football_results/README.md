# Football Results

For a final score in a football game we'd like to get a description of the result -
- "Home win"
- "Away win"
- "Draw"

A final score has this dictionary structure -

```python
{    
    "home_score": 0,
    "away_score": 1
}
```
We'd also like to get a list of results for a list of final scores.


list-dict

[
    {"home_score": 0,
    "away_score": 1},
    {"home_score": 1,
    "away_score": 0},
    {"home_score": 0,
    "away_score": 0}
]


```python
   return ["Home win", ...]
```

## Running the tests

To run the tests, run `python3 run_tests.py`

