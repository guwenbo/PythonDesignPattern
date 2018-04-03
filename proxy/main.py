#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from proxy import *

if __name__ == '__main__':
    sub = RealSubject()
    p = Proxy(sub)
    p.request()
