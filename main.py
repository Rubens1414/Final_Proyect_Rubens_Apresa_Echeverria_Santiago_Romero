from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
screen_helper = """
ScreenManager:
    MenuScreen:
    SeleccionScreen:
    PreparacionScreen:
    IngredientesScreen:
<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        Image:
            pos_hint:{'center_x':0.5,'center_y':0.8}
            source: 'Imagen/imagen.png'
            size_hint:(0.3,0.3)
    Image:
        pos_hint:{'center_x':0.2,'center_y':0.1}
        source: 'Imagen/Arepa.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.4,'center_y':0.3}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.8,'center_y':0.6}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.7,'center_y':0.4}
        source: 'Imagen/Arepa.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.9,'center_y':0.1}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.5,'center_y':0.1}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.2,'center_y':0.5}
        source: 'Imagen/Papa.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.1,'center_y':0.8}
        source: 'Imagen/Papa.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.25,'center_y':0.7}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.1,'center_y':0.3}
        source: 'Imagen/Empanada.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.9,'center_y':0.9}
        source: 'Imagen/Arepa.png'
        size_hint:(0.1,0.1)
    Image:
        pos_hint:{'center_x':0.75,'center_y':0.2}
        source: 'Imagen/Papa.png'
        size_hint:(0.1,0.1)
    MDFillRoundFlatIconButton:
        text: '¡Haz tu Pedido!'
        icon: "truck-delivery"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press: root.manager.current = 'Seleccion'
    
<SeleccionScreen>:
    name: 'Seleccion'
    Image:
        source:'Imagen/Titulo.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
   
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'menu'
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint:(0.15,0.15)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'    
        Image:
            source:'Imagen/selec_Empanada.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:(0.15,0.15)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'
        Image:
            source:'Imagen/selec_arepa.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y     
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint:(0.15,0.15)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'
        Image:
            source:'Imagen/selec_papa.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y         
<PreparacionScreen>:
    name: 'Preparacion'
    Image:
        source:'Imagen/Titulo2.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Seleccion'
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint:(0.15,0.15)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Ingrediente'
        Image:
            source:'Imagen/horneado.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint:(0.15,0.15)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Ingrediente'
        Image:
            source:'Imagen/Frito.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
<IngredientesScreen>
    name: 'Ingrediente'
    Image:
        source:'Imagen/Titulo3.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
        
"""


class MenuScreen(Screen):
    pass


class SeleccionScreen(Screen):
    pass


class PreparacionScreen(Screen):
    pass

class IngredientesScreen(Screen):
    pass



# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SeleccionScreen(name='Seleccion'))
sm.add_widget(PreparacionScreen(name='Preparacion'))
sm.add_widget(PreparacionScreen(name='Preparacion'))
sm.add_widget(IngredientesScreen(name='Igrediente'))

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
if __name__ == '__main__':       
  DemoApp().run()