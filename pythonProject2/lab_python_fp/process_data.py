import json
import sys
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.print_result import print_result

path = sys.argv[1] if len(sys.argv) > 1 else "data_light.json"

import codecs

with open(path, 'rb') as f:
    data = json.loads(codecs.getdecoder('utf-8')(f.read())[0])

@print_result
def f1(data):
    return list(Unique([item["job-name"].lower() for item in list(field(data, "job-name"))], ignore_case=True))

@print_result
def f2(data):
    return list(filter(lambda x: x.startswith("программист"), data))

@print_result
def f3(data):
    return list(map(lambda x: x + " с опытом Python", data))

@print_result
def f4(data):
    return list(map(lambda x: x + ", зарплата " + str(next(gen_random(1, 100000, 200000))) + " руб.", data))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))