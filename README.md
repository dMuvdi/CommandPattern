## Command Pattern

El patrón command se basa principalmente en cuatro parámetros básicos, el command, invoker, client, reciever. Estos cuatro relacionados entre sí, permiten encapsular una solicitud como un objeto (Command) que ha utilizado la información de un reciever, y que el invoker tomará para finalmente ejecutarla (método execute) y entregársela al client, soportando también el undo, o deshacer de los commands.
