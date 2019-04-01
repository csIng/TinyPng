# encoding:utf-8

import sys
import getopt
import os
import tinify


def tiny(argv):
    server_key = ''
    in_file = ''
    out_file = ''
    try:
        opts, args = getopt.getopt(argv, 'hk:i:o:', ["k=", "ifile=", "ofile="])
    except getopt.GetoptError:
        print_help()
    for opt, arg in opts:
        if opt == '-h':
            print_help()
        elif opt in ("-k", "--k"):
            server_key = arg
        elif opt in ("-i", "--ifile"):
            in_file = arg
        elif opt in ("-o", "-ofile"):
            out_file = arg
    if not server_key:
        print_help()

    print("start")
    if os.path.isfile(in_file) and os.path.isfile(out_file):
        tiny_file(server_key, in_file, out_file)
    elif os.path.isdir(in_file) and os.path.isdir(out_file):
        in_files = os.listdir(in_file)
        for file in in_files:
            tiny_file(server_key, os.path.join(in_file, file), os.path.join(out_file, file))

    print("end")


def tiny_file(server_key, in_file, out_file):
    print("compressing in:" + in_file + '\t' + 'out:' + out_file)
    tinify.key = server_key
    tinify.from_file(in_file).to_file(out_file)


def print_help():
    print('TinyPng.py -k <tiny server key> -i <input> -o <output>')
    sys.exit(2)


if __name__ == '__main__':
    tiny(sys.argv[1:])
