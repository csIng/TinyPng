# encoding:utf-8

import sys
import getopt
import os
import tinify


class Params(object):
    server_key = ''
    input_file = ''
    output_file = ''


def is_invalid(params):
    return not params or not params.server_key or not params.input_file


def get_files(params):
    input_files = []
    output_files = []
    if os.path.isfile(params.input_file):
        input_files.append(params.input_file)
        output_files.append(params.output_file)

    elif os.path.isdir(params.input_file) and not os.path.exists(params.output_file):
        os.mkdir(params.output_file)

    if os.path.isdir(params.input_file) and os.path.isdir(params.output_file):
        in_files = os.listdir(params.input_file)
        for file in in_files:
            input_files.append(os.path.join(params.input_file, file))
            output_files.append(os.path.join(params.output_file, file))
    return input_files, output_files


def tiny(argv):
    p = parse_params(argv)
    if is_invalid(p):
        print('input file not exists')
        print_help()

    print("start")
    input_files, output_files = get_files(p)
    if not input_files or not output_files:
        print_help()
    for i, input_file in enumerate(input_files):
        tiny_file(p.server_key, input_file, output_files[i])
    print("end")


def parse_params(argv):
    result = Params
    try:
        opts, args = getopt.getopt(argv, 'hk:i:o:', ["k=", "ifile=", "ofile="])
        for opt, arg in opts:
            if opt == '-h':
                print_help()
            elif opt in ("-k", "--k"):
                result.server_key = arg
            elif opt in ("-i", "--ifile"):
                result.input_file = arg
            elif opt in ("-o", "-ofile"):
                result.output_file = arg
    except getopt.GetoptError:
        pass
    return result


def tiny_file(server_key, in_file, out_file):
    print("compressing in:" + in_file + '\t' + 'out:' + out_file)
    tinify.key = server_key
    tinify.from_file(in_file).to_file(out_file)


def print_help():
    print('TinyPng.py -k <tiny server key> -i <input> -o <output>')
    sys.exit(2)


if __name__ == '__main__':
    tiny(sys.argv[1:])
