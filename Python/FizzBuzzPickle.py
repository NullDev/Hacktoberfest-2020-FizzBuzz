"""FizzBuzz implemented using a Python pickle bomb (tested in version 3.6)
Author: @PAndaContron

Python has a serialization library called pickle, which is actually a full bytecode VM that allows for arbitrary code execution.
This allows for "pickle bombs" to be created; data which, when deserialized, executes code instead of returning an object.
However, since pickle bytecode isn't really designed to be used this way, it's very inflexible.
A workaround would be to use the eval function to run python code, but that's boring; it would just be a slightly modified version of an existing program.

This pickle bytecode is equivalent to the following python code:
operator.getitem(list(map(print, itertools.starmap(operator.add, zip(itertools.starmap(operator.add, zip(map(functools.partial(operator.mul, 'Fizz'), map(functools.partial(operator.gt, 1), itertools.starmap(operator.mod, zip(itertools.count(1), itertools.repeat(3))))), map(functools.partial(operator.mul, 'Buzz'), map(functools.partial(operator.gt, 1), itertools.starmap(operator.mod, zip(itertools.count(1), itertools.repeat(5))))))), itertools.starmap(operator.mul, zip(map(operator.not_, map(functools.partial(operator.gt, 1), itertools.starmap(operator.mul, zip(itertools.starmap(operator.mod, zip(itertools.count(1), itertools.repeat(3))), itertools.starmap(operator.mod, zip(itertools.count(1), itertools.repeat(5))))))), map(str, range(1, 101)))))))), 0)
"""

import pickle

pickle.loads(b'coperator\ngetitem\n(c__builtin__\nlist\n(c__builtin__\nmap\n(c__builtin__\nprint\ncitertools\nstarmap\n(coperator\nadd\nc__builtin__\nzip\n(citertools\nstarmap\n(coperator\nadd\nc__builtin__\nzip\n(c__builtin__\nmap\n(cfunctools\npartial\n(coperator\nmul\nVFizz\ntRc__builtin__\nmap\n(cfunctools\npartial\n(coperator\ngt\nI1\ntRcitertools\nstarmap\n(coperator\nmod\nc__builtin__\nzip\n(citertools\ncount\n(I1\ntRcitertools\nrepeat\n(I3\ntRtRtRtRtRc__builtin__\nmap\n(cfunctools\npartial\n(coperator\nmul\nVBuzz\ntRc__builtin__\nmap\n(cfunctools\npartial\n(coperator\ngt\nI1\ntRcitertools\nstarmap\n(coperator\nmod\nc__builtin__\nzip\n(citertools\ncount\n(I1\ntRcitertools\nrepeat\n(I5\ntRtRtRtRtRtRtRcitertools\nstarmap\n(coperator\nmul\nc__builtin__\nzip\n(c__builtin__\nmap\n(coperator\nnot_\nc__builtin__\nmap\n(cfunctools\npartial\n(coperator\ngt\nI1\ntRcitertools\nstarmap\n(coperator\nmul\nc__builtin__\nzip\n(citertools\nstarmap\n(coperator\nmod\nc__builtin__\nzip\n(citertools\ncount\n(I1\ntRcitertools\nrepeat\n(I3\ntRtRtRcitertools\nstarmap\n(coperator\nmod\nc__builtin__\nzip\n(citertools\ncount\n(I1\ntRcitertools\nrepeat\n(I5\ntRtRtRtRtRtRtRc__builtin__\nmap\n(c__builtin__\nstr\nc__builtin__\nrange\n(I1\nI101\ntRtRtRtRtRtRtRtRI0\ntR.')

"""Pickletools disassembly:
    0: c    GLOBAL     'operator getitem'
   18: (    MARK
   19: c        GLOBAL     '__builtin__ list'
   37: (        MARK
   38: c            GLOBAL     '__builtin__ map'
   55: (            MARK
   56: c                GLOBAL     '__builtin__ print'
   75: c                GLOBAL     'itertools starmap'
   94: (                MARK
   95: c                    GLOBAL     'operator add'
  109: c                    GLOBAL     '__builtin__ zip'
  126: (                    MARK
  127: c                        GLOBAL     'itertools starmap'
  146: (                        MARK
  147: c                            GLOBAL     'operator add'
  161: c                            GLOBAL     '__builtin__ zip'
  178: (                            MARK
  179: c                                GLOBAL     '__builtin__ map'
  196: (                                MARK
  197: c                                    GLOBAL     'functools partial'
  216: (                                    MARK
  217: c                                        GLOBAL     'operator mul'
  231: V                                        UNICODE    'Fizz'
  237: t                                        TUPLE      (MARK at 216)
  238: R                                    REDUCE
  239: c                                    GLOBAL     '__builtin__ map'
  256: (                                    MARK
  257: c                                        GLOBAL     'functools partial'
  276: (                                        MARK
  277: c                                            GLOBAL     'operator gt'
  290: I                                            INT        1
  293: t                                            TUPLE      (MARK at 276)
  294: R                                        REDUCE
  295: c                                        GLOBAL     'itertools starmap'
  314: (                                        MARK
  315: c                                            GLOBAL     'operator mod'
  329: c                                            GLOBAL     '__builtin__ zip'
  346: (                                            MARK
  347: c                                                GLOBAL     'itertools count'
  364: (                                                MARK
  365: I                                                    INT        1
  368: t                                                    TUPLE      (MARK at 364)
  369: R                                                REDUCE
  370: c                                                GLOBAL     'itertools repeat'
  388: (                                                MARK
  389: I                                                    INT        3
  392: t                                                    TUPLE      (MARK at 388)
  393: R                                                REDUCE
  394: t                                                TUPLE      (MARK at 346)
  395: R                                            REDUCE
  396: t                                            TUPLE      (MARK at 314)
  397: R                                        REDUCE
  398: t                                        TUPLE      (MARK at 256)
  399: R                                    REDUCE
  400: t                                    TUPLE      (MARK at 196)
  401: R                                REDUCE
  402: c                                GLOBAL     '__builtin__ map'
  419: (                                MARK
  420: c                                    GLOBAL     'functools partial'
  439: (                                    MARK
  440: c                                        GLOBAL     'operator mul'
  454: V                                        UNICODE    'Buzz'
  460: t                                        TUPLE      (MARK at 439)
  461: R                                    REDUCE
  462: c                                    GLOBAL     '__builtin__ map'
  479: (                                    MARK
  480: c                                        GLOBAL     'functools partial'
  499: (                                        MARK
  500: c                                            GLOBAL     'operator gt'
  513: I                                            INT        1
  516: t                                            TUPLE      (MARK at 499)
  517: R                                        REDUCE
  518: c                                        GLOBAL     'itertools starmap'
  537: (                                        MARK
  538: c                                            GLOBAL     'operator mod'
  552: c                                            GLOBAL     '__builtin__ zip'
  569: (                                            MARK
  570: c                                                GLOBAL     'itertools count'
  587: (                                                MARK
  588: I                                                    INT        1
  591: t                                                    TUPLE      (MARK at 587)
  592: R                                                REDUCE
  593: c                                                GLOBAL     'itertools repeat'
  611: (                                                MARK
  612: I                                                    INT        5
  615: t                                                    TUPLE      (MARK at 611)
  616: R                                                REDUCE
  617: t                                                TUPLE      (MARK at 569)
  618: R                                            REDUCE
  619: t                                            TUPLE      (MARK at 537)
  620: R                                        REDUCE
  621: t                                        TUPLE      (MARK at 479)
  622: R                                    REDUCE
  623: t                                    TUPLE      (MARK at 419)
  624: R                                REDUCE
  625: t                                TUPLE      (MARK at 178)
  626: R                            REDUCE
  627: t                            TUPLE      (MARK at 146)
  628: R                        REDUCE
  629: c                        GLOBAL     'itertools starmap'
  648: (                        MARK
  649: c                            GLOBAL     'operator mul'
  663: c                            GLOBAL     '__builtin__ zip'
  680: (                            MARK
  681: c                                GLOBAL     '__builtin__ map'
  698: (                                MARK
  699: c                                    GLOBAL     'operator not_'
  714: c                                    GLOBAL     '__builtin__ map'
  731: (                                    MARK
  732: c                                        GLOBAL     'functools partial'
  751: (                                        MARK
  752: c                                            GLOBAL     'operator gt'
  765: I                                            INT        1
  768: t                                            TUPLE      (MARK at 751)
  769: R                                        REDUCE
  770: c                                        GLOBAL     'itertools starmap'
  789: (                                        MARK
  790: c                                            GLOBAL     'operator mul'
  804: c                                            GLOBAL     '__builtin__ zip'
  821: (                                            MARK
  822: c                                                GLOBAL     'itertools starmap'
  841: (                                                MARK
  842: c                                                    GLOBAL     'operator mod'
  856: c                                                    GLOBAL     '__builtin__ zip'
  873: (                                                    MARK
  874: c                                                        GLOBAL     'itertools count'
  891: (                                                        MARK
  892: I                                                            INT        1
  895: t                                                            TUPLE      (MARK at 891)
  896: R                                                        REDUCE
  897: c                                                        GLOBAL     'itertools repeat'
  915: (                                                        MARK
  916: I                                                            INT        3
  919: t                                                            TUPLE      (MARK at 915)
  920: R                                                        REDUCE
  921: t                                                        TUPLE      (MARK at 873)
  922: R                                                    REDUCE
  923: t                                                    TUPLE      (MARK at 841)
  924: R                                                REDUCE
  925: c                                                GLOBAL     'itertools starmap'
  944: (                                                MARK
  945: c                                                    GLOBAL     'operator mod'
  959: c                                                    GLOBAL     '__builtin__ zip'
  976: (                                                    MARK
  977: c                                                        GLOBAL     'itertools count'
  994: (                                                        MARK
  995: I                                                            INT        1
  998: t                                                            TUPLE      (MARK at 994)
  999: R                                                        REDUCE
 1000: c                                                        GLOBAL     'itertools repeat'
 1018: (                                                        MARK
 1019: I                                                            INT        5
 1022: t                                                            TUPLE      (MARK at 1018)
 1023: R                                                        REDUCE
 1024: t                                                        TUPLE      (MARK at 976)
 1025: R                                                    REDUCE
 1026: t                                                    TUPLE      (MARK at 944)
 1027: R                                                REDUCE
 1028: t                                                TUPLE      (MARK at 821)
 1029: R                                            REDUCE
 1030: t                                            TUPLE      (MARK at 789)
 1031: R                                        REDUCE
 1032: t                                        TUPLE      (MARK at 731)
 1033: R                                    REDUCE
 1034: t                                    TUPLE      (MARK at 698)
 1035: R                                REDUCE
 1036: c                                GLOBAL     '__builtin__ map'
 1053: (                                MARK
 1054: c                                    GLOBAL     '__builtin__ str'
 1071: c                                    GLOBAL     '__builtin__ range'
 1090: (                                    MARK
 1091: I                                        INT        1
 1094: I                                        INT        101
 1099: t                                        TUPLE      (MARK at 1090)
 1100: R                                    REDUCE
 1101: t                                    TUPLE      (MARK at 1053)
 1102: R                                REDUCE
 1103: t                                TUPLE      (MARK at 680)
 1104: R                            REDUCE
 1105: t                            TUPLE      (MARK at 648)
 1106: R                        REDUCE
 1107: t                        TUPLE      (MARK at 126)
 1108: R                    REDUCE
 1109: t                    TUPLE      (MARK at 94)
 1110: R                REDUCE
 1111: t                TUPLE      (MARK at 55)
 1112: R            REDUCE
 1113: t            TUPLE      (MARK at 37)
 1114: R        REDUCE
 1115: I        INT        0
 1118: t        TUPLE      (MARK at 18)
 1119: R    REDUCE
 1120: .    STOP
highest protocol among opcodes = 0
"""
