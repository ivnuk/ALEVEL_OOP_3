Створити інтерактивну гру в консолі, що базується на принципі "камень-ножиці-бумага". Оцінка pylint - не менше 8

Вимогу до проекту:

Cтворити віртуальне оточення (python -m venv %env_name%).
Проект має бути в окремій директорії та в окремому репозиторії.
В проекті має бути файл .gitignore, всі файли які не мають версіюватись мають бути прописані там.
Master/Main branch має містити два порожніх файла: requirements.txt та scores.txt.
Розробка має вестись в гілці develop, яка утворена на базі master/main.
Завдання приймається виключно у виді pull-request з гілкі develop в master/main.
При невиконанні умов в пунктах 2-6 робота не буде розглядатись.
Базовая концепция:

При запуску файлу game.py запропонувати користувачу ввести своє ім'я.
Запропонувати користувачу ввести start для початку гри.
Хід починається з атаки гравця:
гравець обирає чаклуна(1), воїна(2) чи розбійника(3).
Вибір противника обирається автоматично.
Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.
Після атаки вивести результат атаки - влучив, промахнувся, нічия. Нічия у випадку, якщо обрані однакові класи.
Далі атакує противник, користувач обирає захист - механізм той самий.
Після успішної атаки у противника зменшуеться кількість життів. Гравець отримує 1 очко.
Після невдалого захисту гравець втрачає одне життя.
Коли у гравця закінчуються життя - ігра завершується.
Коли у противника закінчуються життя - гравець отримує додатково +5 очків і генерується новий противник.
При завершенні гри вивести результат на екран.
Структура проекта:

В проекті мають бути файли requirements.txt та scores.txt для збереження додаткових бібіліотек і збереження рекордів гравців.
Файл settings.py має містити в собі всі константи (напр. кількість життів гравця)
Файл game_exceptions.py буде містити спеціальні винятки, які будуть контролювати ігровий процес.
В файлі models.py зберігати класи гравця та противника.
Файл game.py - основний файл, який запускається для гри.
exceptions.py:

Містить клас GameOver - унаслідований від Exception. В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.

Містить клас EnemyDown - унаслідований від Exception. Функціонал не потрібен, тільки декларація.

Додаткове завдання: Створити механізм збереження тільки топ 10 рекордів.

models.py - class Enemy:

Атрибути класу - level, lives.

Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.

Містить два методи:

статичний select_attack(): повертає випадкове число від 1 до 3.
decrease_lives(self): зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown.
models.py - class Player:

Атрибути: name, lives, score, allowed_attacks.

Конструктор приймає ім'я гравця.

Кількість життів отримується з settings.
Рахунок дорівнює нулю.
Методи:

статичний fight(attack, defense) - повертає результат атаки/захисту:

0 нічия
-1 aтака/захист невдалі.
1 атака/захист вдалі.
decrease_lives(self) - те саме, що і Enemy.decrease_lives(), викликає виняток GameOver.

attack(self, enemy_obj)

отримує input (1, 2, 3) від користувача;
обирає атаку противника з об'екту enemy_obj;
викликає метод fight();
Якщо результат 0 - вивести "It's a draw!"
Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
Якщо -1 = "You missed!"
defence(self, enemy_obj) - такий самий, як метод attack(), тільки в метод fight першим передається атака противника, та при вдалій атаці противника викликається метод decrease_lives гравця.

game.py:

Містить блок на перевірку імені модуля (main)
В середині if блок try/except.
try запускає функцію play()
except обробляє два винятки:
GameOver - виводить на екран повідомлення про завершення гри, записує результат в таблицю рекордів.
KeyboardInterrupt - pass.
finally виводить на екран "Good bye!"
game.py - play():

Гравець вводить ім'я
Створюється об'єкт player
level = 1
Створюється об'єкт enemy.
В бескінечному циклі викликаються методи attack та defence об'єкту player
при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем
Додаткові завдання (обов'язкові):

Додати валідацію вводу корситувача.
Розширити ігрове меню:
Додати команду show scores - яка виводить записи із файлу scores.txt
Додати команду exit - викликає виняток та завершує роботу програми.
Додати команду help - виводить список можливих команд (зберігати в файлі налаштувань).
Додаткове завдання (необов'язкове)

Перед початком гри запропонувати режими гри: Normal або Hard

При виборі Hard кілкість життів противника множиться на N та кількість очків множиться на N

N зберігається в налаштуваннях
Додати в запис рекордів режим гри (Hard/Normal)

наприклад, якщо hard_mode_multiplier = 3, то на першому рівні противник має 3 життя, за успішну атаку гравець отримує 3 очка, за перемогу над противником отримує 15 балів