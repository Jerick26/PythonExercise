#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} in_file out_dir".format(sys.argv[0]))
        sys.exit(-1)
    in_file = sys.argv[1]
    out_dir = sys.argv[2]
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    if not os.path.exists(out_dir):
        print("out directory not exist")
        sys.exit(-1)
    ent_dict = {}
    with open(in_file) as fp:
        for line in fp:
            fields = line.split("\t")
            if ent_dict.get(fields[2]) is None:
                ent_dict[fields[2]] = []
            ent_dict[fields[2]].append(fields[1]+"\t"+fields[4])
    for k, v in ent_dict.iteritems():
        out_fp = open(out_dir + "/百科" + k + ".txt", 'w')
        out_lines = []
        for ln in v:
            out_lines.append(ln)
            if len(out_lines) == 1000:
                out_fp.writelines(out_lines)
                out_lines[:] = []
        if len(out_lines) > 0:
            out_fp.writelines(out_lines)
        out_fp.close()
