#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json


class Item(object):

    def __init__(self, name, key, val):
        self.Name = name
        self.Key = key
        self.Val = val

    def ExtractObj(self, line, key):
        elems = line.split("\t")
        if elems[2] == key:
            item = Item(elems[1], elems[2], elems[4].strip().replace("", ","))
            return item
        return None


def jsonDefault(object):
    return object.__dict__


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} in_file out_file key step".format(sys.argv[0]))
        sys.exit(-1)
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    key = sys.argv[3]
    step = int(sys.argv[4])
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    if not os.path.exists(os.path.dirname(out_file)):
        print("out file directory not exist")
        sys.exit(-1)
    items = []
    item = Item("", "", "")
    with open(in_file, 'r') as f:
        count = 0
        for line in f:
            count += 1
            if count < step:
                continue
            node = item.ExtractObj(line, key)
            if node is None:
                continue
            items.append(node)
            count = 0
    with open(out_file, 'w') as f:
        json.dump(items, f, indent=4, separators=(',', ': '), encoding="utf-8",
                  default=jsonDefault)
