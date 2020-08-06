import pytest

class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeWebDriverManager().install())
        self.driver.im