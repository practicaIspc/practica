El documento proporciona una guía detallada sobre Git y GitHub, enfocándose en el uso de ramas para el desarrollo colaborativo. A continuación, se presenta un resumen de los comandos y sus funciones, organizados desde los más básicos hasta los más avanzados.

### Comandos Básicos de Git

*   **`Git Init`**: Se utiliza para **iniciar el seguimiento de los archivos** de una carpeta, convirtiéndola en un repositorio Git local.
*   **`Git Status`**: Proporciona **toda la información necesaria sobre la rama actual**, mostrando el estado del repositorio.
*   **`Git Add`**: Permite **incluir los cambios de uno o varios archivos** para ser incluidos en el siguiente commit (prepararlos para el commit).
*   **`Git Commit`**: Esencialmente, **establece un punto de control** en el proceso de desarrollo, similar a un punto de guardado en un videojuego, al cual se puede volver más tarde si es necesario.

### Gestión de Ramas (Branches)

*   **`Git Branch`**: Este comando tiene múltiples usos:
    *   **Muestra un listado de las ramas** que existen en un proyecto.
    *   Indica **en qué rama te encuentras** en un momento dado.
    *   Se utiliza también para **borrar ramas**.
*   **`Git Checkout -b <nombre_de_tu_branch>`**: Se usa para **crear una nueva rama local y cambiar automáticamente a ella**.
*   **`Git Show-branch`**: Muestra **todas las ramas del proyecto junto con los commits realizados** en cada una.
*   **`Git Checkout <nombre_de_tu_branch>`**: Permite **moverse entre ramas existentes**, cambiando automáticamente todos los archivos del proyecto para que reflejen el contenido de la rama seleccionada.

### Interacción con Repositorios Remotos

*   **`Git Push`**: Se utiliza para **enviar los archivos que han sido incluidos en un commit al repositorio remoto**. Generalmente, se especifica el origen y el nombre de la rama.
*   **`Git Push Origin <nombre_de_tu_branch>`**: Es el comando específico para **publicar una rama determinada en el repositorio remoto** (comúnmente llamado 'origin').
*   **`Git Push -u Origin <nombre_de_tu_branch>`**: Configura la rama local para que su rama remota por defecto sea la especificada. Una vez hecho esto, se puede usar **`git push`** de forma simplificada para futuras subidas a esa rama.
*   **`Git Pull`**: Es un comando que **actualiza la versión local de un repositorio desde uno remoto**. Por defecto, recupera (`git fetch`) las nuevas confirmaciones y las fusiona (`git merge`) en tu rama local actual, además de actualizar las referencias de ramas remotas para otras ramas.
*   **`Git Clone <URL_del_repositorio>`**: Este comando permite **descargar el código de un proyecto publicado en un sitio como GitHub a tu ordenador**, creando un repositorio Git local que incluye todo el historial de cambios.

### Fusión de Ramas (Merging)

*   **`Git Merge <rama_a_fusionar>`**: Se utiliza para **fusionar el código de una rama específica** (por ejemplo, `ramaGit`) **en la rama actual** (por ejemplo, `master`), incorporando el trabajo realizado.
*   **`Git Merge <rama_a_fusionar> -m “Mensaje”`**: Permite realizar la fusión de ramas y **añadir un mensaje de commit directamente** sin necesidad de abrir un editor de texto.

### Eliminación de Ramas

*   **`Git Branch -d <rama_a_borrar>`**: Se utiliza para **borrar una rama local de forma segura**. Este comando no permite la eliminación si hay cambios que no se han guardado en el repositorio remoto o no se han fusionado con otras ramas.
*   **`Git Branch -D <rama_a_borrar>`**: Permite **forzar el borrado de una rama local**, independientemente de si se han realizado push o merge de sus cambios. Esta opción es menos segura y puede llevar a la pérdida de código si no se usa con precaución.
*   **`Git Push Origin --delete <rama_a_borrar>`**: Este comando se usa para **eliminar una rama del repositorio remoto**.

### Conceptos Relacionados con GitHub (No son Comandos Git directos, pero son parte del flujo de trabajo)

*   **Pull Request**: Es una herramienta de GitHub que permite **fusionar ramas y visualizar los cambios entre ellas** antes de la integración final. Facilita la revisión de código y la colaboración.
*   **Invitar Colaboradores**: Es un proceso dentro de GitHub que permite a los propietarios de un repositorio **otorgar permisos a otras personas para que puedan subir cambios** a su proyecto, facilitando el trabajo en equipo.