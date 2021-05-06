from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import*


app = QApplication([])
w1 = QWidget()
w1.show()
w1.setWindowTitle('Memory Card')
w1.resize(500, 300)
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

qlist = list()
qlist.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
qlist.append(Question('Самая высокая горная вершина мира', 'Эверест', 'Бештау', 'Машук', 'Альпы'))
qlist.append(Question('Полное безветрие на море', 'Штиль', 'Шторм', 'Тайфун', 'Цунами'))
qlist.append(Question('Как называется веревка с петлей на конце?', 'Лассо', 'Канат', 'Кнут', 'Бичевка'))
qlist.append(Question('Ягода ярко-малинового цвета', 'Малина', 'Клубника', 'Арбуз', 'Черника'))
qlist.append(Question('Подставка для фотоаппарата', 'Штатив', 'Стойка', 'Палка', 'Держалка'))
qlist.append(Question('Дикий предок собаки', 'Волк','Лис', 'Лев', 'Кайот'))
qlist.append(Question('Бог морей, управляющий ими с помощью трезубца', 'Посейдон', 'Аид', 'Зевс', 'Дионис'))
qlist.append(Question('Пустыня в Африке', 'Сахара', 'Мисисипи', 'Танзания', 'Арктика'))
qlist.append(Question('Отец отца или матери', 'Дедушка', 'Дядя', 'Внук', 'Сын'))

text = QLabel('Какой национальности не существует?')


butn_ok = QPushButton('Ответить')
butn_ok.stretch = 1

r = QGroupBox('Варианты ответов')
o = QGroupBox('Резульат')

ol = QLabel('Молодец')
v4 = QVBoxLayout()
v4.addWidget(ol)
o.setLayout(v4)

a1 = QRadioButton('Энцы')
a2 = QRadioButton('Чулымцы')
a3 = QRadioButton('Смурфы')
a4 = QRadioButton('Алеуты')

but = QButtonGroup()
but.addButton(a1)
but.addButton(a2)
but.addButton(a3)
but.addButton(a4)

h1 = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QVBoxLayout()

v2.addWidget(a1)
v2.addWidget(a2)
v3.addWidget(a3)
v3.addWidget(a4)
h1.addLayout(v2)
h1.addLayout(v3)
r.setLayout(h1)

o.hide()
v1.addWidget(text)
v1.addWidget(r)
v1.addWidget(o)
v1.setSpacing(50)
v1.addWidget(butn_ok)
w1.setLayout(v1)

answers = [a1, a2, a3, a4]

def win():
    butn_ok.setText('Следуюший вопрос')
    r.hide()
    o.show()
def win2():
    butn_ok.setText('Ответить')
    o.hide()
    r.show()
    but.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    but.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)

    win2()

def show_correct(res):
    ol.setText(res)
    win()
w1.a = 1
w1.a = float(w1.a)
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        w1.a = w1.a + 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

w1.i = 0
w1.i = float(w1.i)
s = 1
s = float(s)
def next_question():
    w1.i = w1.i + 1
    po = randint(0, len(qlist)-1)
    q = qlist[po]
    ask(q)
    s = w1.a / w1.i * 100
    print('Статистика:')
    print('Всего вопросов: ' + str(w1.i))
    print('Правильных ответов: ' + str(w1.a))
    print('Рейтинг: '+ str(s) )


def click_ok():
    if butn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


butn_ok.clicked.connect(click_ok)
next_question()




app.exec_()