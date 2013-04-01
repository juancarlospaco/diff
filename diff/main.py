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
from os import linesep
from subprocess import check_output as getoutput  # lint:ok

from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QDockWidget
from PyQt4.QtGui import QToolBar
from PyQt4.QtGui import QAction
from PyQt4.QtGui import QFileDialog
<<<<<<< HEAD
from PyQt4.QtGui import QMessageBox

from PyQt4.QtCore import QUrl
=======
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QCursor
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QGroupBox
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QMessageBox

from PyQt4.QtCore import Qt
>>>>>>> 2d27414adc5a1390490919535be1fe3b54709558

try:
    from PyKDE4.kdecore import *
    from PyKDE4.kparts import *
except ImportError:
    pass

from ninja_ide.core import plugin

from .diffgui import DiffGUI as Diff_GUI


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
<<<<<<< HEAD
        self.diff.triggered.connect(self.run_gui_and_get_results)
        self.save = QAction(QIcon.fromTheme("document-save"), 'Save DIFF', self)
        self.save.triggered.connect(self.save_a_diff)
        self.patc = QAction(QIcon.fromTheme("document-edit"), 'PATCH it!', self)
        self.patc.triggered.connect(lambda: QMessageBox.information(self.dock,
            __doc__, ' Sorry. This Feature is not ready yet !, thank you... '))
        QToolBar(self.dock).addActions((self.open, self.diff,
                                        self.save, self.patc))
=======
        QToolBar(self.dock).addActions((self.open, self.diff))
>>>>>>> 2d27414adc5a1390490919535be1fe3b54709558
        try:
            self.factory = KPluginLoader("komparepart").factory()
            self.part = self.factory.create(self)
            self.dock.setWidget(self.part.widget())
            self.open.triggered.connect(lambda: self.part.openUrl(KUrl(str(
                QFileDialog.getOpenFileName(self.dock, ' Open a DIFF file ',
                                        path.expanduser("~"), ';;(*.diff)')))))
<<<<<<< HEAD
=======
            self.diff.triggered.connect(self.make_diff)
>>>>>>> 2d27414adc5a1390490919535be1fe3b54709558
        except:
            self.dock.setWidget(QLabel(""" <center>
            <h3>ಠ_ಠ<br> ERROR: Please, install Kompare App ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Apps). </i><center>"""))

        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.dock,
                                QIcon.fromTheme("edit-select-all"), __doc__)

<<<<<<< HEAD
    def run_gui_and_get_results(self):
        ' run_gui_and_get_results '
        gui = Diff_GUI()
        if gui.diff_path is not None and path.isfile(gui.diff_path) is True:
            self.part.openUrl(KUrl(str(gui.diff_path)))
        return gui.diff_path

    def save_a_diff(self):
        ' save a diff '
        out_file = path.abspath(str(QFileDialog.getSaveFileName(self.dock,
                   'Save a Diff file', path.expanduser("~"), ';;(*.diff)')))
        inp_file = file(str(QUrl(
               self.part.url()).toString()).replace('file://', ''), 'r').read()
        end_file = file(out_file, 'w')
        end_file.write(inp_file)
        end_file.close()
=======
###############################################################################

    def make_diff(self):
        ' make a diff method with GUI '
        dialog = QDialog(self.dock)

        group1 = QGroupBox()
        group1.setTitle('Diff')
        frmt = QComboBox(group1)
        frmt.addItems(['Unified', 'Normal', 'Context'])
        bcknd = QComboBox(group1)
        bcknd.addItems(['diff', 'diff.py'])
        bcknd.setDisabled(True)  #TODO this feature needs work
        wdth = QComboBox(group1)
        wdth.addItems(['80', '90', '100', '120', '130', '250', '500', '999'])
        tbs = QComboBox(group1)
        tbs.addItems(['4', '6', '8', '10', '2'])
        nice = QComboBox(group1)
        nice.addItems(['20', '15', '10', '5', '0'])
        file1 = QLineEdit()
        file1.setPlaceholderText('/full/path/to/one_file.py')
        file2 = QLineEdit()
        file2.setPlaceholderText('/full/path/to/another_file.py')
        regex = QLineEdit()
        regex.setPlaceholderText('Do NOT use unless you know what are doing')
        borig = QPushButton(QIcon.fromTheme("folder-open"), 'Open')
        bmodi = QPushButton(QIcon.fromTheme("folder-open"), 'Open')
        vboxg1 = QVBoxLayout(group1)
        for each_widget in (QLabel('Original'), file1, borig,
                            QLabel('Modified'), file2, bmodi,
                            QLabel('Diff Output Format'), frmt,
                            QLabel('Diff Backend (EXPERIMENTAL)'), bcknd,
                            QLabel('Diff Maximum Total Width'), wdth,
                            QLabel('Diff Tabs-to-Spaces Size'), tbs,
                            QLabel('Diff Backend CPU Priority'), nice,
                            QLabel('Diff REGEX to Ignore (ADVANCED)'), regex):
            vboxg1.addWidget(each_widget)
            each_widget.resize(each_widget.size().width() * 2,
                               each_widget.size().height())

        group2 = QGroupBox()
        group2.setTitle('Options')
        nwfl = QCheckBox('Treat new files as Empty', group2)
        smll = QCheckBox('Look for smaller changes', group2)
        lrgf = QCheckBox('Optimize for large files', group2)
        case = QCheckBox('Ignore case changes on content', group2)
        cnvt = QCheckBox('Convert Tabs to Spaces', group2)
        blnk = QCheckBox('Ignore added or removed Blank lines', group2)
        spac = QCheckBox('Ignore changes in amount of Spaces', group2)
        whit = QCheckBox('Ignore ALL white Spaces', group2)
        tabz = QCheckBox('Ignore changes by Tab expansions', group2)
        lolz = QCheckBox('Output DIFF in two equal columns', group2)
        sprs = QCheckBox('Remove Space or Tab before empty lines', group2)
        pret = QCheckBox('Align all Tabs by prepending a Tab', group2)
        filn = QCheckBox('Ignore case when comparing file names', group2)
        plai = QCheckBox('Force treat all files as plain text', group2)
        nocr = QCheckBox('Force strip trailing carriage return', group2)
        ridt = QCheckBox('Report when two files are identical', group2)
        nocm = QCheckBox('Do not output common lines', group2)
        rdif = QCheckBox('Report only when files differ', group2)
        clip = QCheckBox('Copy Diff to Clipboard when done', group2)
        noti = QCheckBox('Use system Notification when done', group2)
        for widget_should_be_checked in (nwfl, smll, lrgf, cnvt, plai, noti):
            widget_should_be_checked.setChecked(True)
        vboxg2 = QVBoxLayout(group2)
        for each_widget in (nwfl, smll, lrgf, case, cnvt, blnk, spac, whit,
                            tabz, lolz, sprs, pret, filn, plai, nocr, ridt,
                            nocm, rdif, clip, noti):
            vboxg2.addWidget(each_widget)
            each_widget.setToolTip(each_widget.text())
            each_widget.setCursor(QCursor(Qt.PointingHandCursor))

        container = QWidget()
        hbox = QHBoxLayout(container)
        for each_widget in (group1, group2):
            hbox.addWidget(each_widget)

        buttons = QDialogButtonBox()
        buttons.resize(dialog.size().width(), buttons.size().height() * 2)
        buttons.setOrientation(Qt.Horizontal)
        buttons.setStandardButtons(
            QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel |
            QDialogButtonBox.Close |
            QDialogButtonBox.Help)
        buttons.setCenterButtons(False)
        buttons.helpRequested.connect(lambda: QMessageBox.about(dialog, __doc__,
            ''.join((__doc__, ' GUI and Visualizer Plugin,', linesep,
            'version ', __version__, ', (', __license__, '), by ', linesep,
            __author__, ', ( ', __email__, ' ).', linesep))))
        buttons.rejected.connect(dialog.close)
        # buttons.accepted.connect()

        info = QLabel(''.join(('<b> Current Backend Diff Engine: </b>',
                      getoutput('diff --version', shell=True).split(linesep)[0]
        )))

        vbox = QVBoxLayout(dialog)
        for each_widget in (
                QLabel('<center><h2> Ninja IDE Diff and Patch </h2></center>'),
                container, info, buttons):
            vbox.addWidget(each_widget)

        dialog.resize(self.dock.size().width() / 2, dialog.size().height())
        dialog.exec_()
>>>>>>> 2d27414adc5a1390490919535be1fe3b54709558


###############################################################################


if __name__ == "__main__":
    print(__doc__)
