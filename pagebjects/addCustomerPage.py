import time

from selenium.webdriver.support.select import Select


class AddCustomerTest :
    link_customer_main_manu_xpath = "//span[text()='Customers']"
    link_customer_mainItem_xpath = "(//span[text()='Customers'])[2]"
    link_add_new_xpath = "//a[@class='btn bg-blue']"
    input_email_xpath = "//input[@name='Email']"
    input_password_xpath = "//input[@name='Password']"
    input_first_name_xpath = "//input[@name='FirstName']"
    input_last_name_xpath = "//input[@name='LastName']"
    input_male_gender_xpath = "//input[@id='Gender_Male']"
    input_female_gender_xpath = "//input[@id='Gender_Female']"
    input_date_of_birth_xpath = "//input[@name='DateOfBirth']"
    input_company_name_xpath = "//input[@name='Company']"
    input_IsTaxExempt_xpath = "//input[@name='IsTaxExempt']"
    new_letter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    new_letter_your_store_name_xpath = "//li[contains(text(),'Your')]"
    new_letter_test_store_xpath = "//li[contains(text(),'Test')]"
    customer_roles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    customer_roles_administators_xpath = "//li[contains(text(),'Administrators')]"
    customer_roles_moderators_xpath = "//li[contains(text(),'Moderators')]"
    customer_roles_Guests_xpath = "//li[contains(text(),'Guests')]"
    customer_roles_Registered_xpath = "//li[contains(text(),'Registered')]"
    customer_roles_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    input_active_xpath = "//input[@name='Active']"
    input_AdminComment_xpath = "//textarea[@name='AdminComment']"
    button_save_xpath = "//button[@name='save']"
    select_manager_of_vendor_xpath =  "//select[@id='VendorId']"
    div_customer_successfully_added_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def check_customer_added_successfully ( self ) :
        act_text = self.driver.find_element_by_xpath ( self.div_customer_successfully_added_xpath ).text
        expected_text= "The new customer has been added successfully."
        if expected_text in act_text:
            assert True
        else:
            assert False

    def click_on_save_button ( self ) :
        self.driver.find_element_by_xpath ( self.button_save_xpath ).click ()

    def click_on_comment ( self, comment ) :
        self.driver.find_element_by_xpath ( self.input_AdminComment_xpath ).send_keys ( comment )

    def click_on_active_button ( self ) :
        self.driver.find_element_by_xpath ( self.input_active_xpath ).click ()

    def select_manager_of_vendor ( self, vendor="Vendor 1" ) :
        sel = Select ( self.driver.find_element_by_xpath ( self.select_manager_of_vendor_xpath ) )
        if vendor == "Vendor 1" :
            sel.select_by_visible_text ( vendor )
        elif vendor == "Vendor 2" :
            sel.select_by_visible_text ( vendor )

    def set_customer_role ( self, role="Guest" ) :
        self.driver.find_element_by_xpath(self.customer_roles_xpath).click()
        time.sleep(3)
        if role == "Registered" :
            self.role_listItem = self.driver.find_element_by_xpath ( self.customer_roles_Registered_xpath )
        elif role == "Administrator" :
            self.role_listItem =self.driver.find_element_by_xpath ( self.customer_roles_administators_xpath )
        elif role == "Guest" :
            time.sleep(3)
            self.role_listItem = self.driver.find_element_by_xpath ( "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]" ).click()
            self.role_listItem =self.driver.find_element_by_xpath ( self.customer_roles_Guests_xpath )
        elif role == "Moderator" :
            self.role_listItem =self.driver.find_element_by_xpath ( self.customer_roles_moderators_xpath )
        elif role == "Vendors" :
            self.role_listItem =self.driver.find_element_by_xpath ( self.customer_roles_Vendors_xpath )
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.role_listItem)


    def set_new_letter(self, new_letter="Your store name"):
        self.driver.find_element_by_xpath(self.new_letter_xpath).click()
        time.sleep(3)
        if new_letter == "Your store name":
            time.sleep ( 3 )
            self.driver.find_element_by_xpath ( self.new_letter_your_store_name_xpath ).click ()
        elif new_letter == "Test store 2" :
            time.sleep ( 3 )
            self.driver.find_element_by_xpath ( self.new_letter_test_store_xpath ).click ()

    def click_on_is_tax_exempt ( self ) :
        self.driver.find_element_by_xpath ( self.input_IsTaxExempt_xpath ).click ()

    def set_company_name ( self, company_name ) :
        self.driver.find_element_by_xpath ( self.input_company_name_xpath ).send_keys ( company_name )

    def set_date_of_birth ( self, date_of_birth ) :
        self.driver.find_element_by_xpath ( self.input_date_of_birth_xpath ).send_keys ( date_of_birth )

    def click_on_gender ( self, gender="male" ) :
        if gender == "male" :
            self.driver.find_element_by_xpath ( self.input_male_gender_xpath ).click ()
        elif gender == "female" :
            self.driver.find_element_by_xpath ( self.input_female_gender_xpath ).click ()

    def set_last_name ( self, lastName ) :
        self.driver.find_element_by_xpath ( self.input_last_name_xpath ).send_keys ( lastName )

    def set_first_name ( self, firstName ) :
        self.driver.find_element_by_xpath ( self.input_first_name_xpath ).send_keys ( firstName )

    def set_password ( self, password ) :
        self.driver.find_element_by_xpath ( self.input_password_xpath ).send_keys ( password )

    def set_email ( self, email ) :
        self.driver.find_element_by_xpath ( self.input_email_xpath ).send_keys ( email )

    def click_on_add_new_button ( self ) :
        self.driver.find_element_by_xpath ( self.link_add_new_xpath ).click ()

    def click_on_customer_mainItem ( self ) :
        self.driver.find_element_by_xpath ( self.link_customer_mainItem_xpath ).click ()

    def click_on_customer_main_manu ( self ) :
        self.driver.find_element_by_xpath ( self.link_customer_main_manu_xpath ).click ()

    def __init__ ( self, driver ) :
        self.driver = driver
