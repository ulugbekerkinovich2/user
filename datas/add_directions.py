from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from kontrakt_excell import data_excell

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.headless = True
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

data = []


def dtm():
    driver.maximize_window()
    driver.execute_script("window.open();")
    driver.execute_script("window.open();")
    driver.execute_script("window.open();")
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[3])
    driver.get('https://translate.google.com/')
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://admin.mentalaba.uz/#/login')
    time.sleep(2.5)
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('syovkochev@gmail.com')
    password = driver.find_element(By.NAME, 'password')
    password.send_keys('12345678')
    button = driver.find_element(By.NAME, 'Button')
    button.click()
    time.sleep(2.5)
    arr = ['tumani', 'shahri', 'viloyati', 'respublikasi']
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://abt.uz/university')  # TODO abt.uz ------> 4
    all_univers = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    for universitet in all_univers:
        try:
            uni = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').text
            time.sleep(1.5)
            print(uni)
            uni_link = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').get_attribute('href')
            country = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'div').text
            print(uni)
            print(country)
            print(uni_link)
            time.sleep(0.4)
            driver.switch_to.window(driver.window_handles[1])  # TODO abt.uz university link -------> 3
            driver.get(uni_link)
            time.sleep(0.2)
            for k in range(1, 5):
                try:
                    talim_shakli = driver.find_element(
                        By.XPATH,
                        f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]')
                    talim_shakli_text = driver.find_element(
                        By.XPATH,
                        f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]'
                    ).get_attribute('textContent')
                    talim_shakli.click()
                    print(f"\n----{talim_shakli_text}----")
                    for i in range(1, 8):
                        try:
                            talim_tili = driver.find_element(
                                By.XPATH,
                                f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]'
                            )
                            talim_tili_text = driver.find_element(
                                By.XPATH,
                                f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]'
                            ).text
                            talim_tili.click()
                            print(f"\n----{talim_tili_text}----")
                            t_yonalish = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

                            for yonalish in t_yonalish:
                                try:
                                    time.sleep(3)
                                    shtrix_code = str(
                                        yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                  'div').get_attribute(
                                            'textContent'))
                                    time.sleep(1)
                                    nomi = str(
                                        yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                  'a').text)
                                    nomi = str(nomi.replace(shtrix_code, '').strip())
                                    if any(h in nomi for h in arr):
                                        continue
                                    qabul = yonalish.find_elements(By.TAG_NAME, 'td')[1].get_attribute('textContent')
                                    grant = yonalish.find_elements(By.TAG_NAME, 'td')[2].get_attribute('textContent')
                                    kontarkt = yonalish.find_elements(By.TAG_NAME, 'td')[3].get_attribute('textContent')
                                    time.sleep(1.2)
                                    print(
                                        f'{nomi}\n{shtrix_code}----------------------> {qabul}   {grant} {kontarkt}\n')
                                    time.sleep(2)
                                    driver.switch_to.window(driver.window_handles[2])
                                    search = driver.find_element(By.XPATH,
                                                                 '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/div/input')
                                    time.sleep(2)
                                    search.send_keys(f'{uni}')
                                    time.sleep(5)
                                    click = driver.find_element(By.XPATH,
                                                                '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div[3]/div[1]/table/tbody/tr/td[2]/div')
                                    time.sleep(1.5)
                                    click.click()
                                    time.sleep(1)
                                    direction = driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[1]/div/div[1]/span[3]')
                                    time.sleep(4)
                                    direction.click()
                                    time.sleep(2)
                                    search = driver.find_element(By.XPATH,
                                                                 '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[1]/div[3]/div[1]/div/input')
                                    time.sleep(2)
                                    search.send_keys(f'{nomi}')
                                    time.sleep(3)

                                    # time.sleep(1000000)
                                    # try:
                                    #     for k1 in range(100):
                                    #         direction_name = driver.find_element(By.XPATH,
                                    #                                              f'/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[{k1}]/td[2]').get_attribute(
                                    #             'textContent')
                                    #         if direction_name == nomi:
                                    #             direction_name_edit = driver.find_element(By.XPATH,
                                    #                                                       f'/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[{k1}]/td[7]')
                                    #             time.sleep(1.5)
                                    #             direction_name_edit.click()
                                    #             time.sleep(1)
                                    #             edit = driver.find_element(By.XPATH,
                                    #                                        f'/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[{k1}]/td[7]/div/div/div/div[1]/a')
                                    #             time.sleep(0.8)
                                    #             edit.click()
                                    #             time.sleep(0.4)
                                    #             break
                                    # except:
                                    #     print('tugadi')
                                    time.sleep(0.5)
                                    # add_direction = driver.find_element(By.XPATH,
                                    #                                     '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[1]/div[1]/div[2]/button')
                                    # time.sleep(2.5)
                                    # add_direction = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
                                    #                                                                            By.XPATH,
                                    #                                                                            '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[1]/div[1]/div[2]/button')))
                                    #
                                    # add_direction.click()
                                    # time.sleep(7)
                                    # print(int(shtrix_code), type(int(shtrix_code)))
                                    # direction_id = driver.find_element(By.NAME, 'direction_id')
                                    # direction_id = driver.find_element(By.NAME, 'direction_id')
                                    # time.sleep(2.5)
                                    # direction_id.click()
                                    # time.sleep(1.5)
                                    # direction_id.send_keys(int(shtrix_code))
                                    dir_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[2]').text
                                    if dir_name == nomi:
                                        direction_edit1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[7]/div/div/button')
                                        time.sleep(2)
                                        direction_edit1.click()
                                        direction_edit2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[7]/div/div/div/div[1]')
                                        time.sleep(2)
                                        direction_edit2.click()
                                    time.sleep(1)
                                    direction_uz = driver.find_element(By.NAME, 'direction_uz')
                                    time.sleep(3)
                                    direction_uz.send_keys(f'{nomi}')
                                    time.sleep(3)
                                    driver.switch_to.window(driver.window_handles[3])  # TODO perevochik -------> 1
                                    time.sleep(1)
                                    trans_uz = driver.find_element(By.XPATH,
                                                                   '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
                                    time.sleep(0.5)
                                    trans_uz.clear()
                                    time.sleep(2)
                                    trans_uz.send_keys(f'{nomi}')
                                    time.sleep(2)
                                    trans_ru = driver.find_element(By.XPATH,
                                                                   '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span').text
                                    print(trans_ru)
                                    time.sleep(4.5)
                                    driver.switch_to.window(2)  # TODO netlify -------> 2
                                    time.sleep(3.5)
                                    send_direction_ru = driver.find_element(By.NAME, 'direction_ru')
                                    time.sleep(2.5)
                                    send_direction_ru.send_keys(f'{trans_ru}')
                                    # degree = driver.find_element(By.XPATH,
                                    #                              '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[5]/div/ul/li[1]/label')
                                    # time.sleep(1.5)
                                    # degree.click()
                                    # time.sleep(2)
                                    # select_year = driver.find_element(By.XPATH,
                                    #                                   '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[4]/div/div/input')
                                    # time.sleep(4)
                                    # select_year.click()
                                    # time.sleep(4)
                                    # el = driver.find_element(By.XPATH,
                                    #                          '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[4]/div/ul/li[1]')
                                    # time.sleep(2.5)
                                    # el.click()
                                    # time.sleep(1)
                                    if talim_shakli_text == 'Kunduzgi':
                                        full_time = driver.find_element(By.XPATH,
                                                                        '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[1]/ul/li[1]/label')
                                        full_time.click()
                                    # try:
                                    #     # full_time = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[1]/h1').text
                                    # except:
                                    #     print('full time yoq')
                                    # if full_time:


                                    if talim_shakli_text == 'Kechki':
                                        evening = driver.find_element(By.XPATH,
                                                                      '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[1]/ul/li[3]/label')
                                        evening.click()
                                    if talim_shakli_text == 'Sirtqi':
                                        part_time = driver.find_element(By.XPATH,
                                                                        '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[1]/ul/li[2]/label')
                                        part_time.click()
                                    if talim_tili != 'O‘zbek':
                                        add_lang = driver.find_element(By.XPATH,
                                                                       '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[1]/div/button')
                                        add_lang.click()
                                        try:
                                            for f in range(1, 13):
                                                lang = driver.find_element(By.XPATH,
                                                                           f'/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[1]/div/div/div[{f}]').text
                                                lang_button = driver.find_element(By.XPATH,
                                                                                  f'/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[1]/div/div/div[{f}]')
                                                if lang == talim_tili:
                                                    lang_button.click()
                                        except Exception as e:
                                            print('til tanlanmadi', e)

                                    qabul_grant = qabul.split('/')[0].strip()
                                    qabul_kontrakt = qabul.split('/')[1].strip()
                                    uzbek_g = driver.find_element(By.XPATH,
                                                                  '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/input')
                                    uzbek_k = driver.find_element(By.XPATH,
                                                                  '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[2]/div[2]/div/div[1]/div/input')
                                    uzbek_g.send_keys(f'{qabul_grant}')
                                    uzbek_k.send_keys(f'{qabul_kontrakt}')
                                    grant_b = driver.find_element(By.XPATH,
                                                                  '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/input')
                                    kontrakt_b = driver.find_element(By.XPATH,
                                                                     '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[2]/div[2]/div/div[2]/div/input')
                                    grant_b.send_keys(f'{grant}')
                                    kontrakt_b.send_keys(f'{kontarkt}')
                                    contract_price = data_excell(f'{nomi}')
                                    print(contract_price)
                                    tution_fee = driver.find_element(By.XPATH,
                                                                     '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[4]/div[1]/div/input')
                                    tution_fee.send_keys(contract_price)
                                    contract = driver.find_element(By.XPATH,
                                                                   '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[7]/div/ul/li[2]/label')
                                    contract.click()
                                    test = driver.find_element(By.XPATH,
                                                               '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[8]/div/ul/li[1]/label')
                                    test.click()
                                    from_ = driver.find_element(By.XPATH,
                                                                '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[9]/div/div/div[1]/div/label')
                                    from_.click()
                                    start_date = driver.find_element(By.NAME, 'start_date')
                                    start_date.send_keys('16.06.2023')
                                    end_date = driver.find_element(By.XPATH,
                                                                   '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[9]/div/div/div[2]/div/label')
                                    end_date.click()
                                    ends_date = driver.find_element(By.NAME, 'end_date')
                                    ends_date.send_keys('17.07.2023')
                                    time.sleep(1)

                                    save = driver.find_element(By.XPATH,
                                                               '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[10]/div/button[2]')
                                    time.sleep(2)
                                    save.click()
                                    time.sleep(3)
                                    driver.get("https://delicate-salmiakki-0dd525.netlify.app/#/institutions")
                                    time.sleep(1.5)
                                    driver.switch_to.window(driver.window_handles[1])  # TODO abt.uz -------> 1

                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[3]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[3]/div[2]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[4]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div/div/div/div/div[4]/div[2]/div/div[1]/div/input')
                                    #
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[2]/div/div/div/div[3]/div[2]/div/div[1]/div/input')
                                    #
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[3]/div/div/div/div[3]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[3]/div/div/div/div[3]/div[2]/div/div[1]/div/input')
                                    #
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[4]/div/div/div/div[3]/div[1]/div/div[1]/div/input')
                                    # '/html/body/div[1]/div/div/div[3]/div[3]/div/div/div/div[2]/div/form/div/div/div/div[6]/div[3]/div[4]/div/div/div/div[3]/div[2]/div/div[1]/div/input')
                                except:
                                    print('yo\'nalish topilmadi')
                        except:
                            print('ta\'lim tili mavjud emas')
                except:
                    print('ta\'lim shakli mavjud emas')
        except:
            print('universitet mavjdu ems')


dtm()
