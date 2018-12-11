#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'runningapple'

import sys
import time


def read_file_name():
    """获取用户输入的文件名"""
    try:
        return sys.argv[1] + '.md'
    except IndexError:
        print('please input file name')
    return None


def create_template():
    """创建markdown文件模板"""
    return '---' + \
           '\nTitle: YourBlogTitle' + \
           '\nDate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + \
           '\nModified: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + \
           '\nComments: false' + \
           '\nCategory: Category' + \
           '\nTags: Tags' + \
           '\nSlug: ' + sys.argv[1] + \
           '\nAuthor: 苍南竹竿君' + \
           '\nStatus: draft' + \
           '\n---'


def create_file(filename, template):
    """创建文件，并写入模板"""
    file = open(filename, mode='w')
    file.write(template)
    file.close()


def generate_md_file():
    """自动生成markdown文件"""
    filename = read_file_name()
    if filename is not None:
        template = create_template()
        create_file(filename, template)


generate_md_file()
