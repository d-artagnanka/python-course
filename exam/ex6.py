"""Реалізуйте клас "стек" (задача на ООП)

Операції для стеку:

push («заштовхнути елемент»): елемент додається в стек та розміщується в його верхівці. Розмір стека збільшується на одиницю. При перевищенні розміру стека граничної величини, відбувається переповнення стека .

pop («виштовхнути елемент»): отримує елемент з верхівки стека. При цьому він видаляється зі стека і його місце в верхівці стека займає наступний за ним відповідно до правила LIFO, а розмір стека зменшується на одиницю. При намаганні «виштовхнути» елемент з вже пустого стека, відбувається ситуація «незаповненість» стека (англ. stack underflow). Кожна з цих операцій зі стеком виконується за фіксований час O(1) і не залежить від розміру стеку.

Додаткові операції:

isEmpty: перевірка наявності елементів в стека; результат: істина (true), коли стек порожній.

isFull: перевірка заповненості стека. Результат: істина, коли додавання нового елементу неможливе.

clear: звільнити стек (видалити усі елементи).

top: отримати верхній елемент (без виштовхування).

size: отримати розмір (кількість елементів) стека."""

class Stack:
    pass
