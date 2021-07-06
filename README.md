# design-patternss-learn

## Singleton pattern

Su objetivo es asegurar que una clase tiene únicamente una instancia. La razón más común es para controlar el acceso a algun recurso compartido, como una BBDD o un fichero.
Imagina que has creado un objeto, pero tras un tiempo quieres crear otro. En vez de recibir un objeto nuevo, recibirás el creado previamente. Esto no puede lograrse con un constructor al uso.

SOLUCION:
* Hacer el constructor por defecto privado, para evitar que otros objetos usen el operador new
* Crear un método estático de creación que funciona como constructor. Este método llamará al constructor privado para crear un objeto y lo guarda en un campo estático.

HOW TO:
* Añadir un campo privado estático para guardar la clase
* Declara un método público de creación para coger el Singleton
* Implementar una inicializacion lazy dentro del método estático. Debería crear un nuevo objeto con la primera llamada y ponerlo en el campo estático. El método siempre debe devolver la instancia en todas las llamadas siguientes.
* Haz el constructor de la clase privado. El método estático de la clase podrá llamar al constructor, pero no los demás objetos.
* Hay que reemplazar las llamadas al constructor de la clase (ahora privado) y sustituirlo por llamadas al método estático de creación

## Factory

Imagina que creas una aplicación de gestión logística. La primera versión de la app solo puede manejar transporte por camión, por lo que la mayoría del código usa la clase Camión.

En un tiempo, la aplicación es muy popular y recibes muchas peticiones para que se incorporte logística marítima.

¿Qué ocurre con el código? La mayoría del código está acoplada a la clase Camión. Añadir la clase Barco en la aplicación requeriría hacer cambios en todo el código.

SOLUCION

* El patrón factory sugiere que se reemplacen las llamadas directas al constructor (usando el operador new) con llamadas a una método especial facotry. Los objetos se siguen creando mediante el método new, pero se llama desde el método factoria.

Parece que el cambio no es muy grande, pero ahora podemos reescribir el método factoria en una subclase y cambiar la clase de productos creados por el método.

La limitación es que la factoría devolverá diferentes tipos de productos solo si éstos tienen una clase base común o interface. El método factoria de la clase base deberá tener su tipo retornado declarado.