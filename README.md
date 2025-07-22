# 🍽️ Restaurante Appbar

Aplicación móvil completa para restaurante desarrollada con **Flet** (Python + Flutter). Permite gestión de usuarios, productos, pedidos y carrito de compras.

## 📋 Características

### 🔐 Autenticación
- **Registro de usuarios** (clientes y administradores)
- **Inicio de sesión** con validación
- **Roles diferenciados** (Cliente/Administrador)

### 👥 Clientes
- **Visualización del menú** con categorías
- **Carrito de compras** con gestión de cantidades
- **Historial de pedidos** con estados
- **Perfil de usuario** personalizable

### 👨‍💼 Administradores
- **Dashboard** con estadísticas y gráficos
- **CRUD completo de productos** (Crear, Leer, Actualizar, Eliminar)
- **Gestión de pedidos** con estados
- **Panel de administración** completo

### 🛠️ Tecnologías
- **Flet** - Framework Python para UI
- **MySQL** - Base de datos
- **Python 3.8+** - Lenguaje principal

## 🚀 Instalación

### Prerrequisitos
- Python 3.8 o superior
- MySQL Server (opcional, funciona sin conexión)
- Git

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd restaurante_app_BAR
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar base de datos (opcional)**
```bash
# Editar src/data/database.py
# Cambiar configuración de MySQL:
config = {
    'host': 'localhost',
    'user': 'tu_usuario',
    'password': 'tu_password',
    'database': 'restaurante_appbar'
}
```

4. **Ejecutar la aplicación**
```bash
python src/main.py
```

## 📱 Uso de la Aplicación

### Datos de Prueba
- **Administrador**: `admin` / `admin123`
- **Cliente**: `cliente` / `cliente123`

### Funcionalidades Cliente
1. **Iniciar sesión** como cliente
2. **Explorar menú** por categorías
3. **Agregar productos** al carrito
4. **Gestionar carrito** (cantidades, eliminar)
5. **Realizar pedido**
6. **Ver historial** de pedidos

### Funcionalidades Administrador
1. **Iniciar sesión** como administrador
2. **Ver dashboard** con estadísticas
3. **Gestionar productos** (CRUD)
4. **Administrar pedidos** (estados)
5. **Configurar sistema**

## 📦 Generación de APK

### Opción 1: Usando Flet (Recomendado)

1. **Instalar Flet CLI**
```bash
pip install flet
```

2. **Generar APK**
```bash
flet pack src/main.py --name "Restaurante Appbar" --product-name "Restaurante Appbar"
```

### Opción 2: Usando BeeWare

1. **Instalar BeeWare**
```bash
python -m pip install briefcase
```

2. **Crear proyecto**
```bash
briefcase new
```

3. **Configurar y generar**
```bash
briefcase create android
briefcase build android
briefcase run android
```

### Cambiar Icono de la App

1. **Preparar icono**
   - Tamaño: 1024x1024 px
   - Formato: PNG
   - Nombre: `icon.png`

2. **Ubicación del icono**
   - Colocar en: `assets/icon.png`

3. **Configurar en Flet**
```python
# En main.py
ft.app(
    target=main,
    assets_dir="assets",
    icon="assets/icon.png"
)
```

## 🏗️ Estructura del Proyecto

```
restaurante_app_BAR/
├── src/
│   ├── main.py                 # Punto de entrada
│   ├── controllers/
│   │   └── auth_controller.py  # Controlador de autenticación
│   ├── views/
│   │   ├── login_view.py       # Vista de login/registro
│   │   ├── menu_view.py        # Vista del menú (clientes)
│   │   └── admin_view.py       # Vista de administrador
│   ├── components/
│   │   ├── appbar.py          # Barra de navegación
│   │   ├── drawer.py          # Menú lateral
│   │   └── tabs.py            # Componente de pestañas
│   ├── utils/
│   │   ├── helpers.py         # Funciones utilitarias
│   │   └── validators.py      # Validaciones
│   └── data/
│       └── database.py        # Conexión y operaciones DB
├── requirements.txt           # Dependencias
└── README.md                 # Documentación
```

## 🔧 Configuración

### Base de Datos MySQL

1. **Crear base de datos**
```sql
CREATE DATABASE restaurante_appbar;
```

2. **Configurar conexión**
Editar `src/data/database.py`:
```python
self.config = {
    'host': 'localhost',
    'user': 'tu_usuario',
    'password': 'tu_password',
    'database': 'restaurante_appbar'
}
```

### Variables de Entorno (Opcional)
Crear archivo `.env`:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=restaurante_appbar
```

## 🧪 Pruebas

### Ejecutar en modo desarrollo
```bash
python src/main.py
```

### Ejecutar en modo web
```bash
flet run --web src/main.py
```

### Ejecutar en modo móvil
```bash
flet run --mobile src/main.py
```

## 📊 Características Implementadas

### ✅ Completadas
- [x] **Autenticación** (Login/Registro)
- [x] **Tabs** de navegación
- [x] **NavigationDrawer** con menú lateral
- [x] **CircleAvatar** para usuarios
- [x] **CRUD de productos** completo
- [x] **Carrito de compras** funcional
- [x] **Gestión de pedidos** con estados
- [x] **Dashboard** con estadísticas
- [x] **Conexión MySQL** (con fallback a datos en memoria)
- [x] **Validaciones** de formularios
- [x] **Interfaz responsive**

### 🔄 En Desarrollo
- [ ] **Gráficos avanzados** con Chart.js
- [ ] **Notificaciones push**
- [ ] **Pagos en línea**
- [ ] **Geolocalización**
- [ ] **Modo offline**

## 🐛 Solución de Problemas

### Error de conexión MySQL
```
Error conectando a MySQL: [Errno 2003] Can't connect to MySQL server
```
**Solución**: La app funciona sin MySQL usando datos en memoria.

### Error de dependencias
```
ModuleNotFoundError: No module named 'flet'
```
**Solución**: `pip install -r requirements.txt`

### Error de permisos (Android)
```
Permission denied for android.permission.INTERNET
```
**Solución**: Agregar permisos en `android/app/src/main/AndroidManifest.xml`

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- Email: tu.email@ejemplo.com
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- **Flet Team** por el framework
- **Flutter** por la base de UI
- **MySQL** por la base de datos
- **Comunidad Python** por el soporte

---

## 📞 Soporte

Si tienes problemas o preguntas:
- 📧 Email: soporte@restaurante-appbar.com
- 💬 Discord: [Servidor de la comunidad]
- 📖 Documentación: [Wiki del proyecto]

**¡Disfruta usando Restaurante Appbar! 🍽️**
