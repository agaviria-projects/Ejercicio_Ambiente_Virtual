# Análisis de Asistencia Estudiantes
Este proyecto realiza un análisis de datos a partir de dos fuentes:
- Un archivo `.csv` con los registros de asistencia de estudiantes
- Un archivo `.xlsx` con los datos de usuarios del sistema

El objetivo es extraer, limpiar y visualizar la información usando Python y librerías como `pandas`, `matplotlib` y `seaborn`.

---

## Estructura del proyecto
colectivoData20252/ ├── env/ # Ambiente virtual ├── asistencia_estudiantes_completo.csv ├── usuarios_sistema_completo.xlsx ├── analisis_asistencia.py # Script principal ├── requirements.txt # Librerías usadas └── readme.md # Descripción del proyecto

---

## Tecnologías utilizadas

- Python 3
- pandas
- matplotlib
- seaborn
- openpyxl

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/agaviria-projects/analisis-asistencia-python.git

2. Activar el entorno virtual:
env\Scripts\activate  # Windows

3.Instalar dependencias:
pip install -r requirements.txt

4.Ejecutar el script:
python analisis_asistencia.py

¿Qué hace este análisis?
Une datos de asistencia y usuarios por ID

Cuenta cuántos asistieron, faltaron o justificaron

Filtra por estrato, medios de transporte y más

Genera gráficos de barras con seaborn

#📸 Captura del gráfico generado

![Primeras filas](img/primeras_filas_v3.png)

![Conteo de asistencias](img/conteo_de_asistencias_v3.png)

![Transporte por estrato](img/medios_de_transporte_estrato_1_v3.png)

![Gráfico de asistencia](img/grafico_de_asistencia_v3.png)




## 😐Autor

- Héctor Alejandro  
- Estudiante de Tercer Semestre, CESDE  
- Proyecto académico: Nuevas Tecnologías / Análisis de Datos

## 📬 Contacto

- 📧 agaviria1408@gmail.com

