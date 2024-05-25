from pathlib import Path
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFileDialog,QComboBox,QApplication,QFormLayout,QMainWindow,QPushButton,QWidget,QLabel,QHBoxLayout,QGridLayout, QLineEdit, QSizePolicy, QMessageBox

class Empleado:
    def __init__(self, NombreEmpleado:str, AreaEmpleado:str, PuestoEmpleado:str) -> None:
        self._NombreEmpleado=NombreEmpleado
        self._AreaEmpleado=AreaEmpleado
        self._PuestoEmpleado=PuestoEmpleado
    
    def AnadirEmpleado(self)->None:
        self._NombreEmpleado=input("Dame el nombre del empleado a registrar: ")
        self._AreaEmpleado=input("Dame el area en la que el empleado trabaja: ")
        self._PuestoEmpleado=input("Dame el puesto del empleado: ")
        print(self._AreaEmpleado, self._NombreEmpleado, self._PuestoEmpleado)

    
    def CrearArchivoEmpleados(self)->None:
        ruta_archivo=Path("Empleado.txt")
        """
        Nombre|Puesto|Area
        Juan|Almacen|Pasante
        Monica|Administracion|Gerente
        """
        encabezados="Nombre|Puesto|Area"
        with ruta_archivo.open('w', encoding='utf-8') as archivo:
            archivo.write(encabezados)
    
    def ModificarArchivoEmpleado(self)->None:
        self.AnadirEmpleado()
        ruta_archivo=Path("Empleado.txt")
        datos=[f"{self._NombreEmpleado}|{self._PuestoEmpleado}|{self._AreaEmpleado}"]
        with ruta_archivo.open('a') as archivo:
            for registro in datos:
                archivo.write("\n" + registro)

    def LeerArchivo(self)->None:
        ruta_archivo=Path("Empleado.txt")
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados=archivo.readline().strip().split('|')
                for linea in archivo:
                    campos=linea.strip().split('|')
                    registro={}
                    for i in range(len(encabezados)):
                        registro[encabezados[i]]=campos[i]
                    self._NombreEmpleado=registro['Nombre']
                    self._PuestoEmpleado=registro['Puesto']
                    self._AreaEmpleado=registro['Area']
    
    def BusquedaEmpleado(self)->None:
        searchopc=input("Que empleado quiere buscar? ")
        found=False
        ruta_archivo=Path("Empleado.txt")
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados=archivo.readline().strip().split('|')
                for linea in archivo:
                    campos=linea.strip().split('|')
                    registro={}
                    for i in range(len(encabezados)):
                        registro[encabezados[i]]=campos[i]
                    if registro['Nombre']==searchopc:
                        print(registro['Nombre'], registro['Puesto'], registro['Area'])
                        found=True
            if found==False:
                print("No se encontró el empleado en la base de datos")
        else:
            print("El archivo no existe.")

class Hardware (Empleado):
    def __init__(self, Empleado:str, NombreHardware:str, TagHardware:int) -> None:
        self.NombreHardware=NombreHardware
        self.Empleado=Empleado
        self.TagHardware=TagHardware
        
class Software (Empleado):
    def __init__(self, NombreSoftware: str,NombreEmpleado: str, AreaEmpleado: str, PuestoEmpleado: str) -> None:
        super().__init__(NombreEmpleado, AreaEmpleado, PuestoEmpleado)
        self.NombreSoftware=NombreSoftware

class ventana (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.iniciarventana()
        self.setCentralWidget(self.iniciarventana())
        self.show()
        self.logininfo={"admin":"admin"}
        self.empleadosinfo=[]
        self.softwareinfo=[]
        self.hardwareinv=[]
        self.hardwareinfo=[]

    def iniciarventana(self):
        self.setGeometry(150,250,200,250)
        self.setWindowTitle("PASH")
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        self.username_label=QLabel("Nombre de Usuario: ")
        self.password_label=QLabel("Contraseña: ")
        self.login_button=QPushButton("Login")
        self.exit_button=QPushButton("Salir")
        self.username_label_edit=QLineEdit()
        self.password_label_edit=QLineEdit()

        form_layout.addRow(self.username_label,self.username_label_edit)
        form_layout.addRow(self.password_label,self.password_label_edit)
        form_layout.addRow(self.login_button)
        form_layout.addRow(self.exit_button)

        self.login_button.clicked.connect(self.NewWindow)
        self.exit_button.clicked.connect(self.close)

        return central_widget
    
    def close(self):
        super().close()
    
    def ventanainicio(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        
        welcome_label=QLabel("Bienvenido al PASH")
        Exit_button=QPushButton("Salir del Programa")
        Hardware_button=QPushButton("Acceder a ventana Hardware")
        Software_button=QPushButton("Acceder a ventana Software ")
        Empleado_button=QPushButton("Acceder a ventana Empleado")

        form_layout.addRow(welcome_label)
        form_layout.addRow(Hardware_button)
        form_layout.addRow(Software_button)
        form_layout.addRow(Empleado_button)
        form_layout.addRow(Exit_button)
        
        Empleado_button.clicked.connect(self.show_empleado)
        Hardware_button.clicked.connect(self.show_hardware)
        Software_button.clicked.connect(self.show_software)
        Exit_button.clicked.connect(self.show_login)

        return central_widget
    
    def ventanaempleado(self):
        self.empleadosinfo.clear()
        self.cargar_archivo_empleados()
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        
        empleado_label=QLabel("Bienvenido a las funciones de empleado")
        add_empleadobutton=QPushButton("Añadir Empleado")
        busqueda_empleadobutton=QPushButton("Búsqueda de Empleados")
        return_button=QPushButton("Regresar a la ventana principal")
        
        form_layout.addRow(empleado_label)
        form_layout.addRow(add_empleadobutton)
        form_layout.addRow(busqueda_empleadobutton)
        form_layout.addRow(return_button)

        return_button.clicked.connect(self.show_main)
        add_empleadobutton.clicked.connect(self.show_registerempleado)
        busqueda_empleadobutton.clicked.connect(self.show_busquedaempleado)

        return central_widget
    
    def ventanahardware(self):

        self.hardwareinfo.clear()
        self.hardwareinv.clear()
        self.empleadosinfo.clear()

        self.cargar_archivo_empleados()
        self.cargar_hardware_empleados()
        self.cargar_inventario_hardware()

        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        hardware_label=QLabel("Bienvenido a las funciones de Hardware")
        add_hardwarebutton=QPushButton("Añadir Hardware al inventario")
        asign_hardwarebutton=QPushButton("Asignar Hardware a un empleado")
        reporte_hardwarebutton=QPushButton("Generar un reporte de Hardware")
        return_button=QPushButton("Regresar a la ventana principal")


        form_layout.addRow(hardware_label)
        form_layout.addRow(add_hardwarebutton)
        form_layout.addRow(asign_hardwarebutton)
        form_layout.addRow(reporte_hardwarebutton)
        form_layout.addRow(return_button)

        return_button.clicked.connect(self.show_main)
        add_hardwarebutton.clicked.connect(self.showasignarinv)
        asign_hardwarebutton.clicked.connect(self.show_asignar_hardware)
        reporte_hardwarebutton.clicked.connect(self.showreportehardware)

        return central_widget

    def ventanasoftware(self):
        self.empleadosinfo.clear()
        self.cargar_archivo_empleados()
        
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        Software_label=QLabel("Bienvenido a las funciones de Software")
        asign_softwarebutton=QPushButton("Asignar Software a un empleado")
        reporte_softwarebutton=QPushButton("Generar un reporte de Software")
        return_button=QPushButton("Regresar a la ventana principal")

        form_layout.addRow(Software_label)
        form_layout.addRow(asign_softwarebutton)
        form_layout.addRow(reporte_softwarebutton)
        form_layout.addRow(return_button)

        return_button.clicked.connect(self.show_main)
        asign_softwarebutton.clicked.connect(self.show_asignarsoftware)
        reporte_softwarebutton.clicked.connect(self.show_generar_reporte_software)

        return central_widget
    #ventanas software

    def ventanaasignarsoftware(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)

        label=QLabel("Asignar Software")
        self.nameboxs=QComboBox()
        self.actualizar_box_software()

        label_name=QLabel("Empleado a asignar software: ")
        software_label=QLabel("Nombre del software a asignar: ")
        self.software_label_edit=QLineEdit()
        accept_button=QPushButton("Asignar Software")
        exit_button=QPushButton("Salir al menu software")

        form_layout.addRow(label)
        form_layout.addRow(label_name,self.nameboxs)
        form_layout.addRow(software_label,self.software_label_edit)
        form_layout.addRow(accept_button,exit_button)

        accept_button.clicked.connect(self.asignarsoftware)
        exit_button.clicked.connect(self.show_software)

        return central_widget

    def ventanareportesoftware(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)

        label=QLabel("Reporte de software")
        register_button=QPushButton("Generar Reporte")
        exit_button=QPushButton("Salir")
        self.nameboxrs=QComboBox()
        
        self.actualizar_box_software_reporte()
        form_layout.addRow(label)
        form_layout.addRow(self.nameboxrs)
        form_layout.addRow(register_button,exit_button)

        register_button.clicked.connect(self.generar_reporte_software)
        exit_button.clicked.connect(self.show_software)

        return central_widget


    #ventanas empleados
    def ventanacrearempleado(self):

        central_widget=QWidget(self)
        grid_layout=QFormLayout(central_widget)
        main_label=QLabel("Bienvenido al registro de Empleados.")
        empleado_label=QLabel("Nombre de Empleado: ")
        self.empleado_label_edit=QLineEdit()
        area_label=QLabel("Area de trabajo: ")
        self.area_label_edit=QLineEdit()
        rol_label=QLabel("Rol del empleado: ")
        self.rol_label_edit=QLineEdit()
        finish_button=QPushButton("Registrar empleado")
        grid_layout.addRow(main_label)
        grid_layout.addRow(empleado_label,self.empleado_label_edit)
        grid_layout.addRow(area_label,self.area_label_edit)
        grid_layout.addRow(rol_label,self.rol_label_edit)
        grid_layout.addRow(finish_button)



        finish_button.clicked.connect(self.Register_empleado)

        return central_widget

    def ventanabusquedaempleado(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)

        label=QLabel("Busqueda de Usuario")
        name_label=QLabel("Nombre a buscar: ")
        self.name_label_edit=QLineEdit()
        done_button=QPushButton("Buscar empleado")

        form_layout.addRow(label)
        form_layout.addRow(name_label)
        form_layout.addRow(self.name_label_edit)
        form_layout.addRow(done_button)
        done_button.clicked.connect(self.search_empleado)

        return central_widget

    #ventana hardware
    def ventanaasignarhardware(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        label=QLabel("Asignar Hardware")
        self.name_box=QComboBox()
        name_label=QLabel("Empleado a asignar hardware: ")
        hardware_label=QLabel("Hardware a asignar: ")
        tag_label=QLabel("Etiqueta asignada al hardware: ")
        self.tag_label_edit=QLineEdit()
        self.hardware_box=QComboBox()
        register_button=QPushButton("Asignar Hardware")
        exit_button=QPushButton("Salir")

        self.update_hardware_name_box()
        self.update_name_box()
        
        form_layout.addRow(label)
        form_layout.addRow(name_label,self.name_box)
        form_layout.addRow(hardware_label,self.hardware_box)
        form_layout.addRow(tag_label, self.tag_label_edit)
        form_layout.addRow(register_button,exit_button)

        register_button.clicked.connect(self.asignarhardware)
        exit_button.clicked.connect(self.show_hardware)

        return central_widget

    def asignarhardware(self):

        
        hardware=self.hardware_box.currentText()
        nombre=self.name_box.currentText()
        tag=self.tag_label_edit.text()
        ruta_archivo=Path("InventarioHardware.txt")
        
        repeats=False

        for i in range(len(self.hardwareinfo)):
            if tag==self.hardwareinfo[i].TagHardware:
                repeats=True
                
        if repeats==True:
            QMessageBox.critical(self,"Error","Esta etiqueta ya esta asignada a otro hardware")

        if ((hardware and nombre) !=None) and repeats==False:
            self.apphardware(hardware,tag,nombre)
            QMessageBox.information(self,"Correcto","Se registro el hardware con exito")
            if ruta_archivo.exists():
                with ruta_archivo.open('w') as archivo:
                    archivo.write("Hardware|Cantidad")

            for i in range(len(self.hardwareinv)):
                for x,y in self.hardwareinv[i].items():
                    if x==hardware:
                        y=int(y)-1

                    if ruta_archivo.exists():
                        with ruta_archivo.open('a') as archivo2:
                            archivo2.write(f"\n{x}|{y}")
        else:
            QMessageBox.critical(self,"Error","Ocurrio un error al asignar el hardware")

        
        
        self.show_hardware()

    def show_asignar_hardware(self):
        self.setCentralWidget(self.ventanaasignarhardware())

    def update_name_box(self):
        self.name_box.clear()
        for i in range(len(self.empleadosinfo)):
            self.name_box.addItem(self.empleadosinfo[i]._NombreEmpleado)

    def update_hardware_name_box(self):
        self.hardware_box.clear()
        for i in range(len(self.hardwareinv)):
            print(len(self.hardwareinv))
            for x,y in self.hardwareinv[i].items():
                if int(y)>0:
                    self.hardware_box.addItem(x)

    def ventanaasignarinventario(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)

        label=QLabel("Asignar Inventario")
        name_label=QLabel("Nombre del Hardware: ")
        self.name_label_edit=QLineEdit()
        cant_label=QLabel("Stock a agregar: ")
        self.cant_label_edit=QLineEdit()
        agregar_button=QPushButton("Añadir Inventario")
        exit_button=QPushButton("Salir")

        form_layout.addRow(label)
        form_layout.addRow(name_label,self.name_label_edit)
        form_layout.addRow(cant_label,self.cant_label_edit)
        form_layout.addRow(agregar_button,exit_button)

        agregar_button.clicked.connect(self.asignarinventario)
        return central_widget

    def asignarinventario(self):
        producto=self.name_label_edit.text()
        cantidad=self.cant_label_edit.text()
        for i in range(len(self.hardwareinv)):
            for x,y in self.hardwareinv[i].items():
                if x==producto:
                    self.hardwareinv[i][producto]=int(y)+int(cantidad)
                    self.overwriteinvhardware()
                    QMessageBox.information(self,"Modificado","El producto ya existía, solo se modificó su stock en inventario")
                else:
                    dicc={producto:cantidad}
                    self.hardwareinv.append(dicc)
                    QMessageBox.information(self,"Correcto","Se registro el producto correctamente")
                    self.appinvhardware(producto,cantidad)
        self.show_hardware()
               
    def showasignarinv(self):
        self.setCentralWidget(self.ventanaasignarinventario())

    def reportehardware(self):
        central_widget=QWidget(self)
        form_layout=QFormLayout(central_widget)
        self.report_box=QComboBox()
        label=QLabel("Generar Reporte")
        report_label="Empleado a generar reporte: "
        report_button=QPushButton("Generar reporte")
        exit_button=QPushButton("Salir")

        self.update_report_box()

        form_layout.addRow(label)
        form_layout.addRow(report_label,self.report_box)
        form_layout.addRow(report_button,exit_button)

        report_button.clicked.connect(self.generar_reporte_hardware)
        exit_button.clicked.connect(self.show_hardware)

        return central_widget

    def showreportehardware(self):
        self.setCentralWidget(self.reportehardware())

    def update_report_box(self):
        self.report_box.clear()
        repeats=""
        for i in range(len(self.hardwareinfo)):
            if repeats=="":
                self.report_box.addItem(self.hardwareinfo[i].Empleado)
                repeats=self.hardwareinfo[i].Empleado
            elif repeats != "":
                if repeats==self.hardwareinfo[i].Empleado:
                    continue
                else:
                    self.report_box.addItem(self.hardwareinfo[i].Empleado)
                    repeats=self.hardwareinfo[i].Empleado
            
    def generar_reporte_hardware(self):
        nombre=self.report_box.currentText()
        ruta_archivo=Path("ReporteHardware.txt")
        with ruta_archivo.open('w') as archivo:
                    archivo.write(f"{nombre}")
        for i in range(len(self.hardwareinfo)):
            if nombre==self.hardwareinfo[i].Empleado:
                with ruta_archivo.open('a') as archivo:
                    archivo.write(f"\nHardware: {self.hardwareinfo[i].NombreHardware}\nTag:{self.hardwareinfo[i].TagHardware}")
        
        QMessageBox.information(self,"Correcto","Se genero el reporte en un archivo txt")
        self.show_hardware()

    def NewWindow(self):
        username=self.username_label_edit.text()
        password=self.password_label_edit.text()

        if username in self.logininfo and password==self.logininfo["admin"]:
            QMessageBox.information(self,"Bienvenido", f"Bienvenido al sistema, usuario {username}")
            self.setCentralWidget(self.ventanainicio())
        else:
            QMessageBox.critical(self,"Error", f"El usuario {username} o la contraseña estan incorrectas. Intente nuevamente")
            self.refresh()

    def show_login(self):
        QMessageBox.information(self,"Log Out", "Hasta Luego")
        self.setCentralWidget(self.iniciarventana())
        self.refresh()

    def show_main(self):
        QMessageBox.information(self,"Regresar", "Regresando a la ventana principal")
        self.setCentralWidget(self.ventanainicio())
    
    def show_empleado(self):
        QMessageBox.information(self,"Empleado","Entrando a el área de empleados")
        self.setCentralWidget(self.ventanaempleado())

    def show_hardware(self):
        QMessageBox.information(self,"Hardware", "Entrando al Area de Hardware")
        self.setCentralWidget(self.ventanahardware())

    def show_software(self):
        QMessageBox.information(self,"Software", "Entrando al area de Software")
        self.setCentralWidget(self. ventanasoftware())
    
    def show_registerempleado(self):
        self.setCentralWidget(self.ventanacrearempleado())

    def show_busquedaempleado(self):

        self.setCentralWidget(self.ventanabusquedaempleado())

    def Register_empleado(self):
        QMessageBox.information(self,"Registro", "Registro Exitoso, volviendo al menu de empleados")
        empleado=self.empleado_label_edit.text()
        area=self.area_label_edit.text()
        rol=self.rol_label_edit.text()
        self.appempleado(empleado,area,rol)
        self.setCentralWidget(self.ventanaempleado())

    def refresh(self):
        self.username_label_edit.clear()
        self.password_label_edit.clear()

    def search_empleado(self):
        empleado=self.name_label_edit.text()
        found=False
        for i in range(len(self.empleadosinfo)):
            if empleado == self.empleadosinfo[i]._NombreEmpleado:
                QMessageBox.information(self,"Encontrado",f"La informacion relacionada con {empleado} es la siguiente: \nNombre: {empleado}\nArea: {self.empleadosinfo[i]._AreaEmpleado}\nRol: {self.empleadosinfo[i]._PuestoEmpleado}")
                found=True
                self.setCentralWidget(self.ventanaempleado())
        if found==False:
            QMessageBox.information(self,"No encontrado", "Lo sentimos, no tenemos registro de ese empleado en nuestra base de datos")
            self.setCentralWidget(self.ventanaempleado())

    def actualizar_box_software(self):
        self.nameboxs.clear()
        for i in range(len(self.empleadosinfo)):
            self.nameboxs.addItem(self.empleadosinfo[i]._NombreEmpleado)

    def actualizar_box_software_reporte(self):
        self.nameboxrs.clear()
        for i in range(len(self.softwareinfo)):
            self.nameboxrs.addItem(self.softwareinfo[i]._NombreEmpleado)

    def asignarsoftware(self):
        empleado=self.nameboxs.currentText()
        found=False
        for i in range(len(self.empleadosinfo)):
            if empleado==(self.empleadosinfo[i]._NombreEmpleado):
                found=True
                objeto=Software(self.software_label_edit.text(), self.empleadosinfo[i]._NombreEmpleado,self.empleadosinfo[i]._AreaEmpleado, self.empleadosinfo[i]._PuestoEmpleado)
                self.softwareinfo.append(objeto)
                QMessageBox.information(self,"Correcto",f"Se asigno el software al empleado {empleado}")

        if found==False:
            QMessageBox.information(self,"Fallo","No se pudo agegar el software al empleado.")

        self.show_software()

    def show_asignarsoftware(self):
        self.setCentralWidget(self.ventanaasignarsoftware())

    def generar_reporte_software(self):
        file_path=Path("ReporteSoftware.txt")
        empleado=self.nameboxrs.currentText()
        software=""
        found=False
        for i in range(len(self.softwareinfo)):
            if empleado==(self.softwareinfo[i]._NombreEmpleado):
                software=self.softwareinfo[i].NombreSoftware
                found=True
        if found==False:
            QMessageBox.critical(self,"Error","No se pudo encontrar a ese empleado")     
            self.show_software()
        else:
            with file_path.open('w') as archivo:
                archivo.write(f"Empleado: {empleado}\nSoftware Asignado: {software}")
            QMessageBox.information(self,"Correcto","Se genero el reporte txt con exito")
            self.show_software()

    def show_generar_reporte_software(self):
        self.setCentralWidget(self.ventanareportesoftware())
        
    def cargar_archivo_empleados(self):
        ruta_archivo=Path("Empleado.txt")
        if ruta_archivo.exists:
            with ruta_archivo.open('r',encoding='utf=8') as archivo: 
                encabezados=archivo.readline().strip().split('|')
                print(encabezados)
                for linea in archivo:
                    campos=linea.strip().split('|')
                    registro={}
                    for i in range(len(encabezados)):
                        registro[encabezados[i]]=campos[i]
                    NombreEmpleado=registro['Nombre']
                    PuestoEmpleado=registro['Puesto']
                    AreaEmpleado=registro['Area']
                    objeto=Empleado(
                        NombreEmpleado,AreaEmpleado,PuestoEmpleado
                    )
                    self.empleadosinfo.append(objeto)

    def appempleado(self,empleado,area,rol):
        ruta_archivo=Path("Empleado.txt")
        if ruta_archivo.exists:
             with ruta_archivo.open('a',encoding='utf=8') as archivo:
                 archivo.write(f"\n{empleado}|{rol}|{area}")

    def cargar_inventario_hardware(self):
        ruta_Archivo=Path("InventarioHardware.txt")
        if ruta_Archivo.exists():
                with ruta_Archivo.open('r', encoding='utf=8') as archivo2:
                    encabezados2=archivo2.readline().strip().split('|')
                    print(encabezados2)
                    for linea in archivo2:
                        campos2=linea.strip().split('|')
                        registro2={}
                        for i in range(len(encabezados2)):
                            registro2[encabezados2[i]]=campos2[i]
                        nombre=registro2['Hardware']
                        cantidad=registro2['Cantidad']
                        dicc={nombre:cantidad}
        
                        self.hardwareinv.append(dicc)

    def cargar_hardware_empleados(self):
        ruta_archivo=Path("HardwareAsignado.txt")
        if ruta_archivo.exists:
            with ruta_archivo.open('r', encoding='utf=8') as archivo:
                encabezados=archivo.readline().strip().split('|')
                print(encabezados)
                for linea in archivo:
                    campos=linea.strip().split('|')
                    registro={}
                    for i in range(len(encabezados)):
                        registro[encabezados[i]]=campos[i]
                    NombreEmpleado=registro['Nombre']
                    hardware=registro['Hardware']
                    Tag=registro['Tag']
                    objeto=Hardware(NombreEmpleado,hardware,Tag)
                    self.hardwareinfo.append(objeto)

    def apphardware(self, hardware,tag,empleado):
        ruta_archivo=Path("HardwareAsignado.txt")
        if ruta_archivo.exists:
             with ruta_archivo.open('a',encoding='utf=8') as archivo:
                 archivo.write(f"\n{empleado}|{hardware}|{tag}")

    def appinvhardware(self,hardware,cantidad):
        ruta_archivo=Path("InventarioHardware.txt")
        if ruta_archivo.exists:
             with ruta_archivo.open('a',encoding='utf=8') as archivo:
                 archivo.write(f"\n{hardware}|{cantidad}")

    def overwriteinvhardware(self):
        ruta_archivo=Path("InventarioHardware.txt")
        with ruta_archivo.open('w') as archivo:
            archivo.write("Hardware|Cantidad")
            for i in range(len(self.hardwareinv)):
                for x,y in self.hardwareinv[i].items():
                    archivo.write(f"\n{x}|{y}")


app=QApplication(sys.argv)

window=ventana()

sys.exit(app.exec())




