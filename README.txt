#########################################################################
#########################    MANIFEST      ##############################
#########################################################################

name = Nombre de la aplicación
icon = Icono pequeño del listado de aplciaciones
icon_image = Icono más grande en el apartado de más información de la aplicación
summary = Pequeño resumen de la aplicación
description = Descripción más completa de la aplicación
author = Autor de la aplicación
website = Web relacionada a la aplicación
category = Categoría de la aplicación(En nuestro caso para que salga en la categoría Web sería[Website/Website])
version = Versión de la aplicación
data = Son los archivos que siempre van a estar cargados(Normalmente son las llamadas a las vistas)
demo = Son los ficheros que rellenan datos por defecto en la aplicación
assets = Son los ficheros que se cargan dinámicamente como js o css en los módulos creados hay diferentes ejemplos

#########################################################################
#########################    MODELOS      ###############################
#########################################################################

En el modelo se define una clase dando igual su nombre y que tenga como parametro:
    -models.model => Clase de Python para definir un nuevo módelo
    -models.TransientModel => Usados para interacción tipo asistente con el usuario y la usuaria. 
        Sus datos son aún almacenados en la base de datos, pero se espera que sea temporal. 
        Un proceso de reciclaje limpia periódicamente los datos viejos de esas tablas. 
    -models.AbstractModel => Usado para crear un modelo abstracto y heredarlo

_name => Establece el nombre del modelo por el que se le va a llamar desde las vistas
_description => Establece una descripción del modelo
_order => Orden en el que salen los registros

Tipos de campos
--------------
Fields.
    -Char() =>  Campo de texto 
    -Text() => Campo de texto más grande que el char donde se pueden añadir líneas
    -Selection([(x,y),(a,b)]) => Selector de opciones establecidas en los parámetros
    -HTML() => Campo para establecer código HTML
    -Integer() => Campo númerico
    -Float((3,2)) => Campo con decimales, en los parámetros se establece los enteros y decimales
    -Date() => Campo de fecha 
    -DateTime() => Campo de fecha y hora
    -Boolean() => Campo booleano
    -Binary() => Campo binario como por ejemplo para almacenar imagenes

Atributos
--------------
string => Título que se mostrara en las vistas
default => Fija un valor por defecto
size => Establece el tamaño del campo
translate => Hace que los campos puedan ser traducidos
help => Texto de ayuda para el campo
required => Establecer campo como requerido
index => Crea un índice del campo en la base de datos
copy=False => Hace que el campo no se pueda copiar

Campos Reservados
----------------
create_uid => Usuario que crea el registro
created_date => Fecha y hora de cuando es creado el registro
write_uid => Usuario que ha modificado el registro
write_date => Fecha y hora de cuando es modificado el registro
name => Es usado por defecto para establecer el nombre del registro
active => Desactiva registros y asi no salen en las consultas
sequence => Número de orden de salida de un campo

Relaciones
-----------------
Many2one{

    Argumentos
    --------------
        -comodel_name => Modelo con el que se relaciona
        -string => Título de salida del campo
        -ondelete => {
            -Null(Defecto) => Al ser eliminado el registro relacionado se establece como vacío
            -Restrict => Arroja un error que previene de la relación
            -Cascade => Elimina también el registro relacionado
        }
        -context,domain => Aún no se muy bien el funcionamiento de esto
        -auto_join => Por defecto esta en false para reforzar las reglas de seguridad, si esta en True
            no tendrá seguridad y el usuario podrá ver los registros relacionados
}

Many2many{

    Argumentos
    --------------
        -comodel_name => Modelo con el que se relaciona
        -relation => Nombre de la tabla de relación
        -column1 => Campo para este registro
        -column2 => Campo para el otro registro
        -string => Título de salida del campo
        -ondelete => {
            -Null(Defecto) => Al ser eliminado el registro relacionado se establece como vacío
            -Restrict => Arroja un error que previene de la relación
            -Cascade => Elimina también el registro relacionado
        }
        -context,domain => Aún no se muy bien el funcionamiento de esto
        -auto_join => Por defecto esta en false para reforzar las reglas de seguridad, si esta en True
            no tendrá seguridad y el usuario podrá ver los registros relacionados
}

One2many{

    Argumentos
    --------------
        -comodel_name => Modelo con el que se relaciona
        -string => Título de salida del campo
        -inverse_name => Campo para relacionado a la inversa
}

Campos computados
---------------
    -Campos que se rellenan llamando a una funcion
    -Se utilizan añadiendo el parámetro compute="Nombre de la funcion"

Campos relacionados
----------------
    -Llamadas a campos que han sido relacionados en un campo anterior
    Si por ejemplo se ha relacionado canciones con cantantes y se quiere guardar en un campo el nombre del cantante
    se crea un campo con el parámetro (related=nombre_del_campo_relacionado.campo_del_modelo_relacionado)

----------
Se pueden establecer funciones para cambiar valor de los datos como por ejemplo lo realizado en el módulo de custom_crm
Se establecen funciones que cambian por ejemplo un booleano y en la vista se establece un botón que llame a esta función
cambiando su valor, al igual que hay un botón para eliminar el registro

HERENCIA
---------------------------------------
Para heredar un modelo se usará el campo _inherit, hay 3 tipos de herencia pero los que yo he usado son 2:
    -En el primer tipo de herencia se usa unicamente el campo _inherit="nombre_modulo",al usar este tipo los campos que se añadan
    se establecerán en el modelo padre.
    Se pueden añadir funcionalidades que cambien el funcionamiento del padre.
    Las vistas se usan las del padre y para modificarlas se usara el campo:
        <field name="inherit_id" ref="módulo.id_vista" />
    Y se usará xpath para establecer donde se añadirá el campo que hemos añadido o modificar la vista

    -En el segundo tipo de herencia se usa el campo _inherit="nombre_modulo" y el campo _name="modulo.nombre_modelo".
    Al añadir el segundo campo lo que estamos haciendo es crear un nuevo modelo heredando todo lo del modelo padre 
    En caso de los controladores y de las vistas se pueden copiar y adaptar a tu módelo
    En caso de querer modificar una vista del padre se haría el mismo procedimiento que en el otro tipo de herencia


#########################################################################
######################    CONTROLADORES      ############################
#########################################################################

Hasta ahora el principal funcionamiento que he usado ha sido el como establecer la respuesta que da las rutas establecidad en el 
controlador de la siguiente manera:
    @http.route([
        '/nose/prueba',
        '<model("modulo.modelo"):variable_en_la_que_se_almacena>'
    ])
    def funcion que responde a esa url
        En caso del retorno hasta ahora solo he retornado el render de las vistas
        Hay que importar request
        return request.render("modulo.id_vista", valores_que_se_le_pasan_al_return)
        Los valores que se pasan a traves del render son los que se iteran en la vista mediante Q-web


#########################################################################
###########################    VISTAS      ##############################
#########################################################################

Divido las vistas en dos apartados:
    -Templates para el back
    -Templates para el front

    En Back hay tres tipos de vistas:
        -Form
        -Tree
        -Kanban

Ejemplo de estructura para los formularios:
 <record id="modulo_modelo_view" model="ir.ui.view">
    <field name="name">modulo.modelo.form</field>
    <field name="model">modulo.modelo</field>
    <field name="arch" type="xml">
        <form string="título del formulario">
            <sheet>
                <group name="group_top">
                    <group name="group_left">
                        <field name="name" />(Pinto la salida de este campo)
                        <field name="artists" widget="many2many_tags" />(uso un widget para la selecion de las relaciones)
                    </group>
                    <group name="group_right">
                        <field name="image" widget="image" />(uso un widget para la salida y edición del a imagen)
                    </group>
                </group>
            </sheet>
        </form>
    </field>
</record>

Ejemplo de estructura para la salida del tree:

<record id="modulo_modelo_tree" model="ir.ui.view">
    <field name="name">modulo.modelo.tree</field>
    <field name="model">modulo.modelo</field>
    <field name="arch" type="xml">
        <tree string="Titulo_del_listado">
        (Columnas con los campos que se quieran mostrar)
            <field name="name" />
            <field name="artists" widget="many2many_tags" />(Vuelvo a usar un widget para la salida de las relaciones)
            <field name="record" />
        </tree>
    </field>
</record>

Ejemplo de estructura para la salida del kanban:

<record id="modulo_modelo_kanban" model="ir.ui.view">
            <field name="name">modulo.modelo.kanban</field>
            <field name="model">modulo.modelo</field>
            <field name="arch" type="xml">
                <kanban class="o_music_songs_kanban">
                    <field name="name" />
                    <field name="artists" />
                    <templates>
                        <t t-name="kanban-box">
                            <div t-attf-class="oe_kanban_global_click">
                                <div class="o_kanban_image">
                                    <img alt="Avatar"
                                        t-att-src="kanban_image('modulo.modelo', 'image', campo.id.raw_value)" />
                                </div>
                                <div class="oe_kanban_details">
                                    <strong class="o_kanban_record_title">
                                        <field name="name" />
                                    </strong>
                                    <div t-if="record.record.value">
                                        <t t-esc="record.record.value" />
                                    </div>
                                    <div class="o_kanban_record_title" widget="many2many_tags">
                                        <field name="artists" />
                                    </div>
                                </div>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
        </record>
