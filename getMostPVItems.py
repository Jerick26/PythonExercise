#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} in_file out_file pv_th"
              .format(sys.argv[0]))
        sys.exit(-1)
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    pv_th = int(sys.argv[3])
    if not os.path.exists(in_file):
        print("in file not exists")
        sys.exit(-1)
    if not os.path.exists(os.path.dirname(out_file)):
        print("out file directory not exist")
        sys.exit(-1)
    outLines = []
    with open(in_file) as fp:
        lastid = ""
        PV = 0
        chunk = ""
        for line in fp:
            fields = line.split("\t")
            if len(fields) != 5:
                continue

            if fields[2].strip() == "PV":
                try:
                    PV = int(fields[4].strip())
                except ValueError:
                    print(line)

            if lastid != fields[0].strip():
                lastid = fields[0].strip()
                if PV >= pv_th:
                    outLines.append(chunk + "\n")
                chunk = ""
                PV = 0
            chunk += line

    step = 10000
    with open(out_file, "w") as fp:
        for i in range(0, len(outLines), step):
            fp.writelines(outLines[i:i+step])
        if len(outLines) % step > 0:
            start = len(outLines)/step*step
            fp.writelines(outLines[start:])
