#!/usr/bin/env python
# coding:utf-8

__author__ = 'coderzh'

import os
import shutil


PUBLIC_DIR = 'public_test'


def publish():
    files = [the_file for the_file in os.listdir(PUBLIC_DIR) if the_file != '.git']
    for the_file in files:
        file_path = os.path.join(PUBLIC_DIR, the_file)
        if os.path.isfile(file_path):
            os.remove(os.path.join(PUBLIC_DIR, the_file))
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


if __name__ == '__main__':
    publish()
