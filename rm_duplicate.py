#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from sets import Set

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} duplicate_list_file in_file out_file"
              .format(sys.argv[0]))
        sys.exit(-1)
    # data_dir = /data01/kg_graph/rawdata/baike/baike_all_merge
    duplicate_list_file = sys.argv[1]
    in_file = sys.argv[2]
    out_file = sys.argv[3]
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    if not os.path.exists(os.path.dirname(out_file)):
        print("out file directory not exist")
        sys.exit(-1)
    dup_set = Set([])
    with open(duplicate_list_file) as fp:
        for line in fp:
            line = line.split("\t")[0].strip()
            dup_set.add(line)
    out_fp = open(out_file, 'w')
    out_list = []
    with open(in_file) as fp:
        for line in fp:
            elem = line.split("\t")[0].strip()
            if elem not in dup_set:
                out_list.append(line)
            if len(out_list) == 1000:
                out_fp.writelines(out_list)
                out_list[:] = []
    if len(out_list) > 0:
        out_fp.writelines(out_list)
    out_fp.close()
