"""
定义：
    工厂方法模式定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个，工厂方法让类把实例化推迟到子类
使用场景：
    1. 当一个类不知道它所必须创建的对象的类的时候
    2. 当一个类希望由它的子类来指定它所创建的对象的时候
    3. 当你发现你在多个类中使用同样的创建代码的时候，就应该考虑使用工厂方法模式
"""

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):

    def describe(self):
        print("Album Section")


class PatentSection(Section):

    def describe(self):
        print("Patent Section")



class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


