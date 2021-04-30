from PyQt5 import uic, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel
import sys

"""программа открывает БД, показывает полный путь до нее.
Можно выбирать таблицы из БД, и редактировать записи. Меняется в т.ч. БД.
Возможность добавлять/удалять записи в таблицах не реализована.
"""


Form, _ = uic.loadUiType("test.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_file_path)  # обработчик нажатия кнопки
        self.comboBox.currentTextChanged.connect(self.get_item_combo_box)  # обработчик comboBox

    def db_connect(self, filename):  # подключаемся к БД
        conn = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        conn.setDatabaseName(filename)
        # print(conn.databaseName())
        # print(conn.connectionName())
        conn.open()
        tables_list = conn.tables()[:]  # список всех таблиц в выбранной БД
        tables_list.remove("sqlite_sequence")  # удаляем служебную таблицу
        self.combo_box(tables_list)

    def combo_box(self, tables_list):
        self.comboBox.clear()  # при смене БД комбобокс очищаем
        self.comboBox.addItems(tables_list)

    def get_item_combo_box(self):  # получаем имя текущей таблицы и передаем его в загрузку в tableView
        current_db = self.comboBox.currentText()
        # print(self.comboBox.currentText())
        self.load_table(current_db)

    def load_table(self, current_db):
        model = QSqlTableModel()
        model.setTable(f"{current_db}")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)  # указываем стратегию (можно менять данные)
        self.tableView.setModel(model)
        model.select()

    def get_file_path(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл БД", "", "*.db *.sqlite *.sqlite3")
        if filename[0]:  # если нажата кнопка ОТМЕНА, то будет пустой путь
            self.label.setText((filename[0]))
            self.db_connect(filename[0])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec())
