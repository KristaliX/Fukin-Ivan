import check_password

class Test_password_word():
        def test_true_password_1_vfdgb439(self):
            assert check_password.password("vfdgb439") == True
        
        def test_length_password_dlfvh(self):
            assert check_password.password("dlfvh") == False

        def test_not_only_numders_in_password_29346786(self):
            assert check_password.password("29346786") == False

        def test_not_numders_in_password_dlfvnkldf(self):
            assert check_password.password("dlfvnkldf") == False

        def test_password_in_password_1_password1123(self):
            assert check_password.password("password1123") == False
        
        def test_password_in_password_2_PaSswOrd1234(self):
            assert check_password.password("PaSswOrd1234") == False

        def test_password_in_password_3_PASSWORD1234(self):
            assert check_password.password("PASSWORD1234") == False
        
        def test_true_password_2_PaSs1wOrd(self):
            assert check_password.password("PaSs1wOrd") == True
        
        def test_true_password_3_dkfvn2348lfm(self):
            assert check_password.password("dkfvn2348lfm") == True