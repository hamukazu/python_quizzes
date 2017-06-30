#######################################
# Counterクラスの使い方
#######################################

from collections import Counter

# 引数に単語のリストが与えられたときに、各単語の出現数を表すCounterオブジェクトを返せ
# 例：["a","b","a","b","c"] => Counter({"a":3, "b":2, "c":1})

# 以下を書きかえる


def f1(l):
    return Counter()
# ここまでを書きかえる


#######################################
# 正規表現
#######################################

import re
# 引数として与えらた文字列の行頭からスペースまでを削除したものを返せ
# 例："abcd efg" => "efg"

# 以下を書きかえる


def g1(s):
    return ""
# ここまでを書きかえる

# 引数として与えらた文字列の行末から続く英小文字の並びを削除したものを返せ
# 例：
#  "abcDefg" => "abcD"
#  "abc1234efg" => "abc1234"

# 以下を書きかえる


def g2(s):
    return ""
# ここまでを書きかえる


c = f1(list("abcabcabcadef"))
assert (c["a"] == 4 and c["b"] == 3 and c["c"] == 3
        and c["d"] == 1 and c["e"] == 1 and c["f"] == 1)
assert g1("xyz abc") == "abc"
assert g2("xyz!abc") == "xyz!"
print("OK")
