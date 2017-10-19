# -*- coding: utf-8 -*-
import json

def make_url(self):
    keyboard = {}
    ia = []

    for i in self:
        ia.append(i)

    keyboard['inline_keyboard'] = ia
    return json.dumps(keyboard)