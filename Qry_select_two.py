#!/usr/bin/env python
# coding: utf-8

from questionary import prompt

# prompt that asks user to type out answer for how long
time_response = [
    {
        'type': 'text',
        'name': 'time',
        'message': 'How long would you like to run your simulation?',
    },
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    }
]
time_answer = prompt(time_response)


#convert answer to float from string
time_float = float(time_answer)


#repeat for sim
sim_response = [
    {
        'type': 'text',
        'name': 'ammount',
        'message': 'How many simulations would you like to run per-day?',
    },
    {
        'type':, 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    }
]
sim_answer = prompt(sim_response)

time_float = float(sim_answer)