from selenium import webdriver


class SearchCustomer:
    text_email_id = "SearchEmail"
    text_first_name_id = "SearchFirstName"
    text_last_name_id = "SearchLastName"
    btn_search_xpath = "(//i[@class='fa fa-search'])[2]"

    table_search_result_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//*[@id='customers-grid']/tbody/tr"
    table_column_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def set_email( self, email ):
        self.driver.find_element_by_id(self.text_email_id).clear()
        self.driver.find_element_by_id(self.text_email_id).send_keys(email)

    def set_first_name( self,first_name ):
        self.driver.find_element_by_id(self.text_first_name_id).clear()
        self.driver.find_element_by_id(self.text_first_name_id).send_keys(first_name)

    def set_last_name( self,last_name ):
        self.driver.find_element_by_id ( self.text_last_name_id ).clear()
        self.driver.find_element_by_id ( self.text_last_name_id ).send_keys(last_name)

    def click_on_search_button( self ):
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def get_no_of_rows( self ):
        return len(self.driver.find_elements_by_xpath(self.table_row_xpath))

    def get_no_of_column( self ):
        return len(self.driver.find_elements_by_xpath(self.table_column_xpath))

    def search_customer_by_attribute( self, attribute ):
        flag = False
        for row in range(1,self.get_no_of_rows()+1):
            all_table_head = len(self.driver.find_elements_by_xpath("//table[@role='grid']/thead/tr/th"))
            for each_table_head in range(1,(all_table_head//2)+1):
                head_text = self.driver.find_element_by_xpath(f"(//table[@role='grid']/thead/tr/th)[{str(each_table_head)}]").text
                if "email" in head_text.lower():
                    self.col = each_table_head
                    break
                elif "name" in head_text.lower():
                    self.col = each_table_head
                    break

        for row in range(1,self.get_no_of_rows()+1):
            attribute_text = self.driver.find_element_by_xpath(f"//table[@id='customers-grid']/tbody/tr[{str(row)}]/td[{str(self.col)}]").text
            if attribute_text.lower() == attribute.lower():
                flag=True
                break
        return flag




