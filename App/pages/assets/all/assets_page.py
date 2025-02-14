from App.pages.base_page import BasePage


class AssetsPage(BasePage):
    def goto_top_assets_page(self):
        return AssetsPage(driver=self.driver)

    def hide_whether_assets(self):
        # 是否隐藏展示资产
        pass

    def goto_top_assets_bill_page(self):
        # 跳转帐单
        from App.pages.assets.assets_bill.assets_bill_page import AssetsBillPage
        return AssetsBillPage(driver=self.driver)

    def goto_top_spot_assets_page(self):
        # 顶部跳转现货-余额
        from App.pages.assets.spot.spot_assets_page import SpotAssetsPage
        return SpotAssetsPage(driver=self.driver)

    def goto_top_futures_assets_page(self):
        # 顶部跳转合约资产
        from App.pages.assets.futures.futures_asstes_page import FuturesAssetsPage
        return FuturesAssetsPage(driver=self.driver)

    def goto_top_finance_assets_page(self):
        # 顶部跳转理财
        from App.pages.assets.finance.finance_assets_page import FinanceAssetsPage
        return FinanceAssetsPage(driver=self.driver)

    def goto_top_mining_page(self):
        # 顶部跳转挖矿
        from App.pages.assets.mining.mining_assets_page import MiningAssetsPage
        return MiningAssetsPage(driver=self.driver)

    def goto_top_mortgage_loan_page(self):
        # 顶部跳转抵押借贷
        from App.pages.assets.mortgage_loan.mortgage_loan_page import MortgageLoanPage
        return MortgageLoanPage(driver=self.driver)

    def goto_top_stock_page(self):
        # 顶部跳转股票
        from App.pages.assets.stock.stock_assets_page import StockAssetsPage
        return StockAssetsPage(driver=self.driver)

    def goto_top_super_level_page(self):
        # 顶部跳转超级杠杠
        from App.pages.assets.super_level.super_level_asstes_page import SuperLevelAssetsPage
        return SuperLevelAssetsPage(driver=self.driver)

    def goto_top_mortgage_loan_page(self):
        # 顶部跳转借贷
        from App.pages.assets.mortgage_loan.mortgage_loan_page import MortgageLoanPage
        return MortgageLoanPage(driver=self.driver)

    def get_all_assets(self):
        # 获取总资产
        pass

    def goto_top_recharge_page(self):
        # 充值
        pass

    def goto_top_transfer_page(self):
        # 提币
        pass

    def goto_spot_assets_page(self):
        # 跳转现货-余额
        from App.pages.assets.spot.spot_assets_page import SpotAssetsPage
        return SpotAssetsPage(driver=self.driver)

    def get_spot_assets(self):
        # 获取余额
        return ""

    def goto_futures_assets_page(self):
        # 跳转合约资产
        from App.pages.assets.futures.futures_asstes_page import FuturesAssetsPage
        return FuturesAssetsPage(driver=self.driver)

    def get_futures_assets(self):
        # 获取合约资产
        pass

    def goto_finance_assets_page(self):
        # 跳转理财
        from App.pages.assets.finance.finance_assets_page import FinanceAssetsPage
        return FinanceAssetsPage(driver=self.driver)

    def get_finance_assets(self):
        # 获取理财余额
        pass

    def goto_mining_page(self):
        # 跳转挖矿
        from App.pages.assets.mining.mining_assets_page import MiningAssetsPage
        return MiningAssetsPage(driver=self.driver)

    def get_mining_assets(self):
        # 获取挖矿资产
        pass

    def goto_mortgage_loan_page(self):
        # 跳转抵押借贷
        from App.pages.assets.mortgage_loan.mortgage_loan_page import MortgageLoanPage
        return MortgageLoanPage(driver=self.driver)

    def get_mortgage_loan_assets(self):
        # 获取借贷资产
        pass

    def goto_stock_page(self):
        # 跳转股票
        from App.pages.assets.stock.stock_assets_page import StockAssetsPage
        return StockAssetsPage(driver=self.driver)

    def get_stock_assets(self):
        # 获取股票资产
        pass

    def goto_super_level_page(self):
        # 跳转超级杠杠
        from App.pages.assets.super_level.super_level_asstes_page import SuperLevelAssetsPage
        return SuperLevelAssetsPage(driver=self.driver)

    def get_super_level_assets(self):
        # 获取超级港资产
        pass

    def goto_mortgage_loan_page(self):
        # 跳转借贷
        from App.pages.assets.mortgage_loan.mortgage_loan_page import MortgageLoanPage
        return MortgageLoanPage(driver=self.driver)

    def get_mortgage_loan_assets(self):
        # 获取借贷资产
        pass
