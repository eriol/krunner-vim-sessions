# coding: utf-8

import os

from PyKDE4 import plasmascript
from PyKDE4.plasma import Plasma
from PyKDE4.kdeui import KIcon

DEFAULT_SESSION_DIRECTORY = '~/.vim/sessions/'
DEFAULT_SESSION_DIRECTORY = os.path.expanduser(DEFAULT_SESSION_DIRECTORY)


class VimRunner(plasmascript.Runner):

    def init(self):
        self.addSyntax(Plasma.RunnerSyntax('vim',
                                           'Start Vim using a session.'))

    def match(self, context):
        if not context.isValid():
            return

        query = context.query()
        if not query.startsWith('vim'):
            return

        # Search only after the fourth character.
        query = query[4:]
        query = query.trimmed()

        for _, _, sessions in os.walk(DEFAULT_SESSION_DIRECTORY):
            for session in sessions:
                session = session[:-4]
                # Search is case insensitive.
                if str(query).lower() in session.lower():
                    m = Plasma.QueryMatch(self.runner)
                    m.setText(session)
                    m.setSubtext('Open (g)Vim session')
                    m.setType(Plasma.QueryMatch.ExactMatch)
                    m.setIcon(KIcon('vim'))
                    m.setData(session)
                    context.addMatch(session, m)

    def run(self, context, match):
        if match.data():
            args = '--servername %s' % match.data().toString()
        else:
            args = ''

        os.system(' '.join(['gvim', args]))


def CreateRunner(parent):
    return VimRunner(parent)
