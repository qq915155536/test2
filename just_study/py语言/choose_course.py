#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/11/27 11:03
# Author :A0025-江苏-小丹
# QQ:915155536
# File :choose_course.py
#  ===========================
class School:
    school_name = 'OLDBOY'

    # 学校地址,学校里的班级
    def __init__(self, school_addr):
        self.school_addr = school_addr
        self.classes = []

    # 学校关联班级
    def related_class(self, class_obj):
        self.classes.append(class_obj)

    # 查看该校区的班级信息及课程信息
    def tell_classes(self):
        print(self.school_name.center(60, '='))
        for class_obj in self.classes:
            # 输出课程
            class_obj.tell_course()


class Class:

    def __init__(self, name):
        self.name = name
        self.course = None

    # 班级关联课程
    def related_course(self, course_name):
        self.course = course_name

    # 查看课程
    def tell_course(self):
        print('%s下有 %s' % (self.name, self.course))


# 实例化学校类，创建学校
school_shanghai = School('上海校区')
school_beijing = School('北京校区')

# 创建班级，关联课程
class_python = Class('python班')
class_python.related_course('python开发课')
class_java = Class('java班')
class_java.related_course('java开发课')

# 学校关联班级,查看对应班级的课程信息
school_shanghai.related_class(class_python)
school_shanghai.related_class(class_java)
# 查看学校下的课程信息
# school_shanghai.tell_classes()


class Course:
    pass


class Student:
    pass
