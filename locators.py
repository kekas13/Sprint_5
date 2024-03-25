class TestLocators:
    input_name_locator = '//fieldset[1]//input[@class="text input__textfield text_type_main-default"]'  # Ввод имени
    input_email_locator = '//fieldset[2]//input[@class="text input__textfield text_type_main-default"]'  # Ввод почты
    input_password_locator = '//input[@type="password"]'  # Ввод пароля
    input_email_login_locator = '//input[@type="text"]'  # Ввод почты на странице логина
    button_reg_locator = '//button[contains(text(), "Зарегистрироваться")]'  # Кнопка "Зарегистрироваться"
    button_login_locator = '//button[contains(text(), "Войти")]'  # Кнопка "Войти"
    header_locator = '//h1[contains(text(), "Соберите бургер")]'  # Заголовок главной страницы
    error_text_locator = '.input__error'  # Ошибка при вводе некорректного пароля
    button_login_main_page_locator = '//button[contains(text(), "Войти в аккаунт")]'  # "Войти в аккаунт"
    button_login_alternate_locator = '//a[@href="/login"]'  # Войти в личный кабинет (регистрация/восстановление)
    button_go_to_profile_locator = '//p[contains(text(), "Личный Кабинет")]'  # Личный кабинет
    button_save_profile_locator = '//button[contains(text(), "Сохранить")]'  # Кнопка "Сохранить" в ЛК
    button_constructor_locator = '//p[contains(text(), "Конструктор")]'  # "Конструктор" в хедере
    button_logo_locator = '//div[contains(@class, "logo")]'  # Лого в хедере
    button_logout_locator = '//button[contains(text(),"Выход")]'  # Кнопка выхода их аккаунта в ЛК
    tab_sauce_locator = '//span[contains(text(),"Соусы")]'  # Вкладка "Соусы"
    scroll_sauce_locator = '//div[contains(@class, "tab_tab_type_current__2BEPc")]/span[contains(text(),"Соусы")]'  # Скролл до списка соусов
    header_sauce_locator = '//h2[contains(text(), "Соусы")]'  # Заголовок "Соусы" в конструкторе
    tab_fillings_locator = '//span[contains(text(),"Начинки")]'  # Вкладка "Начинки"
    scroll_fillings_locator = '//div[contains(@class, "tab_tab_type_current__2BEPc")]/span[contains(text(),"Начинки")]'  # Скролл до списка начинок
    header_fillings_locator = '//h2[contains(text(), "Начинки")]'  # Заголовок "Начинки" в конструкторе
    tab_buns_locator = '//span[contains(text(),"Булки")]'  # Вкладка "Булки"
    scroll_buns_locator = '//div[contains(@class, "tab_tab_type_current__2BEPc")]/span[contains(text(),"Булки")]'  # Скролл до списка булок
    header_buns_locator = '//h2[contains(text(), "Булки")]'  # Заголовок "Булки" в конструкторе

