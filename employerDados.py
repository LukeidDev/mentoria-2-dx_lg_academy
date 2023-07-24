from class_ler_arquivo import EmployerData

file_path = "Employee Sample Data.xlsx"

emp_stats = EmployerData(file_path)

resultado = emp_stats.funcionarios_por_cargo_grupo()
print(resultado)
