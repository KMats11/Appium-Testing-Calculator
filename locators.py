from appium.webdriver.common.mobileby import By


class MainPageLocators:
    NINE = (By.ID, "com.dalviksoft.calculator:id/digit_9")
    ZERO = (By.ID, "com.dalviksoft.calculator:id/digit_0")
    TWO = (By.ID, "com.dalviksoft.calculator:id/digit_2")
    THREE = (By.ID, "com.dalviksoft.calculator:id/digit_3")
    FIVE = (By.ID, "com.dalviksoft.calculator:id/digit_5")
    EQUAL = (By.ID, "com.dalviksoft.calculator:id/eq")
    RESULT = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                        '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                        '.widget.RelativeLayout/android.widget.FrameLayout['
                        '2]/android.widget.RelativeLayout/android.widget.EditText')
    DELETE = (By.ID, "com.dalviksoft.calculator:id/del")
    RES = (By.ID, "com.dalviksoft.calculator:id/formula")

    X1 = (By.ID, "com.dalviksoft.calculator:id/op_pow")
    X2 = (By.ID, "com.dalviksoft.calculator:id/digit_1")
    X3 = (By.ID, "com.dalviksoft.calculator:id/fun_log")
    X4 = (By.ID, "com.dalviksoft.calculator:id/const_e")


class OperatorsPageLocators:
    SQRT = (By.ID, "com.dalviksoft.calculator:id/op_sqrt")
    SIN = (By.ID, "com.dalviksoft.calculator:id/fun_sin")

    ANGLE = (By.ID, "com.dalviksoft.calculator:id/info")
    RADIAN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView"
                        "/android.widget.LinearLayout[1]/android.widget.LinearLayout")
    DEGREE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView"
                        "/android.widget.LinearLayout[2]/android.widget.LinearLayout")

