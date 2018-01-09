#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import collections


#def topKFrequent(strDict, k):
#    """
#    :type strs: List[str]
#    :type k: int
#    :rtype: List[str]
#    """
#    n = len(strDict)
#    freqList = [[] for i in range(n + 1)]
#    for p in strDict:
#        freqList[strDict[p]] += p
#    ret_list = []
#    for p in range(n, 0, -1):
#        ret_list += freqList[p]
#    return ret_list[:k]


def get_attr_freq(file_path):
    entity = ""
    attr = ""
    count = 0
    attr_freq = collections.defaultdict(int)
    # file = open(file_path)
    with open(file_path) as fp:
        for line in fp:
            elements = line.split("\t")
            if len(elements) != 5:
                continue
            if elements[4].strip() != "社会_交通_交通工具":
                continue
            if entity != elements[1]:
                entity = elements[1]
                attr = ""
                count += 1
            if attr != elements[2]:
                attr = elements[2]
                attr_freq[attr] += 1
    # file.close()
    return attr_freq, count


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: cmd + data_path + rate(0.0~1.0) + out_file")
        sys.exit(-1)
    # data_dir = /data01/kg_graph/rawdata/baike/baike_all_merge
    data_file = sys.argv[1]
    rate = float(sys.argv[2])
    out_file = sys.argv[3]
    if not os.path.exists(data_file):
        print("data file not exists")
        sys.exit(-1)
    if rate < 0 or rate > 1.0:
        print("rate set wrong")
        sys.exit(-1)
    attr_freq, total = get_attr_freq(data_file)
    print("get data file attributions frequence finish")
    # output
    if not os.path.exists(os.path.dirname(out_file)):
        print("out file directory not exist")
        sys.exit(-1)
    out = open(out_file, 'w')
    count = total * rate
    out_str = "Attributes more than {0:4.2f} in {1}\n".format(rate, total)
    for item in attr_freq:
        val = float(attr_freq[item])/total
        if val >= rate:
            out_str += "{0:6.3f}: {1:s}\n".format(val, item)
    # attr_list = topKFrequent(attr_freq, count)
    # for item in attr_list:
    #    out_str += "%6.3f: %s\n" % {attr_freq[item], item}
    out.write(out_str)
    print("writing attributions frequence to file done")
    out.close()
