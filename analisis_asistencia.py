import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leer los archivos
df_asistencia=pd.read_csv("asistencia_estudiantes_completo.csv")
df_usuarios=pd.read_excel("usuarios_sistema_completo.xlsx")

#Unir por coliumna 'id'
df_total=pd.merge(df_asistencia,df_usuarios,left_on="id_estudiante",right_on="id")

#Mostrar primeras filas
print(df_total.head())

#Conteo por estado (asistio,justificado,inasistencias)
print(df_total["estado"].value_counts())

#Transporte usaudo por estudiantes de estrato 1
print(df_total[df_total["estrato"]==1]["medio_transporte"].value_counts())

#Grafico del tipo de asistencia
sns.countplot(data=df_total,x="estado",palette="Set2")
plt.title("Frecuencia por tipo de asistencia")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()