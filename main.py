
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
screen_helper = """
ScreenManager:
    MenuScreen:
    SeleccionScreen:
    PreparacionScreen:
    IngredientesScreen:
    IngredienteAdScreen:
    salsa:
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
        on_press: root.prueba()
    
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
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'  
        on_press: root.Tipofrito('Empanada')  
        Image:
            source:'Imagen/selec_Empanada.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'
        on_press: root.Tipofrito('Arepa') 
        Image:
            source:'Imagen/selec_arepa.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
           
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Preparacion'
        on_press: root.Tipofrito('papa')
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
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Ingrediente'
        on_press: root.TipoPrepa('Horneado')
        Image:
            source:'Imagen/horneado.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Ingrediente'
        on_press: root.TipoPrepa('Frito')
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
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.7}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.tiporelle('Queso')
        on_press: root.manager.current = 'IngredienteAD'

        Image:
            source:'Imagen/queso.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.tiporelle('Carne')
        on_press: root.manager.current = 'IngredienteAD'
        Image:
            source:'Imagen/carne.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y 
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.tiporelle('Pollo')
        on_press: root.manager.current = 'IngredienteAD'
        Image:
            source:'Imagen/pollo.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.7}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.tiporelle('Cerdo')
        on_press: root.manager.current = 'IngredienteAD'

        Image:
            source:'Imagen/cerdo.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y 
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.tiporelle('Huevo')
        on_press: root.manager.current = 'IngredienteAD'
        Image:
            source:'Imagen/huevo.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y  
<IngredienteAdScreen>
    name: 'IngredienteAD'
    Image:
        source:'Imagen/Titulo4.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Ingrediente'
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        on_press: root.TiporelleAd('piña')  
        Image:
            source:'Imagen/piña.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        on_press: root.TiporelleAd('nada')       
        Image:
            source:'Imagen/nada.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        on_press: root.TiporelleAd('Verdura')

        Image:
            source:'Imagen/Verdura.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        on_press: root.TiporelleAd('Maiz')
        Image:
            source:'Imagen/maiz.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
<salsa>
    name: 'salsa'
    Image:
        source:'Imagen/Titulo5.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'IngredienteAD'
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        
        Image:
            source:'Imagen/salsa1.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
      
        Image:
            source:'Imagen/salsa4.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
      
        Image:
            source:'Imagen/salsa2.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
       
        Image:
            source:'Imagen/salsa3.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        Image:
            source:'Imagen/nada.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
"""

class Frito():
   
    def tipo(self,select):
       
       if select=='papa':
           Tipo='Papa'
           
       elif select =='Empanada':
            Tipo='Empanada'
            
       elif select=='Arepa':
            Tipo='Arepa'
            
       self.Tipo = Tipo
    def preparacion(self,select):
      
        if select=='Horneado':
            prepar='Horneado'
            
        elif select=='Frito':
            prepar='Frito'
            
        self.prepar = prepar

    def relleno(self,select):
        if select == 'Carne':
            relle='Carne'
        elif select == 'Queso':
            relle='Queso'
        elif select == 'Cerdo':
            relle='Cerdo'
        elif select == 'Huevo':
            relle='Huevo'
        elif select == 'Pollo':
            relle='Pollo'
        self.relle = relle
    def relleno_ad(self,select):
        if select == 'Verdura':
            rellead='Verdura'
        elif select == 'Maiz':
            rellead='Maiz'
        elif select == 'piña':
            rellead='piña'
        elif select == 'nada':
            rellead='Ninguno'
        
        self.rellead = rellead
                  
    def mostrar(self):
     print('tipo de Frito: {}'.format(self.Tipo)) 
     print('tipo de preparacion: {}'.format(self.prepar))
     print('Relleno de la {} : {}'.format(self.Tipo,self.relle))
     print('Relleno adicional de la {} : {}'.format(self.Tipo,self.rellead))

class recibo() :
    pass

frito=Frito()

class MenuScreen(Screen):
    def prueba(self,*args):
        self.prueba1()
    def prueba1(self):
        print('Prueba')

class SeleccionScreen(Screen,Frito):
     def Tipofrito(self,n):
        frito.tipo(n)

class PreparacionScreen(Screen,Frito):
    def TipoPrepa(self,n):
        frito.preparacion(n)
        
    
class IngredientesScreen(Screen):
    def tiporelle(self,n):
        frito.relleno(n)
       
class IngredienteAdScreen(Screen):
    def TiporelleAd(self,n):
        frito.relleno_ad(n)
        frito.mostrar()

class salsa(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SeleccionScreen(name='Seleccion'))
sm.add_widget(PreparacionScreen(name='Preparacion'))
sm.add_widget(IngredientesScreen(name='Igrediente'))
sm.add_widget(IngredienteAdScreen(name='IngredienteAD'))
sm.add_widget(salsa(name='salsa'))

class DemoApp(MDApp):
    
    def build(self):
        screen = Builder.load_string(screen_helper)
        
        return screen
if __name__ == '__main__':       
  DemoApp().run()