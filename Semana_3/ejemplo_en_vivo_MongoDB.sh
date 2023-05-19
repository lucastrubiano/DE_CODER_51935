-- Version mongo
mongo

-- Cambiar a la base de datos admin
use admin

-- Autenticarme con usuario root
db.auth("root", "example");

-- Ver databases disponibles
show dbs

-- seleccionar una BD, crearla previamente
use datos

-- verificar BD seleccionada
db

-- Crear usuarios
db.createUser({"user":"lucas", pwd:"lucas123",roles:["readWrite","dbAdmin"]})

-- Crear colecciones
db.createCollection('clientes');
show collections;

-- Insertar datos
db.clientes.insert({nombres:"Lucas", apellido:"Trubiano"});
db.clientes.insert({nombres:"Fernando", apellido:"Pareja"});
db.clientes.insert({nombres:"Lautaro", apellido:"Odoni"});

-- Ver registros de coleccion
db.clientes.find();

-- Ver de mejor manera
db.clientes.find().pretty();

-- Ver registros de coleccion con filtro
db.clientes.find({nombres:"Lucas"});

-- Editar registros de coleccion
db.clientes.update({nombres:"Lucas"},{$set:{apellido:"Coder"}});

-- Eliminar registros de coleccion
db.clientes.remove({nombres:"Julio"});