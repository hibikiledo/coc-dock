__author__ = 'Hibiki'

import subprocess

from models import Point

'''

    This function is a wrapper of python's subprocess.
    This is to provide pretty and origanized debug outputs.

'''
def pretty_subprocess(subprocess_list, script_name='', success_msg='Success', error_msg='Default error message'):

    print '-'*15, 'START OUTPUT FROM SCRIPT {}'.format(script_name), '-'*15

    exit_code = subprocess.check_call(subprocess_list)

    print '-'*15, 'END OUTPUT FROM SCRIPT {}'.format(script_name), '-'*15

    if exit_code == 0:
        print "[INFO]", success_msg
    else:
        print "[ERROR]", error_msg


'''

    This function prepares function call that will be passed to matlab cli

'''
def make_fn_call(fn_name, args):
    # wrap each arg in single quotes
    args = [ single_quote(arg) for arg in args ]
    # separate args with commas
    args_cs = ','.join(args)
    # join with fn_name
    return fn_name + '(' + args_cs + ')'


'''
    This function wraps input string with single quotes
'''
def single_quote(args):
    arg_list = list(args)
    arg_list.insert(0, "'")
    arg_list.append("'")
    return ''.join(arg_list)


def group_points(points):

    grouped = []

    for point in points:

        # fine any point that close to this point from the group
        close_point = point.closes_to(grouped, 5)

        # found a match
        if close_point is not None:
            # update value to average between the close 2 points
            p = avg_points([point, close_point])
            close_point.x = p.x
            close_point.y = p.y
        else:
            # no close point found, this is the first one!
            grouped.append(point)

    return grouped



def avg_points(points):

    sum_x = 0
    sum_y = 0

    for point in points:
        sum_x = sum_x + point.x
        sum_y = sum_y + point.y

    avg_x = sum_x / len(points)
    avg_y = sum_y / len(points)

    return Point(avg_x, avg_y)