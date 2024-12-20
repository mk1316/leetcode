class Solution:
    def romanToInt(self, s: str) -> int:
        reverse_string = s[::-1]
        self.__count = 0
        self.__current_num = 0
        self.__prev_num = 0
        self.__total_num = 0
        for i in reverse_string:
            if i == "I":
                self.__current_num = 1
            elif i =="V":
                self.__current_num = 5
            elif i =="X":
                self.__current_num = 10
            elif i =="L":
                self.__current_num = 50
            elif i =="C":
                self.__current_num = 100
            elif i =="D":
                self.__current_num = 500
            else:
                self.__current_num = 1000
            
            if self.__current_num >= self.__prev_num:
                self.__default_value()
            else:
                self.__calc_value()
        return self.__total_num

    def __default_value(self):
        self.__total_num += self.__current_num
        self.__prev_num = self.__current_num

    def __calc_value(self):
        self.__new_current_num = self.__prev_num - self.__current_num
        self.__total_num -= self.__prev_num
        self.__total_num += self.__new_current_num
        self.__prev_num = self.__current_num
            
