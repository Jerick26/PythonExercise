#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json


class Item(object):

    def __init__(self, rel, label):
        self.Rel = rel
        self.Label = label

    def ExtractObj(self, line):
        elems = line.split("\t")
        item = Item(elems[0], elems[1].strip())
        return item


def jsonDefault(object):
    return object.__dict__


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} in_file out_file".format(sys.argv[0]))
        sys.exit(-1)
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    if not os.path.exists(os.path.dirname(out_file)):
        print("out file directory not exist")
        sys.exit(-1)
    items = []
    item = Item("", "")
    with open(in_file, 'r') as f:
        for line in f:
            node = item.ExtractObj(line)
            if node is None:
                continue
            items.append(node)
    with open(out_file, 'w') as f:
        json.dump(items, f, ensure_ascii=False, indent=4, separators=(',', ': '),
                  default=jsonDefault)
