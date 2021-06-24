# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Samuel Weibel <samuel.weibel@gmail.com>
#
"""
ioBroker scripts
"""

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from weblate.addons.events import EVENT_POST_UPDATE, EVENT_PRE_COMMIT
from weblate.addons.scripts import BaseScriptAddon

class GenerateWordsJS(BaseScriptAddon):
    # Event used to trigger the script
    events = (EVENT_PRE_COMMIT,)
    name = 'iobroker.weblate.gulp.adminLanguages2words'
    # Verbose name and long descrption
    verbose = _('ioBroker: Save translations into words.js')
    description = _('This addon runs "npm run translate adminLanguages2words" or "gulp adminLanguages2words" before a commit.')

    # Script to execute
    script = '/app/iobroker/python/weblate_iobroker/scripts/save-to-words.sh'
