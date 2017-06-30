#######################################
# ファイルの操作
#######################################

from collections import Counter

# 引数としてファイル名が与えられたときにそのファイルを開き、
# 1行目と2行目を読み取って、それらを整数とみなして足し算したものを返せ

# 以下を書きかえる


def f1(filename):
    return 0
# ここまでを書きかえる

#######################################
# イテレータの使い方
#######################################
# 引数としてファイル名が与えられたときにそのファイルを開き、
# 3行目に書かれている文字列を返せ

# 以下を書きかえる


def f2(filename):
    return 0
# ここまでを書きかえる


#######################################
# csvファイルの使い方
#######################################
import csv

# 引数としてファイル名が与えられたときにそのファイルを
# csvファイルだと思って開き、3列目に書かれている整数の和を返せ

# 例：
#  a,10,2
#  b,11,3
#  c,12,4 => 9 (= 2+3+4)

# 以下を書きかえる


def f3(filename):
    return 0
# ここまでを書きかえる


filename = "quiz07.tmp"
with open(filename, "w") as fp:
    fp.write("2\n3")
assert f1(filename) == 5
with open(filename, "w") as fp:
    fp.write("abc\ndef\nxyz")
assert f2(filename) == "xyz"
with open(filename, "w") as fp:
    fp.write("1,2,3\n4,5,6\n7,8,9")
assert f3(filename) == 18

print("OK")
