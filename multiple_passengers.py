from __future__ import print_function
from pyddl import Domain, Action, neg

def create_domain_multiple_passengers():
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
                ('dec', 'py', 'by'),  # by = py - 1 (up decreases y)
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
                ('inc', 'py', 'by'),  # by = py + 1 (down increases y)
                ('at', 't', 'px', 'py'),  # Taxi is at current position
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),  # Remove old position
                ('at', 't', 'px', 'by'),       # Set new position
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
                ('dec', 'px', 'bx'),  # bx = px - 1 (left decreases x)
                ('at', 't', 'px', 'py'),  # Taxi is at current position
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),  # Remove old position
                ('at', 't', 'bx', 'py'),       # Set new position
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
                ('inc', 'px', 'bx'),  # bx = px + 1 (right increases x)
                ('at', 't', 'px', 'py'),  # Taxi is at current position
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),  # Remove old position
                ('at', 't', 'bx', 'py'),       # Set new position
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
                ('at', 'p', 'px', 'py'),  # Passenger is at same position
            ),
            effects=(
                neg(('at', 'p', 'px', 'py')),  # Passenger no longer at position
                ('on_taxi', 'p'),              # Passenger is on taxi
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
                ('on_taxi', 'p'),         # Passenger is on taxi
            ),
            effects=(
                neg(('on_taxi', 'p')),    # Passenger no longer on taxi
                ('at', 'p', 'px', 'py'),  # Passenger now at position
            ),
        ),
    ))
    return domain