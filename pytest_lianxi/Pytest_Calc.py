import pytest

from pytest_lianxi.Calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expected", [(9999,200005,210004), (1.03,0.02,1.05), (-9,-4,-13),(13,-4,9), (8,"qw","字符类型错误")])
    def test_add(self,a,b,expected):

        result = self.calc.add(a, b)
        print(result)
        assert expected == result



    @pytest.mark.parametrize("a,b,expected", [(99999,11111,9), (0.75,0.5,1.5), (-6,-3,2), (-14,7,-2),(3,0,"输入数据不合法"),("er",3,"输入数据不合法")])
    def test_div(self,a,b,expected):
        try:
            result = self.calc.div(a, b)
        except :
            result = "输入数据不合法"
        else:
            assert expected == result
        finally:
            print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'Pytest_Calc.py'])