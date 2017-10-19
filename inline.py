# -*- coding: utf-8 -*-
import json

def inline_keyboard(self):
    keyboard = {}
    ia = []

    for i in self:
        ia.append(i)

    keyboard['inline_keyboard'] = ia
    return json.dumps(keyboard)