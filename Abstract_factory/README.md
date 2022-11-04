# Abstract_factory
Este patrón se utiliza para la creación de objetos sin necesidad de especificar la clase completa, por lo que el objeto creado se puede modificar fácilmente. Normalmente se utiliza cuando en el código se utilizan varias familias de productos relacionados, donde no queremos depender de clases concretas de productos. En segundo lugar, las clases heredan el Producto abstracto para que las familias se puedan aplicar a objetos específicos.
El concrete Factory que es el que representa las creaciones específicas que servirán para poder crear todas las instancias de clases de la familia, y por último se define la estructura de estas creaciones las cuales deberán proporcionar una método para cada una de las clases de la familia.

