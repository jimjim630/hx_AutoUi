from App.pages.base_page import BasePage


class HomePage(BasePage):
    # 首页
    def goto_my_page(self):
        # 我的
        from App.pages.my.my_page import MyPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView[1]").click()
        return MyPage(driver=self.driver)

    def goto_search_page(self):
        # 首页搜索
        from App.pages.home.search_page import SearchPage
        self.driver.hx_find_element(locator_type="xpath", locator_value="//*[@hint ='搜索您关心的币种/股票']").click()
        return SearchPage(driver=self.driver)

    def goto_customer_services(self):
        # 首页客服
        from App.pages.home.customer_services_page import CustomerServicesPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView[2]").click()
        return CustomerServicesPage(driver=self.driver)

    def goto_QR_code_scan(self):
        # 首页二维码扫描
        from App.pages.home.qr_code_scan_page import QRCodeScanPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView[3]").click()
        return QRCodeScanPage(driver=self.driver)

    def goto_notify_page(self):
        # 跳转首页站内信
        from App.pages.internal_mail.notify_page import NotifyPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView[4]").click()
        return NotifyPage(driver=self.driver)

    def goto_login(self):
        #  未登录首页点击登录按钮
        from App.pages.login.login_page import LoginPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.Button[@content-desc='登录 / 注册']").click()
        return LoginPage(driver=self.driver)

    def total_assets(self):
        # 登录后资产估值
        pass

    def goto_billings_page(self, is_login):
        # 首页帐单
        if is_login:
            from App.pages.assets.assets_bill.assets_bill_page import AssetsBillPage
            return AssetsBillPage(driver=self.driver)
        else:
            from App.pages.login.login_page import LoginPage
            return LoginPage(driver=self.driver)

    def goto_recharge_page(self, is_login):
        # 首页充值
        from App.pages.assets.recharge_popup_window import RechargePopUpWindow
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.Button[@content-desc='充值']").click()
        return RechargePopUpWindow(driver=self.driver)

    def goto_financial_page(self):
        # 首页理财
        from App.pages.finance.financial_management.financial_management_page import FinancialManagementPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.Button[@content-desc='理财']").click()
        return FinancialManagementPage(driver=self.driver)

    def goto_transfer_page(self):
        # 首页提币
        from App.pages.assets.transfer_popup_window import TransferPopupWindow
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.widget.Button[@content-desc='转账']").click()
        return TransferPopupWindow(driver=self.driver)

    def banner(self):
        pass

    def goto_home_page(self):
        # 底部导航-首页
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.view.View[2]/android.widget.ImageView[1]").click()
        return HomePage(driver=self.driver)

    def goto_quotes_page(self):
        # 底部导航-行情
        from App.pages.quotes.quotes_page import QuotesPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.view.View[2]/android.widget.ImageView[2]").click()
        return QuotesPage(driver=self.driver)

    def goto_trade_page(self):
        # 底部导航-交易
        from App.pages.trade.trade_page import TradePage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.view.View[2]/android.widget.ImageView[3]").click()
        return TradePage(driver=self.driver)

    def goto_finance_page(self):
        # 底部导航-金融
        from App.pages.finance.financial_management.financial_management_page import FinancialManagementPage
        self.driver.hx_find_element(locator_type="xpath",
                                    locator_value="//android.view.View[2]/android.widget.ImageView[4]").click()
        return FinancialManagementPage(driver=self.driver)

    def goto_assets_page(self, if_login):
        # 底部导航-资产
        if if_login:
            from App.pages.assets.all.assets_page import AssetsPage
            self.driver.hx_find_element(locator_type="xpath",
                                        locator_value="//android.view.View[2]/android.widget.ImageView[5]").click()
            return AssetsPage(driver=self.driver)
        else:
            from App.pages.login.login_page import LoginPage
            return LoginPage(driver=self.driver)

    def diamond_field(self):
        # 金刚区
        pass

    def popular_financial_management(self):
        # 首页理财推荐
        pass
