# -*- coding: utf-8 -*-
import json

def make_url(self):
    keyboard = {}
    add = []

    for i in self:
        add.append(i)

    keyboard['inline_keyboard'] = add
    return json.dumps(keyboard)
