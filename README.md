Steps to reproduce:

```
$ pyright --version
pyright 1.1.319

$ PYTHONPATH=install pyright foobar.py
$repro/foobar.py
  $repro/foobar.py:1:8 - error: Stub file not found for "oops.json_importer" (reportMissingTypeStubs)
1 error, 0 warnings, 0 informations
```
