from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')


@when('Select "Ember Temperature Control Smart Mug"')
def select_ember_mug(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/61VXH79P8sL._AC_UL320_.jpg']").click()


@then('Verify that text {expected_result} is shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


# I am not sure if that's correct way to do it, also  am lost and don't know how to write assertion error message
@then('Verify every product has an image')
def verify_every_image_on_search_page(context):
    products = context.driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot.s-result-list div.s-card-container")
    print(len(products))

    for images in products:
        images = context.driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot.s-result-list img.s-image")
        print(len(images))

    assert len(images) >= len(products) # step didn't fail


@then('Verify every product has a name')
def verif_every_product_has_name(context):
    products = context.driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot.s-result-list div.s-card-container")

    for names in products:
        names = context.driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot.s-result-list div.a-section.a-spacing-small h2.a-size-mini.a-spacing-none")

    assert len(names) <= len(products)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(), f'Product image missing'
        print(product.find_element(*PRODUCT_TITLE).text)

        assert product.find_element(*PRODUCT_TITLE).text, 'Product title is missing'

