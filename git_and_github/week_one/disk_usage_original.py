#!/usr/bin/env python3

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there's enough space, False otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gb_free = du.free / 2**30
    if percent_free < min_percent or gb_free < min_absolute:
        return False
    return True

if not check_disk_usage('/', 2*2**30, 10):
    print('ERROR: Not enough disk space')
    # return 1

print('Everything ok')
# return 0
