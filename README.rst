fin@ncetradehelpbot
======

fin@ncetradehelpbot - это бот для Telegram созданный с целью делать вашу жизнь интереснее, присылая вам советы по инвестированию и фотографии мировых валют.

Установка
---------

Создайте виртуальное окружение и активируйте его.Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt 

    Положите картинки с изображением мировых валютв папку images. Название файлов должно начинаться с money, а заканчиваться .jpg например money333325.jpg 

Настройка
---------

Создайте файл setting.py и добавьте туда следующие настройки:

.. code-block:: python

    API_KEY = "API ключ, который вы получили у BotFather."

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
------
В активированом виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py