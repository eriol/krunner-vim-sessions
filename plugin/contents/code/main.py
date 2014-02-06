# coding: utf-8

import os

from PyKDE4 import plasmascript
from PyKDE4.plasma import Plasma
from PyKDE4.kdeui import KIcon

DEFAULT_SESSION_DIRECTORY = '~/.vim/sessions/'
DEFAULT_SESSION_DIRECTORY = os.path.expanduser(DEFAULT_SESSION_DIRECTORY)


class VimRunner(plasmascript.Runner):

    def init(self):
        self.addSyntax(Plasma.RunnerSyntax('vim :s:',
                                           'Start Vim using :s: session.'))

    def match(self, context):
        if not context.isValid():
            return

        query = context.query()

        # Don't use query.startsWith('vim ') because we want the
        # list of all sessions to show up once inserted 'vim'.
        # The space between plugin keywork and text query must be
        # handled manually.
        if not query.startsWith('vim'):
            return
        try:
            if query[3] != ' ':
                return
        except IndexError:
            pass

        query = query[4:]
        query = query.trimmed()

        for _, _, sessions in os.walk(DEFAULT_SESSION_DIRECTORY):
            for session in sessions:
                # Skip lock files.
                if session.endswith('.lock'):
                    continue
                session = session[:-4]
                # Search is case insensitive.
                if str(query).lower() in session.lower():
                    m = Plasma.QueryMatch(self.runner)
                    m.setText(session)
                    m.setSubtext('Open Vim session')
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
