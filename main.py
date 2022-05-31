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
    recibo:
    pedido_proceso:
<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        Image:
            pos_hint:{'center_x':0.5,'center_y':0.8}
            source: 'Imagen/imagen.png'
            size_hint:(0.3,0.3)
    
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
        source:'Imagen/Titulo1.png'
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
        source:'Imagen/Titulo2.png'
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
        source:'Imagen/Titulo3.png'
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
            source:'Imagen/pina.png'
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
            source:'Imagen/verdura.png'
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
        source:'Imagen/Titulo4.png'
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
         
        on_press: root.manager.current = 'recibo'
               
        on_press: root.salsa('Salsa_Rosada')

        Image:
            source:'Imagen/salsa1.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'recibo'
        on_press: root.salsa('Salsa_Suero')
        Image:
            source:'Imagen/salsa4.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'recibo'
        on_press: root.salsa('Salsa_Picante')
        Image:
            source:'Imagen/salsa2.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.3, "center_y": 0.6}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'recibo'
        on_press: root.salsa('Salsa_Tartara')
        Image:
            source:'Imagen/salsa3.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:(0.2,0.2)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'recibo'
        on_press: root.salsa('nada')
        Image:
            source:'Imagen/nada.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    
<recibo>:
    name:'recibo'
    Image:
        source:'Imagen/Titulo5.png'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        size_hint:(0.5,0.5)
    MDLabel:
        id:Titulo_tipo
        pos_hint:{"center_x":0.5,"center_y":0.7+0.03}
        size_hint:(.5,.5)
        font_style:"Body2"
        halign:"center"
        text: ' '
        color: 255/255.0,69/255.0,0/255.0,1
    MDLabel:
        id:Titulo_Preparacion
        pos_hint:{"center_x":0.5,"center_y":0.6+0.05}
        size_hint:(.5,.5)
        font_style:"Body2"
        halign:"center"
        text: ' '
        color: 255/255.0,0/255.0,0/255.0,1
    MDLabel:
        id:Titulo_Relleno
        pos_hint:{"center_x":0.5,"center_y":0.5+0.07}
        size_hint:(.5,.5)
        font_style:"Body2"
        halign:"center"
        text: ' '
        color: 138/255.0,43/255.0,226/255.0,1

    MDLabel:
        id:Titulo_RellenoAD
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
        color: 210/255.0,105/255.0,30/255.0,1
    MDLabel:
        id:Titulo_salsa
        pos_hint:{"center_x":0.5,"center_y":0.4}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
        color: 210/255.0,43/255.0,105/255.0,1
    MDLabel:
        id:Informacion_Tipo
        pos_hint:{"center_x":0.5,"center_y":0.6+0.09}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
    MDLabel:
        id:Informacion_Prepa
        pos_hint:{"center_x":0.5,"center_y":0.6+0.02}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
    MDLabel:
        id:Informacion_Relle
        pos_hint:{"center_x":0.5,"center_y":0.5+0.04}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
    MDLabel:
        id:Informacion_RelleAd
        pos_hint:{"center_x":0.5,"center_y":0.4+0.06}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
    MDLabel:
        id:Informacion_Salsa
        pos_hint:{"center_x":0.5,"center_y":0.3+0.06}
        size_hint:(.5,.5)
        theme_text_color:"Primary"
        font_style:"Body2"
        halign:"center"
        text: ' '
        
    BoxLayout:
        Image:
            source:'Imagen/Forma_recibo.png'
            pos_hint: {'center_x':0.5,'center_y':0.5}
            size_hint:(0.5,0.5)
    BoxLayout:
        Image:
            id:info
            source:'Imagen/icon_info.png'
            pos_hint: {'center_x':0.5,'center_y':0.5}
            size_hint:(0.5/8,0.5/8)
    
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.2, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'salsa'
        on_press: root.Ocultar()
        Image:
            source:'Imagen/volver.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1/2,0.1/2)
        line_color: 0, 0, 0, 0
        on_press: root.Mostrar_Recibo()
        text:'Mostrar info'
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.8, "center_y": 0.1}
        size_hint:(0.1,0.1)
        line_color: 0, 0, 0, 0
        on_press: root.manager.current = 'Pedido_proceso'
        on_press: root.Ocultar()
        Image:
            source:'Imagen/hacer_pedido.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y
<pedido_proceso>
    name:'Pedido_proceso'
    Image:
        source:'Imagen/Titulo6.png'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size_hint:(0.5,0.5)
    Image:
        source:'Imagen/motico.png'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint:(0.5,0.5)
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.2+0.05}
        size_hint:(0.1/2,0.1/2)
        line_color: 0, 0, 0, 0
        text:'Hacer otro pedido'
        on_press: root.manager.current = 'Seleccion'
   
    MDRectangleFlatButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint:(0.1/2,0.1/2)
        line_color: 0, 0, 0, 0
        text:'Cancelar pedido'
        on_press: root.manager.current = 'menu'

"""
#Se crea la clase frito 
class Frito():
    #Este metodo ayuda a detectar que tipo de frito quiere el usuario
    def tipo_f(self,select):
       if select=='papa':
           Tipo='Papa'
       elif select =='Empanada':
            Tipo='Empanada'   
       elif select=='Arepa':
            Tipo='Arepa'
       self.Tipo=Tipo
       return Tipo
    #Este metodo ayuda a detectar que preparacion desea el usuario en su frito
    def preparacion(self,select):
        if select=='Horneado':
            prepar='Horneado'
        elif select=='Frito':
            prepar='Frito'
        self.prepar = prepar
    #Este metodo ayuda a detectar el relleno que elegio el usuario
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
    #Este metodo ayuda a detectar el relleno adicional que elegio el usuario si quiere o no
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
    #Detecta que tipo de salsa quiere el usuario 
    def salsa_f(self,select):
        if select == 'Salsa_Rosada':
                Salsa='Rosada'
        elif select == 'Salsa_Picante':
                Salsa='Picante'
        elif select == 'Salsa_Tartara':
                Salsa='Tartara'
        elif select == 'Salsa_Suero':
                Salsa='Suero'
        elif select == 'nada':
                Salsa='Ninguno'
        self.Salsa = Salsa

    #El metodo mostrar nos ayuda al que al final muestre la informacion que pidio el usuario
    def mostrar(self,n):
        if(n==1):
         desplegar= f'{self.Tipo}'
        elif(n==2):
         desplegar= f'{self.prepar}'
        elif(n==3):
         desplegar= f'{self.relle}'
        elif(n==4):
         desplegar= f'{self.rellead}'
        elif(n==5):
         desplegar= f'{self.Salsa}'
        return desplegar


#Se crea el objeto frito de la clase frito
frito=Frito()


#Esta clases ayudan manejar las diferentes ventanas de nuestra app:
# "Screen" es una herramienta de Kivy que nos ayuda a detectar que es una pantalla
#La clase "MenuScreen" muestra la pantalla de inicio 
class MenuScreen(Screen):
    pass
#La clase "SeleccionScreen"  nos muestra los tipos de frito de nuestra app
class SeleccionScreen(Screen):
    #El metodo "Tipofrito" es llamado de un boton que nos ayudara para detectar el tipo de frito
     def Tipofrito(self,n):
        #con el metodo de la clase frito detectara el tipo de frito que quiere el usuario
        frito.tipo_f(n)
#La clase "PreparacionScreen" otra clase que nos muestra la pantalla de preparacion
class PreparacionScreen(Screen):
     #El metodo "TipoPrepa" es llamado de un boton que nos ayudara a llamar al metodo del objeto frito
    def TipoPrepa(self,n):
        #con el metodo de la clase frito detectara la preparacion del usuario

        frito.preparacion(n)       
#La clase "IngredientesScreen" otra clase que nos muestra la pantalla de los ingredientes
    
class IngredientesScreen(Screen):
   #El metodo "tiporelle" es llamado de un boton que nos ayudara a llamar al metodo del objeto frito

    def tiporelle(self,n):
      #con el metodo de la clase frito detectara el relleno del usuario
        frito.relleno(n)
#La clase "IngredienteAdScreen" otra clase que nos muestra la pantalla de los ingredientes adicionales     
class IngredienteAdScreen(Screen):
    #El metodo "TiporelleAd" es llamado de un boton que nos ayudara a llamar al metodo del objeto frito

    def TiporelleAd(self,n):
        #con el metodo de la clase frito detectara el relleno adicional del usuario

        frito.relleno_ad(n)
#La clase "salsa" otra clase que nos muestra la pantalla de las salsa   
class salsa(Screen):
   #El metodo "salsa" es llamado de un boton que nos ayudara a llamar al metodo del objeto frito

    def salsa(self,n):
       frito.salsa_f(n)
#Fianlmente la clase recibo esta clase nos mostrara a traves de un label de kivymd la informacion del frito
class recibo(Screen):
    #Conexion con el boton de mostrar recibo
   def Mostrar_Recibo(self):
       self.ids.Titulo_tipo.text='Tipo de frito:'
       self.ids.Titulo_Preparacion.text='Preparación:'
       self.ids.Titulo_Relleno.text='Relleno:'
       self.ids.Titulo_RellenoAD.text='Relleno Adicional:'
       self.ids.Titulo_salsa.text='Salsa:'
       self.ids.Informacion_Tipo.text=f'{frito.mostrar(1)}'
       self.ids.Informacion_Prepa.text=f'{frito.mostrar(2)}'
       self.ids.Informacion_Relle.text=f'{frito.mostrar(3)}'
       self.ids.Informacion_RelleAd.text=f'{frito.mostrar(4)}'
       self.ids.Informacion_Salsa.text=f'{frito.mostrar(5)}'
       self.ids.info.pos_hint={'center_x':0.7,'center_y':0.3}
   #Conexion con el boton de esconder el recibo

   def Ocultar(self):
       self.ids.Titulo_tipo.text=' '
       self.ids.Titulo_Preparacion.text=' '
       self.ids.Titulo_Relleno.text=' '
       self.ids.Titulo_RellenoAD.text=' '
       self.ids.Titulo_salsa.text=' '
       self.ids.Informacion_Tipo.text=' '
       self.ids.Informacion_Prepa.text=' '
       self.ids.Informacion_Relle.text=' '
       self.ids.Informacion_RelleAd.text=' '
       self.ids.Informacion_Salsa.text=' '
       self.ids.info.pos_hint={'center_x':0.5,'center_y':0.5}
#Esta clase simula que el pedido ya se envio y estara pronto para entregar
class pedido_proceso(Screen):
    pass

#Screen manager es una clase de Kivy que nos ayuda a controlar las pantallas
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SeleccionScreen(name='Seleccion'))
sm.add_widget(PreparacionScreen(name='Preparacion'))
sm.add_widget(IngredientesScreen(name='Igrediente'))
sm.add_widget(IngredienteAdScreen(name='IngredienteAD'))
sm.add_widget(salsa(name='salsa'))
sm.add_widget(recibo(name='recibo'))
sm.add_widget(pedido_proceso(name='Pedido_proceso'))
#Esta clase carga nuestro archivo .kv para asi mostrarlo a la pantalla
class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
#Este condicional ayuda mucho para detectar que debe correr 
if __name__ == '__main__':       
  DemoApp().run()

