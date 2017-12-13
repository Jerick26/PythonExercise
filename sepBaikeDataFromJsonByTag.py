#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf8')

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
    with codecs.open(in_file, 'rU', 'utf-8', 'strict', 0) as fp:
        for line in fp:
            try:
                v = json.loads(line)
            except ValueError:
                print(line)
            tag = v['custom_tag']
            if ent_dict.get(tag) is None:
                ent_dict[tag] = []
            ent_dict[tag].append(v['title']+"\t"+str(v['pv'])+"\n")
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
