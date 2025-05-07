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
                ('dec', 'py', 'by'),  # by = py - 1, assuming decreasing y is up
                ('at', 't', 'px', 'py'),  # Taxi is at current position
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),  # Remove old position
                ('at', 't', 'px', 'by'),       # Set new position
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
                ('at', 't', 'px', 'py'),  # Taxi is at position
                ('free', 't'),
                ('at', 'p', 'px', 'py'),  # Passenger is at same position
            ),
            effects=(
                neg(('at', 'p', 'px', 'py')),  # Passenger no longer at position
                neg(('free', 't')),
                ('on_taxi', 'p'),  # Passenger is now in taxi
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
                ('at', 't', 'px', 'py'),  # Taxi is at position
                neg(('free', 't')),
                ('on_taxi', 'p'),  # Passenger is in taxi
            ),
            effects=(
                neg(('on_taxi', 'p')),  # Passenger no longer in taxi
                ('at', 'p', 'px', 'py'),  # Passenger now at taxi's position
                ('free', 't')
            ),
        ),
    ))
    return domain