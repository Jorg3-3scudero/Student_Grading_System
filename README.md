#  Student Grading System

Sistema de gestión de calificaciones universitarias por línea de comandos construido en Python.

##  Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.7+**
- **Git** (opcional, para clonar el repositorio)

### Verificar instalación de Python
```bash
python3 --version
```

Si no tienes Python instalado:

#### En Ubuntu/Debian/Mint:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### En Fedora:
```bash
sudo dnf install python3 python3-pip
```

#### En Arch/Manjaro:
```bash
sudo pacman -S python python-pip
```

##  Instalación

### Opción 1: Clonar desde GitHub
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/student-grading-system.git

# Entrar al directorio
cd student-grading-system

# Verificar archivos
ls -la
```

### Opción 2: Descargar ZIP

1. Descarga el ZIP desde GitHub
2. Extrae el archivo
3. Abre terminal en la carpeta
```bash
cd /ruta/donde/extrajiste
```

## Uso

### Ejecutar el programa
```bash
python3 calification_system.py
```

### Primera ejecución

El programa cargará los estudiantes de ejemplo desde `students.json`:
```bash
----------MENU----------
1. Student list
2. Average grades
3. Upload calification
4. Cerrar asignatura
5. Salir
Ingrese una opcion:
```

##  Estructura del Proyecto
```
student-grading-system/
├── calification_system.py    # Programa principal
├── functions.py              # Funciones del sistema
├── students.json             # Base de datos JSON
├── README.md                 # Este archivo
└── .gitignore                # Archivos ignorados por Git
```

##  Solución de Problemas

### Error: `command not found: python3`
```bash
# Verificar si Python está instalado
which python3

# Si no está, instalar:
sudo apt update && sudo apt install python3
```

### Error: `No such file or directory: 'students.json'`
```bash
# Verificar que estás en el directorio correcto
pwd

# Listar archivos
ls -la

# Debe mostrar students.json
```

### Permisos denegados
```bash
# Dar permisos de ejecución (si es necesario)
chmod +x calification_system.py

# Ejecutar
./calification_system.py
```

##  Testing

### Prueba rápida del sistema
```bash
# Ejecutar el programa
python3 calification_system.py

# Opción 1: Ver estudiantes
# Opción 2: Consultar promedio de "Jorge"
# Opción 5: Salir
```

### Verificar que se guardaron los cambios
```bash
# Ver contenido de students.json
cat students.json

# O con formato más legible
python3 -m json.tool students.json
```

##  Reportar Problemas

Si encuentra un bug:

1. Verifica la versión de Python:
```bash
   python3 --version
```

2. Copia el error completo

3. Crea un [Issue](https://github.com/tu-usuario/student-grading-system/issues) con:
   - Descripción del problema
   - Pasos para reproducirlo
   - Mensaje de error completo
   - Tu sistema operativo y versión de Python



## Autor

**Jorge Ivan Escudero**
Estudiante de Desarrollo de Software - 2025

 Email: jorgeescudero160@gmail.com
 LinkedIn: https://www.linkedin.com/in/jorge-ivan-escudero-ibarra-4a0809237/)
 GitHub: https://github.com/Jorg3-3scudero

---

Si este proyecto te fue útil, dale una estrella en GitHub

