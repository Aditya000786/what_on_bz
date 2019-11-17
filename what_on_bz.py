#!/usr/bin/env python2

from argparse import ArgumentParser
from datetime import datetime, timedelta
import urllib.parse

URL = 'https://bugzilla.mozilla.org/buglist.cgi'

LAST_WEEK_PARAMS = {
    'query_format': 'advanced',
    'chfield': 'bug_status',
    'bug_status': 'RESOLVED',
    'chfieldvalue': 'RESOLVED',
    'chfieldto': 'Now',
    'emailtype1': 'equals',
    'emailassigned_to1': '1',
}

# TODO: Declare NEW or ASSIGNED bug status.
PRESENT_PARAMS = {
    'query_format': 'advanced',
    'emailtype1': 'equals',
    'emailassigned_to1': '1',
}

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('email', help='email address of changes')
    return parser.parse_args()


def get_date_str(daydelta):
    """Returns YYYY-MM-DD"""
    seven_days_ago = (datetime.now() - timedelta(days=daydelta)).strftime('%Y-%m-%d')
    return str(seven_days_ago)


def get_url_for_params(static_params, dynamic_params):
    out_params = static_params.copy()
    out_params.update(dynamic_params)
    return URL + '?' + urllib.parse.urlencode(out_params)


args = parse_arguments()
dynamic_params = {
    'email1': args.email,
    'chfieldfrom': get_date_str(7)
}

print('PAST: ' + get_url_for_params(LAST_WEEK_PARAMS, dynamic_params))
print('')  # newline.
print('PRESENT: ' + get_url_for_params(PRESENT_PARAMS, dynamic_params))
print('')  # newline

dynamic_params['chfieldfrom'] = get_date_str(2)

print('MIDWEEK PAST: ' + get_url_for_params(LAST_WEEK_PARAMS, dynamic_params))
print('')  # newline.
print('MIDWEEK PRESENT: ' + get_url_for_params(PRESENT_PARAMS, dynamic_params))
print('')  # newline
