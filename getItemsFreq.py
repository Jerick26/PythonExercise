#!/usr/bin/env python
# -*- coding: utf-8 -*-

# input format
#
# name,地域,id,性别,QQPV,风格	246511
# name,地域,id,性别,QQPV	238635
# name,民族,中文名,国籍,PV,简介,id,性别	31736
# 年龄,name,民族,中文名,出生日期,国籍,PV,简介,id,性别	24805
#
# output format
#
# total: 1584506
# id:	1584506	1.0000
# name:	1584506	1.0000
# 性别:	1264890	0.7983
# 简介:	1079249	0.6811

import sys
import os
from operator import itemgetter

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} in_file rate".format(sys.argv[0]))
        sys.exit(-1)
    in_file = sys.argv[1]
    rate = float(sys.argv[2])
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    prop_freq = {}
    total = 0
    with open(in_file) as fp:
        for line in fp:
            fields = line.split("\t")
            props = fields[0].split(",")
            total += int(fields[1])
            for v in props:
                if v not in prop_freq:
                    prop_freq[v] = 0
                prop_freq[v] += int(fields[1])
    # for k, v in prop_freq.items():
    #     print("prop: {0}:\t\t{1}".format(k, v))
    props_total = 0
    props = list((p, prop_freq.get(p)) for p in prop_freq)
    props.sort(key=itemgetter(1), reverse=True)
    for k, v in props:
        props_total += v
        rt = float(v)/total
        if rt < rate:
            continue
        print("{0}:\t{1}\t{2:6.4f}".format(k, v, rt))
    print("entities total count: {}, properties total count: {}"
          .format(total, props_total))
