from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
#import Layout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivy.clock import Clock
from kivymd.uix.selectioncontrol import MDCheckbox
import csv


#s_g= [['satish','9592390201'],['ram','9592390201'],['hola','9592390201'],['cola','9592390201']
#      ,['satish','9592390201'],['ram','9592390201'],['hola','9592390201'],['cola','9592390201']]




file=open("data.csv", 'r')
file02=open("data02.csv", 'r')
data= list(csv.reader(file, delimiter=","))
data02= list(csv.reader(file02, delimiter=","))
file.close()
s_g=data
gunner=data02
print(s_g)


class Content(BoxLayout):
    nav_drawer= ObjectProperty()
    manager = ObjectProperty()



class Demo(ScreenManager):


    def __init__(self, **kwargs):
        self.checkbox = MDCheckbox()
        super().__init__(**kwargs)
        Clock.schedule_once(self.sg_list)
        Clock.schedule_once(self.g_list)


    SecurityGuard = '0'
    Gunner = '0'

    def sg_list(self, *args):
        for i in s_g:
            self.ids.container.add_widget(TwoLineListItem(text=f'{i[0]}', secondary_text =f'{i[1]}'))

    def g_list(self, *args):
        for i in gunner:
            self.ids.container1.add_widget(TwoLineListItem(text=f'{i[0]}', secondary_text =f'{i[1]}'))
    def fun(self):
        temp_name= self.ids.name.text
        temp_no= self.ids.number.text


        #s_g.append([temp_name,temp_no])
        #print([temp_name,temp_no])
        #Demo.sg_list(self)
        print(Demo.SecurityGuard)
        if Demo.SecurityGuard=='1':
            print('run')
            with open("data.csv", 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                temp_data=[[temp_name,temp_no]]
                print(temp_data)
                csvwriter.writerows(temp_data)
            self.ids.container.add_widget(TwoLineListItem(text=temp_name, secondary_text =temp_no))
        elif Demo.Gunner=='1':
            with open("data02.csv", 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                temp_data=[[temp_name,temp_no]]
                print(temp_data)
                csvwriter.writerows(temp_data)
            self.ids.container1.add_widget(TwoLineListItem(text=temp_name, secondary_text =temp_no))

    def clear_text(self):
        self.ids.name.text = ''
        self.ids.number.text = ''
        #Demo.sg_list(self)




class Layout(MDApp):
    def update_securityguard(self, active):

        if active:
            Demo.SecurityGuard = '1'
            print(Demo.SecurityGuard)
        else:
            Demo.SecurityGuard = '0'
            print(Demo.SecurityGuard)

    def update_gunner(self, active):

        if active:
            Demo.Gunner= '1'
            print(Demo.Gunner)
        else:
            Demo.Gunner = '0'
            print(Demo.Gunner)


    def build(self):
        #Builder.load_string("Layout.kv")



        return Demo()

Layout().run()

