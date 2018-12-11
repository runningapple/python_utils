#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'runningapple'

import os

path = "E:/blog/site/content"
# path = "E:/blog"


def read_all_file_name():
    """读取文件夹下的所有文件名"""
    docs = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('md'):
            docs.append(file)
    return docs


def process_replace(filename):
    data = ''
    with open(path + "/" + filename, 'r+', encoding='utf-8') as f:
        for line in f.readlines():
            if line.find('date') == 0:
                line += 'Modified: ' + line[5:]
            elif line.find('categories') == 0:
                line = 'category: ' + line[11:]
            elif line.find('tags') == 0:
                line = 'tags: ' + line[7:-2]
                line += '\nSlug: ' + filename[:-3] + '\nAuthor: 苍南竹竿君\n'
            data += line

    f = open(path + "/" + filename, 'w', encoding='utf-8')
    f.write(data)
    f.close()


def batch_replace_word():
    """批量修改文件程序"""
    files = read_all_file_name()
    for file in files:
        process_replace(file)


batch_replace_word()
