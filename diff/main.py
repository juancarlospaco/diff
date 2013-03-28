# -*- coding: utf-8 -*-
# PEP8:OK, LINT:OK, PY3:OK


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
" NINJA-IDE Diff and Patch "
__version__ = ' 0.1 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@ubuntu.com '
__url__ = ''
__date__ = ' 25/04/2013 '
__prj__ = ' diff '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
from os import path

from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QDockWidget
from PyQt4.QtGui import QToolBar
from PyQt4.QtGui import QAction
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QScrollArea
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QCursor
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QDialog

try:
    from PyKDE4.kdecore import *
    from PyKDE4.kparts import *
except ImportError:
    pass

from ninja_ide.core import plugin


###############################################################################


class Main(plugin.Plugin):
    " dock Class "
    def initialize(self):
        " Init Class dock "
        self.dock = QDockWidget()
        self.dock.setFeatures(QDockWidget.DockWidgetFloatable |
                                           QDockWidget.DockWidgetMovable)
        self.dock.setWindowTitle(__doc__)
        self.dock.setStyleSheet('QDockWidget::title{text-align: center;}')
        self.open = QAction(QIcon.fromTheme("document-open"), 'Open DIFF', self)
        self.diff = QAction(QIcon.fromTheme("document-new"), 'Make DIFF', self)
        QToolBar(self.dock).addActions((self.open, self.diff))
        try:
            self.factory = KPluginLoader("komparepart").factory()
            self.part = self.factory.create(self)
            self.dock.setWidget(self.part.widget())
            self.open.triggered.connect(lambda: self.part.openUrl(KUrl(str(
                QFileDialog.getOpenFileName(self.dock, ' Open a DIFF file ',
                                        path.expanduser("~"), ';;(*.diff)')))))
            self.diff.triggered.connect(self.make_diff)
        except:
            self.dock.setWidget(QLabel(""" <center>
            <h3>ಠ_ಠ<br> ERROR: Please, install Kompare App ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Apps). </i><center>"""))

        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.dock,
                                QIcon.fromTheme("edit-select-all"), __doc__)

    def make_diff(self):
        ' make a diff method with GUI '
        dialog = QDialog(self.dock)
        # widgets
        frmt = QComboBox()
        frmt.addItems(['Unified', 'Normal', 'Context'])
        bcknd = QComboBox()
        bcknd.addItems(['diff', 'diff.py'])
        bcknd.setDisabled(True)  #TODO this feature needs work
        wdth = QComboBox()
        wdth.addItems(['80', '90', '100', '120', '130', '250', '500', '999'])
        tbs = QComboBox()
        tbs.addItems(['4', '6', '8', '10', '2', 'NO replace Tabs with Spaces'])
        ignr = QComboBox()
        ignr.addItems(['NO ignore all spaces, tabs, and blanks changes',
                       'Ignore case differences in file contents only',
                       'Ignore case differences, and spaces at line end',
                       'Ignore case, spaces at end, and amount of spaces',
                       'Ignore all spaces, tabs, and blanks changes'
        ])


        # list
        widget_list = (
            QLabel(' <h3> Ninja-IDE Diff and Patch <h3> '),
            QLabel('Original'),
            QLineEdit(),
            QLabel(''),
            QLabel('Modified'),
            QLineEdit(),
            QLabel(''),
            QLabel('Output Format'),
            frmt,
            QLabel(''),
            QLabel('Diff Backend (EXPERIMENTAL)'),
            bcknd,
            QLabel(''),
            QLabel('Diff Maximum Total Width'),
            wdth,
            QLabel(''),
            QLabel('Diff Tabs-to-Spaces Size'),
            tbs,
            QLabel(''),
            QLabel('Diff Ignore Tabs, Spaces and Blanks'),
            ignr,



            QLabel(''),
        )
        # pack to gui
        vbox = QVBoxLayout(dialog)
        for each_widget in widget_list:
            vbox.addWidget(each_widget)
        # resize and show
        # dialog.resize(self.dock.size().width() / 2, dialog.size().height())
        dialog.exec_()






###############################################################################


if __name__ == "__main__":
    print(__doc__)
