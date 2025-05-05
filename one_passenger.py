from __future__ import print_function
from pyddl import Domain, Action, neg
from planner import planner


def create_domain_one_passenger():
    domain = Domain((
        Action(
            'move-up',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),  # Current location on the x-axis
                ('position', 'py'),  # Current location on the y-axis
                ('position', 'by'),  # New location on the y-axis
            ),
            preconditions=(
                ('dec', 'py', 'by'),  # by = py - 1
                ('at', 't', 'px', 'py'),  # TODO: shouldn't it be by instead of py?
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),  # TODO: and also in here
                ('at', 't', 'px', 'by'),
            ),
        ),
        Action(
            'move-down',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'by'),
            ),
            preconditions=(
                ('inc', 'py', 'by'),  # by = py + 1
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'px', 'by'),
            ),
        ),
        Action(
            'move-left',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'bx'),
            ),
            preconditions=(
                ('dec', 'px', 'bx'),  # bx = px - 1
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'bx', 'py'),
            ),
        ),
        Action(
            'move-right',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'bx'),
            ),
            preconditions=(
                ('inc', 'px', 'bx'),  # bx = px + 1
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'bx', 'py'),
            ),
        ),
        Action(
            'pick-up',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('passenger', 'p'),
            ),
            preconditions=(
                ('on_taxi', 'p'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(

            ),
        ),
        Action(
            'put-down',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('passenger', 'p'),
            ),
            preconditions=(
                ('free', 'p'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('on_taxi', 't'))
            ),
        ),
    ))
    return domain
