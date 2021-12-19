import quad

class TestQuad:
    def test_quad_1_2_3(self):
        assert quad.quadratic_equation(1, 2, 3) == False
    
    def test_quad_2_4_1(self):
        assert quad.quadratic_equation(2, 4, 1) == True

    def test_quad_1_2_1(self):
        assert quad.quadratic_equation(1, 2, 1) == True