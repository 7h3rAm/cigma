# cigma

cigma is a pure-Python file type identification library. It aims to provide quick and easy type identification without incurring the overhead of parsing file structure to gather metadata. It stores signatures in a json formatted file with the following structure:

```python
{
  "id": 1,
  "longname": "PKZIP",
  "mimetype": "application/octet-stream",
  "patterns": [
    {
      "offset": 0,
      "regex": "\\x50\\x4B\\x05\\x06",
      "size": 4
    }
  ],
  "shortname": "ZIP"
}
```

One can add additional regexes to the patterns list for stricter checks (Eg: PE files, JPG files that include trailers). For each regex in patterns list, **size** bytes of data at the **offset** within file are extracted. If all regexes match, a dict is returned with input source and match results.

## Usage

Import the cigma module:

```python
from cigma import cigma
```

Identify a file buffer:

```python
with open("/bin/ls") as fo:
  filedata = fo.read()

cigma.Cigma().identify(data=filedata)
{'match': {'id': 29,
           'longname': 'Executable and Linkable Format (ELF)',
           'mimetype': 'application/x-executable',
           'patterns': [{'offset': 0,
                         'regex': '\\x7F\\x45\\x4C\\x46',
                         'size': 4}],
           'shortname': 'ELF'},
 'source': '/bin/ls'}
```

Identify a file:

```python
cigma.Cigma().identify(filename="notepad.exe")
{'match': {'id': 31,
           'longname': 'Windows Executable',
           'mimetype': 'application/x-dosexec',
           'patterns': [{'offset': 0, 'regex': '\\x4D\\x5A', 'size': 2}],
           'shortname': 'EXE'},
 'source': 'notepad.exe'}
```

## Author
Ankur Tyagi ([@7h3rAm](https://twitter.com/7h3ram))

## License
This work is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_GB).

![CC-BY-NC-SA](http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)
