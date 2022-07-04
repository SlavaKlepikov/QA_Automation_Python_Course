from utils.read_run_settings import ReadConfig


def test_sign_in(get_home_page):
    user_email = ReadConfig.get_user_login()
    user_password = ReadConfig.get_user_password()
    login_page = get_home_page.click_sign_in()
    login_page.sign_in(user_email, user_password)
    title_web_page_login_expected = "lichess.org • Бесплатные шахматы онлайн"
    assert login_page.auth_login_box_label_invisibility().title == title_web_page_login_expected, \
        f"\nUser not loggined\nActual title:{login_page.title}\n" \
        f"Expected:{title_web_page_login_expected}"


def test_title_base_page(get_home_page):
    title_web_page_base_actual = get_home_page.title
    title_web_page_login_expected = "lichess.org • Free Online Chess"
    assert title_web_page_base_actual == title_web_page_login_expected, \
        f"\nWrong title\nActual title:{title_web_page_base_actual}\n" \
        f"Expected:{title_web_page_login_expected}"


def test_header_create_game(get_home_page):
    get_home_page.click_create_game()
    header_game_setup_menu_expected = "Create a game"
    header_game_setup_menu_actual = get_home_page.get_header_game_setup_menu()
    assert header_game_setup_menu_actual == header_game_setup_menu_expected, \
        f"\nWrong header\nActual header:{header_game_setup_menu_actual}\n" \
        f"Expected:{header_game_setup_menu_expected}"


def test_variants_create_game(get_home_page):
    get_home_page.click_create_game()
    header_game_setup_menu_expected = "Create a game"
    header_game_setup_menu_actual = get_home_page.get_header_game_setup_menu()
    assert header_game_setup_menu_actual == header_game_setup_menu_expected, \
        f"\nWrong header\nActual header:{header_game_setup_menu_actual}\n" \
        f"Expected:{header_game_setup_menu_expected}"


def test_play_with_friend(get_home_page):
    get_home_page.click_play_with_friend()
    header_game_setup_menu_expected = "Play with a friend"
    header_game_setup_menu_actual = get_home_page.get_header_game_setup_menu()
    assert header_game_setup_menu_actual == header_game_setup_menu_expected, \
        f"\nWrong header\nActual header:{header_game_setup_menu_actual}\n" \
        f"Expected:{header_game_setup_menu_expected}"


def test_play_with_computer(get_home_page):
    get_home_page.click_play_with_computer()
    header_game_setup_menu_expected = "Play with the computer"
    header_game_setup_menu_actual = get_home_page.get_header_game_setup_menu()
    assert header_game_setup_menu_actual == header_game_setup_menu_expected, \
        f"\nWrong header\nActual header:{header_game_setup_menu_actual}\n" \
        f"Expected:{header_game_setup_menu_expected}"


def test_time_choice_range_game_setup(get_home_page):
    get_home_page.click_create_game()
    time_choice_range_game_setup_expected = "5"
    time_choice_range_game_setup_actual = get_home_page.get_time_choice_range_game_setup()
    assert time_choice_range_game_setup_actual == time_choice_range_game_setup_expected, \
        f"\nWrong time\nActual time:{time_choice_range_game_setup_actual}\n" \
        f"Expected:{time_choice_range_game_setup_expected}"


def test_donate_title(get_home_page):
    donate_page = get_home_page.click_donate()
    donate_title_expected = "Become a Lichess Patron • lichess.org"
    donate_page_actual = donate_page.title
    assert donate_page_actual == donate_title_expected, \
        f"\nWrong title\nActual title:{donate_page_actual}\n" \
        f"Expected:{donate_title_expected}"


def test_swag_store_title(get_home_page):
    swag_store_page = get_home_page.click_swag_store_btn()
    swag_store_expected = "lichess.org swag store"
    swag_store_page_actual = swag_store_page.title
    assert swag_store_expected == swag_store_page_actual, \
        f"\nWrong title\nActual title:{swag_store_page_actual}\n" \
        f"Expected:{swag_store_expected}"


def test_swag_store_url(get_home_page):
    swag_store_url_page = get_home_page.click_swag_store_btn()
    swag_store_url_expected = "https://lichess-org.myspreadshop.com/"
    swag_store_url_actual = swag_store_url_page.get_current_url()
    assert swag_store_url_expected == swag_store_url_actual, \
        f"\nWrong url\nActual url:{swag_store_url_actual}\n" \
        f"Expected:{swag_store_url_expected}"

