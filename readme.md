# Date Difference Calculator

A Python command-line tool to calculate the difference between two dates or display details about a single date.

## Usage

### Calculate difference between two dates:
```
python app.py -s <day> <month> <year> -e <day> <month> <year>
```

Example:
```
python app.py -s 1 January 2020 -e 1 January 2021
```

### Show details for a single date:
```
python app.py -a <day> <month> <year>
```

Example:
```
python app.py -a 1 January 2020
```

### Show detailed information with difference:
Add `-d` flag for details.

```
python app.py -s 1 January 2020 -e 1 January 2021 -d
```

### Display calendar and select a date:
```
python app.py -c <year>
```

Example:
```
python app.py -c 2023
```