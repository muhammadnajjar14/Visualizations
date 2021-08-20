Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> %matplotlib inline
SyntaxError: invalid syntax
>>> %plt inline
SyntaxError: invalid syntax
>>> table = pd.read_csv("season-1819_csv.csv")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    table = pd.read_csv("season-1819_csv.csv")
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 688, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 454, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 948, in __init__
    self._make_engine(self.engine)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1180, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 2010, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 674, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] No such file or directory: 'season-1819_csv.csv'
>>> C:/Users/SHARAF/Downloads/season-1819_csv.csv
SyntaxError: invalid syntax
>>> table = pd.read_csv("C:\Users\SHARAF\Downloads\season-1819_csv.csv")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> table=pd.read_csv("Users\SHARAF\Downloads\season-1819_csv.csv")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    table=pd.read_csv("Users\SHARAF\Downloads\season-1819_csv.csv")
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 688, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 454, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 948, in __init__
    self._make_engine(self.engine)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1180, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 2010, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 674, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] No such file or directory: 'Users\\SHARAF\\Downloads\\season-1819_csv.csv'
>>> table=pd.read_csv("C:/Users/SHARAF/Downloads/season-1819_csv.csv")
>>> table.head()
  Div        Date      HomeTeam        AwayTeam  ...  BbAvAHA  PSCH  PSCD  PSCA
0  E0  10/08/2018    Man United       Leicester  ...     2.21  1.55  4.07  7.69
1  E0  11/08/2018   Bournemouth         Cardiff  ...     1.75  1.88  3.61  4.70
2  E0  11/08/2018        Fulham  Crystal Palace  ...     1.77  2.62  3.38  2.90
3  E0  11/08/2018  Huddersfield         Chelsea  ...     2.06  7.24  3.95  1.58
4  E0  11/08/2018     Newcastle       Tottenham  ...     1.76  4.74  3.53  1.89

[5 rows x 62 columns]
>>> table=pd.read_csv("C:/Users/SHARAF/Downloads/epl20162017.csv")
>>> table.head()
   #               Team  MP   W   D  L   F   A  D.1   P
0  1            Chelsea  38  30   3  5  85  33   52  93
1  2  Tottenham Hotspur  38  26   8  4  86  26   60  86
2  3    Manchester City  38  23   9  6  80  39   41  78
3  4          Liverpool  38  22  10  6  78  42   36  76
4  5            Arsenal  38  23   6  9  77  44   33  75
>>> plt.hlines(y=np.arrange(1,21),xmin=0,xmax=table['P'])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    plt.hlines(y=np.arrange(1,21),xmin=0,xmax=table['P'])
  File "C:\Users\SHARAF\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\__init__.py", line 215, in __getattr__
    "{!r}".format(__name__, attr))
AttributeError: module 'numpy' has no attribute 'arrange'
>>> plt.hlines(y=np.arange(1,21),xmin=0,xmax=table['P'])
<matplotlib.collections.LineCollection object at 0x0FF9FDD0>






